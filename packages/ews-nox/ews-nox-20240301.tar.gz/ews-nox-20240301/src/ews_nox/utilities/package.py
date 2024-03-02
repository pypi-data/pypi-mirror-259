from __future__ import annotations

import logging
import re
import subprocess
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

import tomlkit
from nox import Session
from packaging.version import Version

from ews_nox.utilities.misc import rm_dir

logger = logging.getLogger(__name__)


def get_library_version(library_name: str, python: str = "python") -> str:
    """
    Get and return the version (__version__) of the specified library.

    Args:
        library_name (str): The name of the library to import.
        python (str, optional): Path to the Python executable. Defaults to "python".

    Returns:
        Version of the library.

    Raises:
        ValueError: If the library version cannot be obtained.
    """
    try:
        command = [
            python,
            "-c",
            f"import {library_name}; print({library_name}.__version__)",
        ]
        result = subprocess.run(
            command, shell=False, check=True, capture_output=True, text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        msg = f"Error getting library version: {e}"
        raise ValueError(msg) from None
    except (FileNotFoundError, OSError) as e:
        msg = f"Error executing command: {e}"
        raise ValueError(msg) from None


def inspect_wheel(session: Session, filename: Path) -> None:
    """
    Inspect the contents of a wheel file.

    Args:
        session (Session): The Nox session.
        filename (Path): Path to the wheel file to be inspected.
    """
    try:
        session.warn(f"Inspecting contents of wheel file: {filename}")
        session.run(
            "unzip",
            "-l",
            str(filename),
            external=True,
            silent=False,
        )
    except FileNotFoundError:
        session.error(
            "The 'unzip' command not found. Make sure 'unzip' is installed and available in your system."
        )
    except Exception as e:
        session.error(f"Error inspecting wheel file: {e}")


def inspect_sdist(session: Session, filename: Path) -> None:
    """
    Inspect the contents of a source distribution (sdist) file.

    Args:
        session (Session): The Nox session.
        filename (Path): Path to the sdist file to be inspected.
    """

    try:
        session.warn(
            f"Inspecting contents of source distribution (sdist) file: {filename}"
        )
        session.run(
            "tar",
            "tvfz",
            str(filename),
            external=True,
            silent=False,
        )
    except FileNotFoundError:
        session.error(
            "The 'tar' command not found. Make sure 'tar' is installed and available in your system."
        )
    except Exception as e:
        session.error(f"Error inspecting source distribution (sdist) file: {e}")


@dataclass
class Package:
    name: str
    namespace: str = ""
    root: Path | None = None
    is_namespace: bool = False
    tests_in_source: bool = True
    raise_on_error: bool = True

    """
    A dataclass containing an representation of a package.

    Args:
        name (str): The name of the package.
        namespace (str): The namespace of the package (Defaults to "").
        root (Path | None): The root path of the project (Defaults to None).
        tests_in_source (bool): Are the tests located in the source folder (Defaults to True).
        raise_on_error (bool): Do we raise exceptions on errors (Defaults to True).

    """

    def __post_init__(self) -> None:
        self.name = re.sub("_", "-", self.name.strip())
        self.namespace = re.sub("_", "-", self.namespace.strip())
        self.is_namespace = self.namespace != ""
        self._pyproject_toml = None
        if self.root is not None:
            self.root = Path(str(self.root)).resolve().absolute()
            self.pyproject_toml  # noqa

    @property
    def pyproject_toml(self) -> dict[str, str]:
        if self._pyproject_toml is None:
            if self.root is not None:
                self._pyproject_toml = tomlkit.loads(
                    self.pyproject_toml_file.read_bytes()
                )
            else:
                self._pyproject_toml = {}
        return self._pyproject_toml

    @property
    def name_with_namespace(self) -> str:
        """Name of the package with the namespace included

        Returns:
            The name of the package with the namespace included.
        """
        return f"{self.namespace}-{self.name}" if self.is_namespace else self.name

    @property
    def library_name(self) -> str:
        """Name of the library (Python import)

        Returns:
            The name of the library.
        """
        return re.sub("-", "_", self.name)

    @property
    def library_name_with_namespace(self) -> str:
        """Name of the library with the namespace included (Python import)

        Returns:
            The name of the library with the namespace included.
        """
        return (
            f"{self.namespace}_{self.library_name}"
            if self.is_namespace
            else self.library_name
        )

    @property
    def pyproject_toml_file(self) -> Path:
        """Location of the pyproject.toml

        Returns:
            The pyproject.toml
        """
        filename = self.root / "pyproject.toml"
        if not filename.is_file() and self.raise_on_error:
            raise FileNotFoundError(filename)
        return filename

    @property
    def src_dir(self) -> Path:
        """Location of the source directory

        Returns:
            The source directory
        """
        namespace = re.sub("-", "_", self.namespace)
        src_dir = self.root / "src"
        if self.is_namespace:
            src_dir = src_dir / namespace
        src_dir = src_dir / self.library_name
        if not src_dir.is_dir() and self.raise_on_error:
            raise FileNotFoundError(src_dir)
        return src_dir

    @property
    def venv_dir(self) -> Path:
        """
        Location of the virtual environment directory.

        Returns:
            Path to the virtual environment directory.
        """
        return self.root / ".venv"

    @property
    def has_venv(self) -> bool:
        """Does the package have a dev virtual envionnement

        Returns:
            True if the package has a dev virtual envionnement
        """
        return self.venv_dir.is_dir()

    @property
    def dist_dir(self) -> Path:
        """
        Location of the distribution directory.

        Returns:
            Path to the distribution directory.
        """
        return self.root / "dist"

    @property
    def docs_dir(self) -> Path:
        """
        Location of the documentation directory.

        Returns:
            Path to the documentation directory.
        """
        return self.root / "docs"

    @property
    def has_docs(self) -> bool:
        """Does the package have a MKDocs documentation

        Returns:
            True if the package has  documentation
        """
        return self.docs_dir.is_dir()

    @property
    def tests_dir(self) -> Path:
        """
        Location of the tests directory.

        Returns:
            Path to the tests directory.
        """
        if self.tests_in_source:
            return self.src_dir / "tests"
        return self.root / "tests"

    @property
    def has_tests(self) -> bool:
        """Does the package have a test-suite

        Returns:
            True if the package has test-suite
        """
        return self.tests_dir.is_dir()

    @property
    def requirements_dir(self) -> Path:
        """
        Get the path to the requirements directory.

        Returns:
            Path to the requirements directory.
        """
        return self.root / "requirements"

    @property
    def version(self) -> Version:
        """
        Find the current library version in the pyproject.toml.

        Returns:
            The extracted version string.
        """
        return Version(self.pyproject_toml["project"]["version"])

    def get_library_version(self, python: str = "python") -> str:
        """
        Get and return the version of the specified library.

        Args:
            python (str, optional): Path to the Python executable. Defaults to "python".

        Returns:
            Version of the library.

        Raises:
            ValueError: If the library version cannot be obtained.
        """
        return get_library_version(self.library_name_with_namespace, python=python)

    @property
    def lib_needs_compiler(self) -> bool:
        """
        Check if there are any .pyx files in the source directory.

        Returns:
            True if .pyx files are found, indicating a need for GCC compilation, False otherwise.
        """
        pyx_files = list(self.src_dir.glob("**/*.pyx"))
        return len(pyx_files) > 0

    def get_import_statements(self, print_version: bool = True) -> list[str]:
        """Return a list of import statements to be evaluated in python.

        Args:
            print_version (bool, optional): Do we want to print the version. Defaults to True.

        Returns:
            The list of import statements.
        """
        namespace = re.sub("-", "_", self.namespace)
        lib_name = self.library_name
        package_name = f"{namespace}.{lib_name}" if self.is_namespace else lib_name
        extra = f"print({package_name}.__version__)" if print_version else ""
        res = [f"import {package_name};{extra}"]
        if self.is_namespace:
            extra = f"print({lib_name}.__version__)" if print_version else ""
            res.append(f"from {namespace} import {lib_name};{extra}")
        return res

    def list_build_artifacts(self) -> list[Path]:
        """
        List build artifacts in the specified source directory.

        Returns:
            List of paths to build artifacts (e.g., .c, .so, .pyd files).
        """
        src_dir = self.src_dir
        build_artifacts = []
        build_artifacts += list(src_dir.glob("**/*.c"))
        build_artifacts += list(src_dir.glob("**/*.so"))
        build_artifacts += list(src_dir.glob("**/*.pyd"))
        return build_artifacts

    @property
    def egg_info_dirname(self) -> Path:
        """
        Location of the egg-info folder

        Returns:
            Location of the egg-info folder.
        """
        return self.src_dir / (self.library_name_with_namespace + ".egg-info")

    def remove_build_artifacts(self, *, callback: Callable | None = None) -> None:
        """
        Remove build artifacts and temporary files.

        This method removes build artifacts such as the 'build' directory and '*.egg-info' directory,
        as well as other temporary files generated during the build process.

        Args:
            session (Session, optional): The Nox session object. Defaults to None.
        """
        if callback:
            callback("Removing build artifacts ...")
        rm_dir(self.root / "build")
        rm_dir(self.egg_info_dirname)
        for filename in self.list_build_artifacts():
            filename.unlink()

    def get_dist_source_filename(self) -> str | Path:
        """Get the filename if the sdist file (tar.gz).

        Returns a string only if the file does not exist.

        Returns:
            The filename if the sdist file.
        """
        version = str(self.version)
        pattern = re.sub(
            "_",
            "-",
            (
                f"{self.namespace}-{self.name}-{version}.tar.gz"
                if self.is_namespace
                else f"{self.name}-{version}.tar.gz"
            ),
        )
        hits = self.dist_dir.glob(pattern)
        try:
            return next(hits)
        except StopIteration:
            return pattern

    def get_dist_wheel_filename(self, py_version: str = "") -> str | Path:
        """Get the filename if the wheel file for a given python version.

        Returns a string only if the file does not exist.

        Args:
            py_version (str) :  The python version.

        Returns:
            The filename if the sdist file.
        """

        version = str(self.version)
        if not self.lib_needs_compiler:
            return (
                self.dist_dir
                / f"{self.library_name_with_namespace}-{version}-py3-none-any.whl"
            )
        py_version = re.sub(r"\.", "", py_version.strip())
        assert py_version, f"py_version {py_version!r} should not be null"  # noqa: S101
        pattern = (
            f"{self.library_name_with_namespace}-{version}-cp{py_version}-cp{py_version}*.whl"
            if self.lib_needs_compiler
            else f"{self.library_name_with_namespace}-{version}-none-any.whl"
        )
        hits = self.dist_dir.glob(pattern)
        try:
            return next(hits)
        except StopIteration:
            return pattern

    # ------------------------------------------------------------------------ #
    # pyproject.toml
    # ------------------------------------------------------------------------ #

    def validate_toml(self) -> None:
        """Validate the `pyproject.toml` file"""
        pyproject = self._pyproject_toml
        if not pyproject:
            msg = "pyproject.toml not found."
            raise RuntimeError(msg)

        name: str = pyproject.get("project", {}).get("name", "")
        if name != self.name_with_namespace:
            msg = f"project.name should be {self.name_with_namespace}"
            raise RuntimeError(msg)

        build_requires: list[str] = pyproject.get("build-system", {}).get(
            "requires", []
        )
        if self.lib_needs_compiler:
            has_cython = len([_ for _ in build_requires if "cython" in _.lower()]) > 0
            if not has_cython:
                msg = "Did you forget to add cython as a dependency in pyproject.toml?"
                raise RuntimeError(msg)
            has_setup_py = (self.root / "setupy.py").is_file()
            if not has_setup_py:
                msg = "Did you forget to create the file setupy.py?"
                raise RuntimeError(msg)

        include: list[str] = (
            pyproject.get("tool", {})
            .get("setuptools", {})
            .get("packages", {})
            .get("find", {})
            .get("include", [])
        )
        assert len(include) > 0  # noqa: S101
        include = include[0]
        expected = self.namespace + "*"
        if expected != include:
            msg = f"tool.setuptools.packages.find.include should be [{expected}]. Found {include}"
            raise RuntimeError(msg)

        urls = pyproject.get("project", {}).get("urls", {})
        homepage_url = urls.get("Homepage", "")
        docs_url = urls.get("Documentation", "")
        source_url = urls.get("Source", "")

        name_with_namespace = self.name_with_namespace
        if not homepage_url.rstrip("/").endswith(name_with_namespace):
            msg = f"project.urls.Homepage {homepage_url!r} should end with {name_with_namespace!r}"
            raise RuntimeError(msg)

        if not docs_url.rstrip("/").endswith(name_with_namespace):
            msg = f"project.urls.Documentation {docs_url!r} should end with {name_with_namespace!r}"
            raise RuntimeError(msg)

        if not source_url.rstrip("/").endswith(name_with_namespace):
            msg = f"project.urls.Source {source_url!r} should end with {name_with_namespace!r}"
            raise RuntimeError(msg)

    @property
    def supported_python_versions(self) -> tuple[str]:
        """Returns a tuple containing the supported python versions from the classifiers.

        Returns:
            The tuple of python versions
        """
        pyproject = self._pyproject_toml
        if not pyproject:
            msg = "pyproject.toml not found."
            raise RuntimeError(msg)

        classifiers = pyproject.get("project", {}).get("classifiers", [])
        classifiers = [_.strip() for _ in classifiers]
        pattern = "Programming Language :: Python :: "
        return tuple(
            sorted(
                [
                    _.split(pattern, 1)[1].strip()
                    for _ in classifiers
                    if _.startswith(pattern)
                ]
            )
        )

    @property
    def optional_dependencies_dict(self) -> dict[str, str]:
        """Returns a dictionary containing the project optional dependencies.

        Returns:
            The dictionary
        """
        pyproject = self._pyproject_toml
        if not pyproject:
            msg = "pyproject.toml not found."
            raise RuntimeError(msg)
        return pyproject.get("project", {}).get("optional-dependencies", {})

    @property
    def install_extras(self) -> str:
        extras = ",".join(self.optional_dependencies_dict.keys())
        return extras


if __name__ == "__main__":
    p = Package(name="ews-nox-helpers", namespace="ewslib-core")
    p = Package(name="ews-nox", namespace="", root=Path("."), raise_on_error=True)
    print(p)
    print(p.src_dir)
    print(p.tests_dir)
    print(p.pyproject_toml_file)
    print(p.supported_python_versions)
    print(p.optional_dependencies_dict)
    print(p.name_with_namespace)
    print(p.library_name)
    print(p.library_name_with_namespace)
    print(p.get_import_statements())
    print(p.get_import_statements(print_version=False))
    print(p.get_dist_source_filename())
    print(p.get_dist_wheel_filename())
    print(p.get_dist_wheel_filename(py_version="3.10"))
    p.validate_toml()
