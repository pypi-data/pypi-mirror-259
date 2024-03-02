from __future__ import annotations

import contextlib
import io
import logging
import os
import re
import subprocess
from collections.abc import Callable
from copy import deepcopy
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from pprint import pprint

import nox
import tomlkit
from dotenv import load_dotenv
from nox import Session, session

from ews_nox.utilities.hosts import (
    get_hostname,
    get_is_connected_to_internet,
)
from ews_nox.utilities.installation import (
    compile_dev_requirements,
    compile_package_requirements,
    install_apt_deps,
    install_package,
    install_precommit,
    install_requirements,
    session_upgrades_pip,
    upgrade_pip,
)
from ews_nox.utilities.misc import rm_dir
from ews_nox.utilities.package import (
    Package,
    inspect_sdist,
    inspect_wheel,
)

with contextlib.suppress(ImportError):
    logging.getLogger("simple_toml_configurator").setLevel(logging.ERROR)
    logging.getLogger("Configuration").setLevel(logging.ERROR)
    logging.getLogger("ews_core_config").setLevel(logging.ERROR)
    from ews_core_config.config import read_settings

    read_settings()


def session_does_upgrade(session: Session) -> bool:
    """Does a session upgrade the packages

    By default, this will be False. Looks for update or upgrade in the session.posargs.

    Args:
        session (Session): The nox session

    Returns:
        True if we need to update the packages.
    """
    upgrade = False
    if "upgrade" in session.posargs:
        upgrade = True
        session.posargs.remove("upgrade")
    if "update" in session.posargs:
        upgrade = True
        session.posargs.remove("update")
    return upgrade


@dataclass
class NoxHelpers:
    """
    A dataclass containing various helper properties and methods for managing a Nox environment.

    Args:
        package (Package): The package.

        in_ci (bool): Flag indicating whether the environment is in a continuous integration (CI) context.

        apt_packages (list[str]): List of APT packages required by the project.
        apt_needs_sudo (bool): Do we need sudo to install apt packages.

        dev_python_version (str): Python version used for development.
        python_versions (list[str]): List of supported Python versions.
        venv_python_str (str): Path to the Python interpreter within the virtual environment.

        docs_enabled (bool): Do we want documentation using MkDocs.
        docs_port (int): Port for serving MkDocs documentation server.
        mkdocs_env (str): Environment variables for MkDocs configuration.
        docs_sub_site (str): Sub-site name for the documentation site.
        docs_site_url (str): URL of the documentation site.
        ewstools_url (str): URL of the EWSTools website.
        ewstools_host (str): Hostname used to upload docs on the EWSTools website.
        ewstools_user (str): Username used to upload docs on the EWSTools website.
        ewstools_password (str): Password used to upload docs on the EWSTools website.
        ewstools_port (int): Port used to upload docs on the EWSTools website.

        jupyter_enabled (bool): Do we want to serve a notebook server.
        jupyter_port (int): Port used to serve the Jupyter server.

        pypi_token (str): PyPI token for authentication.
        testpypi_token (str): Test PyPI token for authentication.

    """

    package: Package = field(init=True, repr=True)

    in_ci: bool = field(init=False, repr=True)
    is_connected_to_internet: bool = field(init=False, repr=True)
    dev_offline: bool = field(init=False, repr=True)
    can_pip_install: bool = field(init=False, repr=True)

    apt_needs_sudo: bool = field(init=False, repr=True, default=True)
    apt_packages: list[str] = field(init=False, repr=True)

    dev_python_version: str = field(init=False, repr=True)
    python_versions: list[str] = field(init=False, repr=True)
    venv_python_str: str = field(init=False, repr=True)

    docs_enabled: bool = field(init=False, repr=True, default=True)
    docs_port: int = field(init=False, repr=True, default=0)
    mkdocs_env: str = field(init=False, repr=True)
    docs_sub_site: str = field(init=False, repr=True)
    docs_site_url: str = field(init=False, repr=True)
    ewstools_url: str = field(init=False, repr=True, default="")
    ewstools_host: str = field(init=False, repr=True, default="")
    ewstools_port: int = field(init=False, repr=False, default=0)
    ewstools_user: str = field(init=False, repr=False, default="")
    ewstools_password: str = field(init=False, repr=False, default="")

    jupyter_enabled: bool = field(init=False, repr=True, default=True)
    jupyter_port: int = field(init=False, repr=True, default=0)

    pypi_token: str = field(init=False, repr=False)
    testpypi_token: str = field(init=False, repr=False)

    def load_project(self) -> tomlkit.TOMLDocument:
        """
        Load environment variables from files.

        This method loads environment variables from 'project.env' and '.env' files if they exist in the project's root directory.
        It populates the environment with variables defined in these files for use throughout the Nox environment management.

        Raises:
            FileNotFoundError: If 'ewsproject.toml' file is required but not found.
        """  # noqa: E501
        project_file = self.package.root / "ewsproject.toml"
        if project_file.is_file():
            project = tomlkit.loads(project_file.read_bytes())
        else:
            msg = f"{project_file.name!r} is required"
            raise FileNotFoundError(msg)

        env_file = self.package.root / ".env"
        if env_file.is_file():
            load_dotenv(env_file)

        return project

    @property
    def is_online(self) -> bool:
        return self.is_connected_to_internet and (not self.dev_offline)

    def __post_init__(self) -> None:
        """
        Initialize properties and configurations after instance creation.

        This method is automatically called after the instance of the NoxHelpers dataclass is created.
        It loads project configuration from 'pyproject.toml', reads environment variables from files,
        sets up various properties for managing the Nox environment, and prepares configurations for
        documentation and PyPI uploading.

        Raises:
            KeyError: If required environment variables are not found.
            FileNotFoundError: If project or environment files are not found.
        """

        self.is_connected_to_internet = get_is_connected_to_internet()
        self.dev_offline = os.getenv("DEV_OFFLINE", "0").upper() in ["YES", "1", "TRUE"]

        pip_index_url = os.getenv("PIP_INDEX_URL", "https://pypi.org/simple/")
        self.can_pip_install = self.is_online or "pypi.org" not in pip_index_url

        assert self.package.src_dir.is_dir()  # noqa: S101

        # Read configuration from project.env file
        project = self.load_project()

        # Python
        python_def = project.get("python", {})
        python_versions = python_def.get("supported-versions", [])
        if not python_versions:
            msg = "supported-versions key is required in ewsproject.toml / python"
            raise KeyError(msg)

        supported_python_versions = self.package.supported_python_versions
        python_versions = tuple(sorted([str(_) for _ in python_versions]))

        if python_versions != supported_python_versions:
            msg = f"{python_versions!r} != {supported_python_versions}"
            raise RuntimeError(msg)

        self.python_versions = python_versions
        self.dev_python_version = str(
            python_def.get("version", sorted(python_versions)[-1])
        )

        # APT packages
        apt_def = project.get("apt", {})
        self.apt_packages = apt_def.get("packages", [])
        self.apt_needs_sudo = apt_def.get("sudo", True)
        if self.package.lib_needs_compiler:
            self.apt_packages = ["gcc"] + [
                p.strip() for p in self.apt_packages if (p != "gcc") and p.strip()
            ]

        # MKDocks documentation
        documentation_def = project.get("documentation", {})
        self.docs_enabled = documentation_def.get("enabled", True)
        self.docs_port = documentation_def.get("port", -1)
        if self.docs_enabled and not self.docs_port:
            logging.warn(
                "Setting documentation / port key is required to serve MkDocs documentation server"
            )
        else:
            self.docs_port = int(self.docs_port)

        self.docs_enabled = self.docs_enabled and self.docs_port > 0

        project_config = self.package.pyproject_toml["project"]
        self.mkdocs_env = {
            "DOCS_SITE_URL": project_config["urls"]["Documentation"].rstrip("/"),
            "DOCS_REPO_NAME": project_config["name"],
            "DOCS_SITE_NAME": project_config["description"],
            "DOCS_REPO_URL": project_config["urls"]["Source"].rstrip("/"),
            "DOCS_AUTHOR": project_config["authors"][0]["name"],
            "DOCS_COPYRIGHT": f"Copyright &copy; {datetime.now().year} EWS Consulting",  # noqa: DTZ005
        }
        self.docs_site_url = self.mkdocs_env["DOCS_SITE_URL"]
        self.docs_sub_site = self.docs_site_url.split("/")[-1]

        self.ewstools_url = os.getenv("EWS_EWSTOOLS_URL", "").strip()
        self.ewstools_host = os.getenv("EWS_EWSTOOLS_HOST", "").strip()
        self.ewstools_user = os.getenv("EWS_EWSTOOLS_USERNAME", "").strip()
        self.ewstools_password = os.getenv("EWS_EWSTOOLS_PASSWORD", "").strip()
        self.ewstools_port = int(os.getenv("EWS_EWSTOOLS_PORT", "").strip())
        if not all(
            [
                self.ewstools_url,
                self.ewstools_host,
                self.ewstools_user,
                self.ewstools_password,
                self.ewstools_port,
            ]
        ):
            logging.warn(
                "Setting EWS_EWSTOOLS_URL / EWS_EWSTOOLS_HOST / EWS_EWSTOOLS_USERNAME"
                " / EWS_EWSTOOLS_PASSWORD / EWS_EWSTOOLS_PORT "
                "env. variables is required to upload the documentation to the EWS website"
            )

        # Jupyter
        jupyter_def = project.get("jupyter", {})
        self.jupyter_enabled = jupyter_def.get("enabled", True)
        self.jupyter_port = jupyter_def.get("port", 0)
        if not self.jupyter_port:
            logging.warn(
                "Setting jupyter / port key is required to serve a Jupyter server"
            )
        else:
            self.jupyter_port = int(self.jupyter_port)
        self.jupyter_enabled = self.jupyter_enabled and self.jupyter_port > 0

        # PYPI upload
        self.pypi_token = os.getenv("EWS_PYPI_TOKEN", "")
        self.testpypi_token = os.getenv("EWS_TESTPYPI_TOKEN", "")
        self.in_ci = bool(os.getenv("CI", ""))

        current_version = self.package.version

        self.venv_python_str = os.fsdecode(self.package.venv_dir.joinpath("bin/python"))

        self.session_kws = {}
        if self.in_ci:
            self.session_kws["python"] = self.dev_python_version
        else:
            self.session_kws["python"] = False
            self.session_kws["venv_backend"] = "none"
            self.session_kws["reuse_venv"] = True

    def augment_session_with_info(self, session: Session):
        posargs = session.posargs
        if "--can-pipinstall" not in posargs and self.can_pip_install:
            posargs.append("--can-pipinstall")

        misses_offline = "--offline" not in posargs
        if misses_offline and not self.is_online:
            posargs.append("--offline")

    def test_lib(
        self, session: Session, python: str = "python", print_version: bool = False
    ) -> None:
        """
        Run tests to check the library version using the provided Python interpreter.

        Args:
            session (Session): The Nox session object for running commands.
            python (str, optional): Path to the Python interpreter. Defaults to "python".
        """
        session.warn("Testing version ...")
        statements = self.package.get_import_statements(print_version=print_version)
        for statement in statements:
            session.run(
                python,
                "-c",
                statement,
                external=False,
            )

    @classmethod
    def get_dummy_session_name(cls, name: str) -> str:
        """
        Generate a formatted dummy session name.

        This class method generates a formatted string that serves as a visually distinguishable dummy session name.
        The generated string consists of a series of '#' characters surrounding the provided name, centered in a field of 30 characters.

        Args:
            name (str): The name to be displayed in the center of the formatted string.

        Returns:
            The formatted dummy session name.
        """  # noqa: E501
        s = "#" * 20
        s += name.center(30)
        s += "#" * 20
        return s

    def create_debug_session(self, *, session_name: str = "debug") -> Callable:
        """
        Create a debug session for showcasing NoxHelpers.

        This method creates a debug session using the provided session_name.
        The debug session displays the content of the current NoxHelpers instance using pprint.

        Args:
            session_name (str, optional): Name of the debug session. Defaults to "debug".

        Returns:
            A function representing the debug session.
        """

        @session(python=False, venv_backend="none", reuse_venv=True, name=session_name)
        def func(session: Session) -> None:
            """Show the nox helper."""
            if self.in_ci:
                pprint(self)
            else:
                pprint(asdict(self))

        func.__name__ = re.sub("-", "_", session_name)
        return func

    @classmethod
    def create_dummy_session(cls, *, session_name: str) -> Callable:
        """
        Create a dummy session with a formatted session name.

        This class method creates a dummy session named after the provided session_name.
        The dummy session is defined as a Nox session that does nothing.

        Args:
            session_name (str): Name of the dummy session.

        Returns:
            A function representing the dummy session.
        """

        @session(venv_backend="none", name=cls.get_dummy_session_name(session_name))
        def dummy() -> None:  # pyright: ignore [reportGeneralTypeIssues]
            """"""

        return dummy

    def test_is_in_venv(
        self, python_name: str, session: Session | None = None, do_raise: bool = True
    ):
        python = subprocess.run(
            f"which {python_name}",
            capture_output=True,
            shell=True,
            text=True,
            check=True,
        )
        python = Path(os.fsdecode(Path(python.stdout)))
        is_in_venv = False
        with contextlib.suppress(ValueError):
            is_in_venv = str(python.relative_to(self.package.venv_dir)).strip() != ""

        if session is not None and is_in_venv and do_raise:
            session.error(
                f"{python_name} already points to the .venv.\nPlease run deactivate!!!"
            )
        return is_in_venv

    def install_our_package(
        self,
        req_file_pkg,
        *,
        pipcompile: bool = False,
        pipinstall: bool = True,
        pipuninstall: bool = False,
        editable: bool = True,
        session: Session | None = None,
        silent: bool = True,
        **kwargs,
    ):
        python = kwargs.pop("python", "python")
        extras = self.package.install_extras

        if pipcompile:
            session.warn(f"Creating the package lock-files in {req_file_pkg.name} ...")
            compile_package_requirements(
                session, req_file_pkg, extras=extras, silent=silent, **kwargs
            )

        if pipinstall:
            editable_args = ("--editable",) if editable else ()
            session.warn("Installing our package ...")
            session.run(
                python,
                "-m",
                "pip",
                "install",
                *editable_args,
                f".[{extras}]" if extras else ".",
                "-c",
                str(req_file_pkg.relative_to(self.package.root)),
                silent=silent,
            )
        if pipuninstall:
            session.warn("Removing existing installation ...")
            session.run(
                python,
                "-m",
                "pip",
                "uninstall",
                "-y",
                f"{self.package.name_with_namespace}",
                silent=silent,
            )

    def create_dev_session(self, *, session_name: str = "dev") -> Callable:
        """
        Create a development environment setup session.

        This method creates a Nox session for setting up a Python development environment for the project.
        The session performs the following tasks:
        - Creates a Python virtual environment for the session.
        - Uses `venv` to create a global project virtual environment.
        - Invokes the Python interpreter from the global project environment to install the project and all its development dependencies.

        Args:
            session_name (str, optional): Name of the development session. Defaults to "dev".

        Returns:
            A function representing the development environment setup session.
        """  # noqa: E501

        @session(python=False, name=session_name, tags=["dev"])
        def func(session: Session) -> None:
            """
            Set up a Python development environment for the project.

            This session performs the following tasks:
            - Creates a virtual environment in .venv directory.
            - Installs APT dependencies.
            - Updates pip and installs pip-tools.
            - Creates lock-files for package and dev-dependencies.
            - Installs the project package and dev-dependencies.
            - Initializes a Git repository and installs pre-commit hooks.
            """
            self.augment_session_with_info(session)
            venv_python = [s for s in session.posargs if s.startswith("python")]
            venv_python = (
                f"python{self.dev_python_version}"
                if not venv_python
                else venv_python[0]
            )

            upgrade = session_does_upgrade(session)

            clear = False
            if "force" in session.posargs:
                clear = True
                session.posargs.remove("force")
            args = [] if not clear else ["--clear"]

            # Create the virtual env
            session.warn(
                f"Creating the virtual env in .venv (clear existing = {clear})..."
            )
            venv_dir_str = os.fsdecode(self.package.venv_dir)
            session.run(
                venv_python,
                "-m",
                nox.options.venv_backend,
                venv_dir_str,
                *args,
                silent=True,
            )
            python = self.venv_python_str

            # Install the APT dependencies
            install_apt_deps(session, *self.apt_packages, external=True, silent=True)

            is_empty = (not self.package.has_venv) or clear

            # Update pip if required
            if is_empty or session_upgrades_pip(session):
                upgrade_pip(session, python=python, silent=True)

            # Install pip tools
            install_package(session, "pip-tools", python=python, silent=True)

            # Create the lock-files
            requirements_dir = self.package.requirements_dir
            req_file_pkg = requirements_dir / "requirements.package.txt"

            self.install_our_package(
                req_file_pkg,
                pipcompile=True,
                pipinstall=True,
                editable=True,
                session=session,
                python=python,
                upgrade=upgrade,
                silent=True,
            )

            # Test that our package is installed
            session.warn("Testing our package installation ...")
            self.test_lib(session, python=python)

            # Create lock-files for the dev-dependencies
            req_file_deps = requirements_dir / "requirements.dev.txt"
            session.warn(
                f"Creating the development lock-files in {req_file_deps.name} ..."
            )
            compile_dev_requirements(
                session,
                req_file_deps,
                in_filenames=list(req_file_deps.parent.glob("*.in")),
                constraint_filenames=[req_file_pkg],
                python=python,
                upgrade=upgrade,
                silent=True,
            )

            # Install the dev-dependencies
            session.warn("Installing the dev-dependencies ...")

            install_requirements(
                session,
                in_filenames=[req_file_deps],
                constraint_filenames=[req_file_pkg],
                python=python,
                silent=True,
            )

            # Install the dev-dependencies
            if not (self.package.root / ".git").is_dir():
                session.warn("Initializing git repo ...")
                session.run(
                    "git",
                    "init",
                    ".",
                    silent=True,
                )

            # Install the pre-commit hooks
            install_precommit(session, python=python, update=True, silent=True)

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_upgrade_session(
        self, *, session_name: str = "upgrade", develop_func: Callable | None = None
    ) -> Callable:
        """
        Create a session for upgrading project dependencies.

        This method creates a Nox session for upgrading project dependencies using the specified 'develop_func'.
        The session is an alias for running the 'develop_func' with additional 'upgrade' and 'upgrade-pip' arguments.

        Args:
            session_name (str, optional): Name of the upgrade session. Defaults to "upgrade".
            develop_func (Callable, optional): A function representing the development setup session. Defaults to None.

        Returns:
            A function representing the upgrade dependencies session.
        """

        @session(**self.session_kws, name=session_name)
        def func(session: Session) -> None:
            """
            Update project dependencies (alias for develop -- upgrade upgrade-pip)

            This session upgrades project dependencies by running the specified 'develop_func' session
            with additional 'upgrade' and 'upgrade-pip' arguments.
            """
            self.augment_session_with_info(session)

            session.warn(
                "Updating the dependencies by running develop -- upgrade upgrade-pip"
            )
            session.posargs.append("upgrade")
            session.posargs.append("upgrade-pip")
            develop_func(session)

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_fix_session(self, *, session_name: str = "fix") -> Callable:
        """
        Create a session to fix the code using 'pre-commit run --all-files'.

        This method creates a Nox session that applies pre-commit checks and fixes to the codebase.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "fix".

        Returns:
            The created Nox session function.
        """

        @session(**self.session_kws, name=session_name)
        def func(session) -> None:
            """Fix the code using pre-commit run --all-files"""
            self.augment_session_with_info(session)
            pre_commit = (
                "pre-commit"
                if self.in_ci
                else str(self.package.venv_dir / "bin" / "pre-commit")
            )
            session.run(pre_commit, "run", "--all-files")

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_lint_session(self, *, session_name: str = "lint") -> Callable:
        """
        Create a session to lint the code using 'ruff' and 'codespell'. The '--fix' option can be used to fix the code.

        This method creates a Nox session that checks the codebase using black formatting,
        ruff linting, and codespell for spelling checks.

        Can also: `upgrade-pip`.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "lint".

        Returns:
            The created Nox session function.
        """

        @session(**self.session_kws, name=session_name)
        def func(session) -> None:
            """Check the code using ruff and codespell (use -- fix to fix the code)."""
            self.augment_session_with_info(session)
            python = "python" if self.in_ci else self.venv_python_str
            if session_upgrades_pip(session):
                upgrade_pip(session, python=python, silent=True)

            requirements_dir = self.package.requirements_dir
            if self.in_ci:
                req_file_pkg = (
                    requirements_dir / f"requirements.{session.python}.package.txt"
                )
                session.warn("Installing our package ...")
                session.run(
                    python,
                    "-m",
                    "pip",
                    "install",
                    ".",
                    "-c",
                    str(req_file_pkg.relative_to(self.package.root)),
                    silent=True,
                )
                session.warn("Installing 'lint.in' ...")
                constraint_filename = (
                    requirements_dir / f"requirements.{session.python}.dev.txt"
                )
                if not constraint_filename.is_file():
                    session.error(
                        f"Constraints file {constraint_filename.name}"
                        f" not found! Did you run nox -s lock-files-{session.python} ?"
                    )
                install_requirements(
                    session,
                    in_filenames=[str(requirements_dir / "lint.in")],
                    constraint_filenames=[constraint_filename],
                    python=python,
                    silent=True,
                )
            elif not (self.package.venv_dir / "bin" / "ruff").is_file():
                session.error("Program ruff not found! Did you run `nox -s develop` ?")

            files = [
                str(self.package.src_dir.relative_to(self.package.root)),
                "scripts",
            ] + [str(p) for p in Path(".").glob("*.py")]

            codespell = (
                (session.bin_paths[0] + "/codespell")
                if self.in_ci
                else os.fsdecode(self.package.venv_dir.joinpath("bin/codespell"))
            )

            if "fix" in session.posargs:
                session.run(python, "-m", "ruff", "check", "--fix", "--show-fixes")
                session.run(python, "-m", "ruff", "format", *files)
            else:
                session.run(python, "-m", "ruff", "check")
                session.run(codespell, "--toml", "pyproject.toml", *files, "docs")

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_test_matrix_session(
        self, *, session_name: str = "test-matrix"
    ) -> Callable:
        """
        Create a session to run the test suite across multiple Python versions.

        This method creates a Nox session that runs the test suite for different Python versions specified in
        the project configuration. It also installs required dependencies and coverage.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "test-matrix".

        Returns:
            The created Nox session function.
        """

        @session(python=self.python_versions, reuse_venv=True, name=session_name)
        def func(session: Session) -> None:
            """Run the test suite."""
            self.augment_session_with_info(session)

            python = "python"
            if session_upgrades_pip(session):
                upgrade_pip(session, python=python, silent=True)

            # Install the APT dependencies
            install_apt_deps(session, *self.apt_packages, external=True, silent=True)

            # Install our package
            requirements_dir = self.package.requirements_dir
            req_file_pkg = (
                requirements_dir / f"requirements.{session.python}.package.txt"
            )
            if not req_file_pkg.is_file():
                session.error(
                    f"Requirement file {req_file_pkg.name} not found! Did you run nox -s lock-files ?"
                )

            self.install_our_package(
                req_file_pkg,
                pipcompile=False,
                pipinstall=True,
                pipuninstall=False,
                editable=False,
                session=session,
                python=python,
                upgrade=False,
            )

            session.warn("Installing 'test.in' ...")
            constraint_filename = (
                requirements_dir / f"requirements.{session.python}.dev.txt"
            )
            if not constraint_filename.is_file():
                session.error(
                    f"Constraints file {constraint_filename.name} not found! Did you run nox -s lock-files ?"
                )
            install_requirements(
                session,
                in_filenames=[str(requirements_dir / "test.in")],
                constraint_filenames=[constraint_filename],
                python=python,
                silent=True,
            )
            session.run(
                "coverage",
                "run",
                "-m",
                "pytest",
                *[
                    _
                    for _ in session.posargs
                    if _ not in {"--can-pipinstall", "--offline"}
                ],
            )

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_test_session(self, *, session_name: str = "test") -> Callable:
        """
        Create a session to run the test suite and generate the coverage report.

        This method creates a Nox session that runs the test suite, generates the coverage report,
        and erases previous coverage data.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "test".

        Returns:
            The created Nox session function.
        """

        @session(python=False, venv_backend="none", reuse_venv=True, name=session_name)
        def func(session: Session) -> None:
            """Erase coverage / run the test suite using only the development python version and create the coverage report."""  # noqa: E501
            self.augment_session_with_info(session)
            session.notify("erase-cover")
            session.notify(f"test-matrix-{self.dev_python_version}")
            session.notify("cover")

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_tests_session(self, *, session_name: str = "tests") -> Callable:
        """
        Create a session to run the test suite for multiple Python versions and generate the coverage report.

        This method creates a Nox session that runs the test suite for different Python versions specified in
        the project configuration, generates the coverage report, and erases previous coverage data.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "tests".

        Returns:
            The created Nox session function.
        """

        @session(python=False, venv_backend="none", reuse_venv=True, name=session_name)
        def func(session: Session) -> None:
            """Erase coverage / run the test suite and create the coverage report."""
            self.augment_session_with_info(session)
            session.notify("erase-cover")
            for py_version in self.python_versions:
                session.notify(f"lock-files-{py_version}", ["update"])
                session.notify(f"test-matrix-{py_version}")
            session.notify("cover")

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_cover_session(self, *, session_name: str = "cover") -> Callable:
        """
        Create a session to run coverage and generate coverage reports.

        This method creates a Nox session that runs coverage on the project's codebase.
        It installs the 'coverage[toml]' package, combines coverage data, generates coverage reports,
        and cleans up coverage data. It also triggers the 'erase-cover' session to delete coverage-related files.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "cover".

        Returns:
            The created Nox session function.
        """

        @session(reuse_venv=True, python=self.dev_python_version, name=session_name)
        def func(session: Session) -> None:
            """Run coverage."""
            self.augment_session_with_info(session)
            if self.can_pip_install:
                session.install("coverage[toml]")

            session.run("coverage", "combine", silent=True)
            session.run("coverage", "report")
            session.run("coverage", "html", silent=True)
            session.run("coverage", "xml", "-o", "cov.xml", silent=True)
            session.run("coverage", "erase", silent=True)
            session.notify("erase-cover")

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def _erase_cover(
        self, *, session: Session | None = None, posargs: tuple[str] = ()
    ) -> None:
        """
        Delete coverage-related files and directories.

        This method deletes coverage-related files and directories from the project root.
        It removes 'cov.xml' files, '.coverage' files, and 'htmlcov' directories if 'html' is in 'posargs'.

        Args:
            session (Session, optional): The Nox session object. If provided, debug messages will be logged. Defaults to None.
            posargs (tuple[str], optional): Additional positional arguments passed to the session. Defaults to ().
        """  # noqa: E501

        if session:
            session.debug("Deleting cov.xml ...")
        p = subprocess.run(
            "find . -maxdepth 1 -type f -name cov.xml | xargs rm -f",
            check=True,
            shell=True,
            capture_output=True,
            text=True,
            cwd=self.package.root,
        )
        if not p:
            session.error(p.stderr)
        if session:
            session.debug("Deleting .coverage files ...")
        p = subprocess.run(
            'find . -maxdepth 1 -type f -name ".coverage*" | xargs rm -f',
            check=True,
            shell=True,
            capture_output=True,
            text=True,
            cwd=self.package.root,
        )
        if not p:
            session.error(p.stderr)

        if "html" in posargs:
            if session:
                session.debug("Deleting htmlcov ...")
            p = subprocess.run(
                "find . -maxdepth 1 -type d -name htmlcov | xargs rm -rf",
                check=True,
                shell=True,
                capture_output=True,
                text=True,
                cwd=self.package.root,
            )
            if not p:
                session.error(p.stderr)

    def create_erase_cover_session(
        self, *, session_name: str = "erase-cover"
    ) -> Callable:
        """
        Create a session to erase coverage files and htmlcov reports.

        This method creates a Nox session that deletes coverage artifacts, including coverage files and
        the 'htmlcov' directory.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "erase-cover".

        Returns:
            The created Nox session function.
        """

        @session(python=False, venv_backend="none", reuse_venv=True, name=session_name)
        def func(session: Session) -> None:
            """Erase the coverage files and the htmlcov report"""
            self.augment_session_with_info(session)
            session.log("Deleting coverage artifacts ...")
            self._erase_cover(session=session, posargs=())

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def delete_caches(self, *, session: Session | None = None) -> None:
        """
        Delete cached Python files and project-related caches.

        This method deletes cached Python files and project-related cache directories from the project root.
        It removes '__pycache__' directories, '.pyc' files, '.ruff_cache' directories, and '.pytest_cache' directories.

        Args:
            session (Session, optional): The Nox session object. If provided, debug messages will be logged. Defaults to None.
        """  # noqa: E501
        if session:
            session.debug("Deleting python files ...")
        p = subprocess.run(
            "find . -maxdepth 1 -type d -name __pycache__ | xargs rm -rf",
            check=True,
            shell=True,
            capture_output=True,
            text=True,
            cwd=self.package.root,
        )
        if not p:
            session.error(p.stderr)

        p = subprocess.run(
            rf"""find {self.package.root!s} -name "*.pyc" -delete""",
            check=True,
            shell=True,
            capture_output=True,
            text=True,
            cwd=self.package.root,
        )
        if not p:
            session.error(p.stderr)
        if session:
            session.debug("Deleting ruff_cache ...")
        p = subprocess.run(
            "find . -maxdepth 1 -type d -name .ruff_cache | xargs rm -rf",
            check=True,
            shell=True,
            capture_output=True,
            text=True,
            cwd=self.package.root,
        )
        if not p:
            session.error(p.stderr)
        if session:
            session.debug("Deleting pytest_cache ...")
        p = subprocess.run(
            "find . -maxdepth 1 -type d -name .pytest_cache | xargs rm -rf",
            check=True,
            shell=True,
            capture_output=True,
            text=True,
            cwd=self.package.root,
        )
        if not p:
            session.error(p.stderr)

    def create_clean_session(self, *, session_name: str = "clean") -> Callable:
        """
        Create a session to clean the project directory.

        This method creates a Nox session that cleans the project directory by removing build artifacts,
        cached files, documentation, and lock-files based on provided arguments.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "clean".

        Returns:
            The created Nox session function.
        """

        @session(python=False, name=session_name)
        def func(session: Session) -> None:
            """
            Clean the directory. Use `locks` to delete the lock-files, `docs` to clean the /site folder.
            `all` cleans everything.
            """
            self.augment_session_with_info(session)
            session.log("Cleaning build artifacts ...")

            is_all = "all" in session.posargs

            # Coverage
            self._erase_cover(session=session, posargs=())

            if is_all:
                self.delete_caches(session=session)
                rm_dir(self.package.dist_dir)

            if ("docs" in session.posargs) or is_all:
                rm_dir(self.package.root / "site")
                rm_dir(self.package.root / "htmlcov")

            if ("locks" in session.posargs) or is_all:
                for filename in self.package.requirements_dir.glob("requirements*.txt"):
                    filename.unlink()

            self.package.remove_build_artifacts(callback=session.debug)

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_package_build_session(
        self, *, session_name: str = "package-build"
    ) -> Callable:
        """
        Create a session to build the package using different Python versions.

        This method creates a Nox session that builds the package using different Python versions, creating
        both wheel and source distribution (sdist) files.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "package-build".

        Returns:
            The created Nox session function.
        """

        @session(
            python=self.python_versions,
            reuse_venv=True,
            name=session_name,
        )
        def func(session: Session) -> None:
            """
            Build the package using different python versions.
            """
            self.augment_session_with_info(session)

            self.package.remove_build_artifacts(callback=session.debug)

            # Update pip and build
            install_package(session, ["pip", "build"], python="python", silent=True)

            self.install_our_package(
                None,
                pipcompile=False,
                pipinstall=False,
                pipuninstall=True,
                session=session,
                silent=True,
            )

            opt_args = []
            if session.python == self.dev_python_version:
                opt_args.append("--sdist")

            session.warn("Build the package ...")
            session.run(
                "python",
                "-m",
                "build",
                *opt_args,
                "--wheel",
                "--outdir",  # cspell:disable-line
                str(self.package.dist_dir),
                ".",
                silent=True,
            )

            wheel_name = self.package.get_dist_wheel_filename(py_version=session.python)
            wheel_not_found = isinstance(wheel_name, str)
            if not wheel_not_found:
                session.log(f"Built {wheel_name.name!r}")
            else:
                session.error(f"Could not find {wheel_name!r}")

            inspect_wheel(session, wheel_name)

            if session.python == self.dev_python_version:
                sdist_name = self.package.get_dist_source_filename()
                sdist_not_found = isinstance(sdist_name, str)
                if not sdist_not_found:
                    session.log(f"Built {sdist_name.name!r}")
                else:
                    session.error(f"Could not find {sdist_name!r}")

                inspect_sdist(session, sdist_name)

            # Test that our package is installed
            session.warn("Installing package from wheel ...")
            session.run(
                "python",
                "-m",
                "pip",
                "install",
                "--force-reinstall",
                str(wheel_name.relative_to(self.package.root)),
                silent=True,
            )

            # Test that our package is installed
            session.warn("Testing our package installation ...")
            self.test_lib(session, python="python")

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_lock_files_session(
        self, *, session_name: str = "lock-files"
    ) -> Callable:
        """
        Create a session to generate lock-files for dependencies.

        This method creates a Nox session that generates lock-files for package dependencies, both for
        the main package and for development dependencies.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "lock-files".

        Returns:
            The created Nox session function.
        """

        @session(
            python=self.python_versions,
            reuse_venv=True,
            name=session_name,
        )
        def func(session: Session) -> None:
            """
            Generate the lock-files (use -- upgrade / update to update the dependencies).
            """
            self.augment_session_with_info(session)

            upgrade = session_does_upgrade(session)

            # Upgrade pip
            install_package(session, "pip", python="python", silent=True)

            # Install pip tools
            install_package(session, "pip-tools", python="python", silent=True)

            # Create the lock-files
            requirements_dir = self.package.requirements_dir
            req_file_pkg = (
                requirements_dir / f"requirements.{session.python}.package.txt"
            )
            self.install_our_package(
                req_file_pkg,
                pipcompile=True,
                pipinstall=False,
                pipuninstall=False,
                editable=False,
                session=session,
                python="python",
                upgrade=upgrade,
                silent=True,
            )

            # Create lock-files for the dev-dependencies
            req_file_deps = requirements_dir / f"requirements.{session.python}.dev.txt"
            session.warn(
                f"Creating the development lock-files in {req_file_deps.name} ..."
            )
            compile_dev_requirements(
                session,
                req_file_deps,
                in_filenames=list(req_file_deps.parent.glob("*.in")),
                constraint_filenames=[req_file_pkg],
                python="python",
                upgrade=upgrade,
                silent=True,
            )

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_upgrade_lock_files(
        self,
        *,
        session_name: str = "upgrade-lock-files",
        lock_files_func: Callable | None = None,
    ) -> Callable:
        """
        Create a session to update dependencies by running the lock-files session with upgrade.

        This method creates a Nox session that updates dependencies by running the 'lock-files' session with
        the additional 'upgrade' argument.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "upgrade-lock-files".
            lock_files_func (Callable | None, optional): The lock-files session function. Defaults to None.

        Returns:
            The created Nox session function.
        """

        @session(python=False, name=session_name)
        def func(session: Session) -> None:
            """Update the dependencies (alias for lock-files -- upgrade)"""

            available_versions = lock_files_func.python
            if "all" in session.posargs:
                py_versions = list(available_versions)
            else:
                py_versions = [
                    arg for arg in available_versions if arg in session.posargs
                ]

            for py_version in py_versions:
                session.notify(f"lock-files-{py_version}", ["update"])

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_package_publish_session(
        self, *, session_name: str = "package-publish"
    ) -> Callable:
        """
        Create a session to upload the package to the PyPI Server.

        This method creates a Nox session that uploads the built package to the PyPI Server. The target can be
        'pypi', 'testpypi', or 'local', each with its respective configurations.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "package-publish".

        Returns:
            The created Nox session function.
        """

        @session(
            python=self.dev_python_version,
            reuse_venv=True,
            name=session_name,
        )
        def func(session: Session) -> None:
            """
            Upload the package to the PyPI Server using -- ... .Choose any of 'pypi', 'testpypi' or 'local' (can be several).
            """  # noqa: E501

            python = "python"
            install_package(session, ["twine"], python=python, silent=True)
            opt_args = []
            if session.python == self.dev_python_version:
                opt_args.append("--sdist")

            wheel_name = self.package.get_dist_wheel_filename(py_version=session.python)
            wheel_not_found = isinstance(wheel_name, str)
            session.log(f"Looking for wheel {wheel_name!r}")
            if not wheel_not_found:
                session.log(f"Built {wheel_name.name!r}")
            else:
                session.error(f"Could not find {wheel_name!r}")

            files = [wheel_name]

            if session.python == self.dev_python_version:
                sdist_name = self.package.get_dist_source_filename()
                if sdist_name.is_file():
                    session.log(f"Built {sdist_name.name!r}")
                else:
                    session.error(f"Could not find {sdist_name!r}")
                files += [sdist_name]

            session.run(
                python,
                "-m",
                "twine",
                "check",
                "--strict",
                *files,
                external=False,
                silent=False,
            )

            for target in session.posargs:
                twine_env = {}

                if target == "pypi":
                    twine_env["TWINE_USERNAME"] = "__token__"
                    twine_env["TWINE_PASSWORD"] = self.pypi_token
                    twine_env["TWINE_REPOSITORY"] = "pypi"
                elif target == "testpypi":
                    twine_env["TWINE_USERNAME"] = "__token__"
                    twine_env["TWINE_PASSWORD"] = self.testpypi_token
                    twine_env["TWINE_REPOSITORY"] = "testpypi"
                elif target == "local":
                    twine_env["PIP_TRUSTED_HOST"] = os.getenv("PIP_EXTRA_INDEX_URL", "")
                    twine_env["PIP_EXTRA_INDEX_URL"] = os.getenv("PIP_TRUSTED_HOST", "")
                    twine_env["TWINE_USERNAME"] = ""
                    twine_env["TWINE_PASSWORD"] = "."  # noqa: S105
                    twine_env["TWINE_REPOSITORY_URL"] = os.getenv("LOCAL_PYPI_URL", "")
                    if self.in_ci:
                        session.warn(
                            "Uploading to private PyPI server is not supported in CI."
                        )
                        continue
                else:
                    session.error(
                        f"Target {target!r} not supported! Choose one of 'pypi', 'testpypi' or 'local'"
                    )
                    continue

                session.warn(f"Uploading to {target}")
                session.run(
                    python,
                    "-m",
                    "twine",
                    "upload",
                    "--verbose",
                    "--non-interactive",
                    "--skip-existing",
                    *files,
                    external=False,
                    silent=True,
                    env=twine_env,
                )

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_notebook_session(self, *, session_name: str = "juypter") -> Callable:
        """
        Create a session to run the Jupyter notebook.

        This method creates a Nox session that runs the Jupyter notebook, allowing for interactive exploration
        and demonstration of code.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "package-publish".

        Returns:
            The created Nox session function.
        """

        @session(
            **self.session_kws,
            name=session_name,
        )
        def func(session: Session) -> None:
            """
            Run the juypter notebook
            """

            upgrade = session_does_upgrade(session)

            python = self.venv_python_str

            constraint_filenames = [
                self.requirements_dir / "requirements.package.txt",
                self.requirements_dir / "requirements.dev.txt",
            ]
            install_package(
                session,
                ["jupyter", "notebook>=7", "ipykernel"],  # cspell:disable-line
                python=python,
                upgrade=upgrade,
                constraint_filenames=constraint_filenames,
                silent=True,
            )

            examples_dir = self.package.root / "examples"
            if not examples_dir.is_dir():
                examples_dir.mkdir()

            session.run(
                python,
                "-m",
                "ipykernel",  # cspell:disable-line
                "install",
                "--sys-prefix",
                "--display-name",
                self.lib_name_with_namespace,
                "--name",
                self.lib_name_with_namespace,
                silent=True,
            )
            session.warn(f"Serving Jupyter Notebook on port {self.jupyter_port}")
            session.warn(
                f"Please open you browser on http://{get_hostname()}:{self.jupyter_port}"
            )
            session.run(
                python,
                "-m",
                "jupyter",
                "notebook",
                f"--notebook-dir={examples_dir!s}",
                "--ip=0.0.0.0",
                f"--port={self.jupyter_port}",
                "--ServerApp.port_retries=0",
                "--ServerApp.allow_origin=*",
                "--ServerApp.password=",
                "--ServerApp.token=",
                "--no-browser",
                "--KernelSpecManager.ensure_native_kernel=False",
                f"--KernelSpecManager.whitelist={self.lib_name_with_namespace}",
                f"--MultiKernelManager.default_kernel_name={self.lib_name_with_namespace}",
                env={"PYDEVD_DISABLE_FILE_VALIDATION": "1"},  # cspell:disable-line
            )

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_docs_session(self, *, session_name: str = "docs") -> Callable:
        """
        Create a session to serve or build documentation.

        This method creates a Nox session that serves the documentation using the MkDocs development server.
        The 'build' argument can be added to build the documentation instead of serving it.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "docs".

        Returns:
            The created Nox session function.
        """

        @session(
            **self.session_kws,
            name=session_name,
        )
        def func(session: Session) -> None:
            """
            Run the server (default) or build the documentation (-- `build`).

            You can upgrade pip by adding `upgrade-pip` and upgrade the mkdocs packages by with `upgrade`
            """
            if not self.package.has_docs:
                session.error("No documentation found!")

            python = "python" if self.in_ci else self.venv_python_str
            if session_upgrades_pip(session):
                upgrade_pip(session, python=python, silent=True)

            requirements_dir = self.package.requirements_dir
            req_file_pkg = requirements_dir / "requirements.package.txt"
            if self.in_ci:
                req_file_pkg = (
                    requirements_dir / f"requirements.{session.python}.package.txt"
                )
                self.install_our_package(
                    req_file_pkg,
                    pipcompile=False,
                    pipinstall=True,
                    pipuninstall=False,
                    editable=False,
                    session=session,
                    python=python,
                    silent=True,
                )
                session.warn("Installing 'docs.in' ...")
                constraint_filename = (
                    requirements_dir / f"requirements.{session.python}.dev.txt"
                )
                if not constraint_filename.is_file():
                    session.error(
                        f"Constraints file {constraint_filename.name} not found! Did you run nox -s lock-files ?"
                    )
                install_requirements(
                    session,
                    in_filenames=[str(requirements_dir / "docs.in")],
                    constraint_filenames=[constraint_filename],
                    python=python,
                    silent=True,
                )
            elif not (self.package.venv_dir / "bin" / "mkdocs").is_file():
                session.error(
                    "Program mkdocs not found! Did you run `nox -s develop` ?"
                )

            whole_name = self.package.library_name_with_namespace
            p = subprocess.run(
                f"{python} -c 'import {whole_name}'",
                shell=True,
                capture_output=True,
                check=False,
                text=True,
            )
            module_is_installed = p.returncode == 0
            session.debug(f"Module {whole_name!r} is installed: {module_is_installed}")

            (self.package.root / "htmlcov").mkdir(parents=False, exist_ok=True)

            mkdocs_env = deepcopy(self.mkdocs_env)
            if "build" in session.posargs:
                mkdocs_env.update(BUILD_DOCS="1")
                site_dir = self.package.root / "site"

                if not self.in_ci:
                    self.install_our_package(
                        req_file_pkg,
                        pipcompile=False,
                        pipinstall=True,
                        pipuninstall=False,
                        editable=True,
                        session=session,
                        python=python,
                        silent=True,
                    )

                session.log("Build documentation ...")
                rm_dir(site_dir)
                args = []
                session.run(
                    python,
                    "-m",
                    "mkdocs",
                    "build",
                    *args,
                    env=mkdocs_env,
                    silent=True,
                )
                return

            if self.in_ci:
                session.error("Documentation server should not run in CI")

            if not module_is_installed:
                self.install_our_package(
                    req_file_pkg,
                    pipcompile=False,
                    pipinstall=True,
                    pipuninstall=False,
                    editable=True,
                    session=session,
                    python=python,
                    silent=True,
                )

            mkdocs_env.update(BUILD_DOCS="0")
            session.warn(f"Serving documentation on port {self.docs_port}")
            session.warn(
                f"Please open you browser on http://{get_hostname()}:{self.docs_port}"
            )
            session.run(
                python,
                "-m",
                "mkdocs",
                "serve",
                "--livereload",  # cspell:disable-line
                "--dev-addr",
                f"0.0.0.0:{self.docs_port}",
                env=mkdocs_env,
            )

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_docs_show_session(self, *, session_name: str = "docs-show") -> Callable:
        """
        Create a session to show the results of 'docs -- build' using a simple HTTP server.

        This method creates a Nox session that uses a simple HTTP server to show the results of building
        the documentation using the 'docs -- build' command.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "docs-show".

        Returns:
            The created Nox session function.
        """

        @session(
            **self.session_kws,
            name=session_name,
        )
        def func(session: Session) -> None:
            """
            Show the results of `docs -- build` using a simple http server.
            """
            if self.in_ci:
                session.error("Documentation site should not be served in CI")
            if not (self.package.root / "site").is_dir():
                session.error("No documentation site not found!")

            session.warn(f"Please open you browser on http://{get_hostname()}:8000")
            session.warn("Press Ctrl + C to exit")
            session.run(
                self.venv_python_str,
                "-m",
                "http.server",
                "8000",
                "-d",
                str(self.package.root / "site"),
                silent=True,
            )

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_docs_upload_session(
        self, *, session_name: str = "docs-upload"
    ) -> Callable:
        """
        Create a session to upload the documentation site to the EWS FTP server.

        This method creates a Nox session that uploads the built documentation site to an FTP server.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "docs-upload".

        Returns:
            The created Nox session function.
        """

        @session(
            **self.session_kws,
            name=session_name,
        )
        def func(session: Session) -> None:
            """
            Upload the documentation site to EWS Server
            """
            if self.in_ci:
                session.error("Documentation site cannot be uploaded in CI")
            if not (self.package.root / "site").is_dir():
                session.error("No documentation site not found!")

            upgrade = session_does_upgrade(session)

            constraint_filenames = [
                self.requirements_dir / "requirements.package.txt",
                self.requirements_dir / "requirements.dev.txt",
            ]
            install_package(
                session,
                ["pysftp"],  # cspell:disable-line
                python=self.venv_python_str,
                upgrade=upgrade,
                constraint_filenames=constraint_filenames,
                silent=True,
            )

            session.warn(f"Uploading to SFTP server {self.ewstools_url} ...")
            session.run(
                self.venv_python_str,
                str(self.package.root / "scripts" / "upload_docs.py"),
                silent=True,
            )

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_nox_size_session(self, *, session_name: str = "nox-size") -> Callable:
        """
        Create a session to show the size of all subfolders in the .nox folder.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "nox-size".

        Returns:
            The created Nox session function.
        """

        @session(
            python=False,
            name=session_name,
        )
        def func(session: Session) -> None:
            """
            Show the size of the .nox folders
            """
            error = "Errors"
            out = "Folder sizes:\n"
            cmd = r"sh -c 'du -bh --all -d0 .venv'"
            p = subprocess.run(
                cmd,
                capture_output=True,
                check=True,
                text=True,
                shell=True,
            )
            if not p:
                error += p.stderr.strip()
            out += p.stdout.strip() + "\n"

            cmd = r"ls .nox | xargs -I %  sh -c 'du -bh --all -d0 .nox/%'"
            p = subprocess.run(
                cmd,
                capture_output=True,
                check=True,
                text=True,
                shell=True,
            )
            if not p:
                error += p.stderr.strip()
            out += p.stdout.strip()

            session.debug(out)

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_git_sizes_session(self, *, session_name: str = "git-sizes") -> Callable:
        """
        Create a session to show the file sizes of the .git folder (LFS).

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "git-sizes".

        Returns:
            The created Nox session function.

        Example:

            nox -s git-sizes -- --threshold=100KB


        """

        @session(
            python=False,
            name=session_name,
        )
        def func(session: Session) -> None:
            """
            Show show the file sizes of the .git folder (LFS) (ex: nox -s git-sizes -- --threshold=100KB)
            """

            posargs = "  ".join(session.posargs)
            cmd = rf'''du -bh --all {posargs} .git | sort -k1 -rh  | grep -E ".*\/objects\/.*\/.*\/.*|.git$"'''
            session.warn(cmd)
            p = subprocess.run(
                cmd,
                cwd=self.package.root,
                capture_output=True,
                check=True,
                text=True,
                shell=True,
            )
            if not p:
                session.error(p.stderr)
            session.debug("\n" + p.stdout.strip())

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_file_sizes_session(
        self, *, session_name: str = "file-sizes"
    ) -> Callable:
        """
        Create a session to show the file sizes.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "file-sizes".

        Returns:
            The created Nox session function.

        Example:

            nox -s file-sizes -- --threshold=10KB

        """

        @session(
            python=False,
            name=session_name,
        )
        def func(session: Session) -> None:
            """
            Show show the file sizes (ex: nox -s file-sizes -- --threshold=100KB)
            """

            posargs = "  ".join(session.posargs)
            cmd = rf'find src docs tests scripts -type f -not -iname "*.pyc" -exec du {posargs} -a {{}} +  | sort -n -r'
            session.warn(cmd)
            p = subprocess.run(
                cmd,
                cwd=self.package.root,
                capture_output=True,
                check=True,
                text=True,
                shell=True,
            )
            if not p:
                session.error(p.stderr)
            session.debug("\n" + p.stdout.strip())

        func.__name__ = re.sub("-", "_", session_name)
        return func

    def create_show_self_session(self, *, session_name: str = "self") -> Callable:
        """
        Create a session to the configuration.

        Args:
            session_name (str, optional): The name of the created Nox session. Defaults to "self".

        Returns:
            The created Nox session function.
        """

        @session(
            python=False,
            name=session_name,
        )
        def func(session: Session) -> None:
            """
            Show the configuration
            """
            from pprint import pprint

            stream = io.StringIO()
            pprint(self, stream=stream)
            msg = stream.getvalue()
            session.debug(msg)

        func.__name__ = re.sub("-", "_", session_name)
        return func
