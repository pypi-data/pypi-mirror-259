from __future__ import annotations

import importlib.util
from pathlib import Path

from nox import Session  # pyright: ignore [reportMissingImports]

if importlib.util.find_spec("tomllib"):
    pass  # pyright: ignore [reportMissingImports]
else:
    pass  # pyright: ignore [reportMissingImports]

from .misc import rm_file


def session_can_pip_install(session: Session) -> bool:
    return "--can-pipinstall" in session.posargs


def session_is_offline(session: Session) -> bool:
    return "--offline" in session.posargs


def session_upgrades_pip(session: Session) -> bool:
    return ("upgrade-pip" in session.posargs) and session_can_pip_install(session)


def remove_pip_tools_headers(req_file: Path) -> None:
    """
    Remove headers from a pip-tools generated requirement file.

    Args:
        req_file (Path): Path to the requirement file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    if not req_file.exists():
        msg = f"File not found: {req_file}"
        raise FileNotFoundError(msg)

    try:
        lines = req_file.read_text().split("\n")
        for i, line in enumerate(lines):  # noqa: B007
            if not line.startswith("#"):
                break
        with req_file.open("w") as file:
            file.write("\n".join(lines[i:]))
    except OSError as e:
        msg = f"Error removing headers: {e}"
        raise OSError(msg) from None


def upgrade_pip(session: Session, python: str | Path = "python", **session_kws) -> None:
    """
    Upgrade the pip package to the latest version.

    Args:
        session (Session): The Nox session.
        python (str | Path, optional): Path to the Python executable. Defaults to "python".
        **session_kws (dict, optional ): Additional keyword arguments for session.run.
    """
    if not session_can_pip_install(session):
        session.warn("Cannot upgrade pip (offline) !")
        return
    session.warn("Upgrading pip ...")
    session.run(str(python), "-m", "pip", "install", "--upgrade", "pip", **session_kws)
    if "upgrade-pip" in session.posargs:
        session.posargs.remove("upgrade-pip")


def install_precommit(session: Session, python: str | Path = "python", update: bool = True, **session_kws) -> None:
    """
    Install and optionally update the pre-commit tool.

    Args:
        session (Session): The Nox session.
        python (str | Path, optional): Path to the Python executable. Defaults to "python".
        update (bool, optional): Whether to update the pre-commit tool. Defaults to True.
        **session_kws (dict, optional ): Additional keyword arguments for session.run.
    """
    if not session_can_pip_install(session):
        session.warn("Cannot initializing pre-commit!")
        return

    session.warn("Initializing pre-commit ...")
    session.run(python, "-m", "pre_commit", "install", **session_kws)
    if update and not session_is_offline(session):
        session.warn("Updating pre-commit ...")
        session.run(python, "-m", "pre_commit", "autoupdate", **session_kws)


def install_nbstripout(session: Session, python: str | Path = "python", install: bool = True, **session_kws) -> None:
    """
    Install and initialize the nbstripout tool.

    Args:
        session (Session): The Nox session.
        python (str | Path, optional): Path to the Python executable. Defaults to "python".
        install (bool, optional): Whether to update the install the tool using .gitattributes. Defaults to True.
        **session_kws (dict, optional ): Additional keyword arguments for session.run.
    """
    if not session_can_pip_install(session):
        session.warn("Cannot install nbstripout!")
        return

    session.warn("Installing nbstripout ...")
    session.run(
        python,
        "-m",
        "pip",
        "install",
        "nbstripout",
        **session_kws,
    )
    session.run(
        "git config filter.nbstripout.extrakeys 'cell.metadata.papermill metadata.papermill'",
        **session_kws,
    )
    if install:
        session.warn("Initializing nbstripout ...")
        session.run(
            python,
            "-m",
            "nbstripout",
            "--install",
            "--attributes .gitattributes",
            **session_kws,
        )


def install_apt_deps(session: Session, *packages: list[str], **session_kws) -> None:
    """
    Install APT dependencies.

    Args:
        session (Session): The Nox session.
        *packages (list[str]): List of APT package names to install.
        **session_kws (dict, optional ): Additional keyword arguments for session.run.
    """
    if session_is_offline(session):
        session.warn("Cannot install APT packages (offline) ...")
        return
    packages = [pkg.strip() for pkg in packages]
    if not packages:
        return
    session.warn("Installing APT dependencies ...")
    session.run("sudo", "apt", "install", "-yqq", *packages, **session_kws)
    session.debug("APT dependencies installation complete.")


def compile_package_requirements(
    session: Session,
    req_filename: Path,
    extras: str = "",
    python: str | Path = "python",
    upgrade: bool = True,
    remove_header: bool = False,
    **session_kws,
) -> None:
    """
    Compile package requirements using piptools.

    Args:
        session (Session): The Nox session.
        req_filename (Path): Path to the requirement file to be generated.
        extras (str): Optional dependencies passed to --extra . Defaults to "".
        python (str | Path, optional): Path to the Python executable. Defaults to "python".
        upgrade (bool, optional): Whether to upgrade packages. Defaults to True.
        remove_header (bool, optional): Whether to remove pip-tools headers from the generated file. Defaults to False.
        **session_kws (dict, optional ): Additional keyword arguments for session.run.
    """

    if not session_can_pip_install(session):
        session.warn("Cannot compile_package_requirements!")
        return

    cwd = Path.cwd()
    upgrade_args = ["--upgrade"] if upgrade else []
    rm_file(req_filename)
    extras = extras.strip()
    extra_args = ["--extra", extras] if extras else []
    session.run(
        python,
        "-m",
        "piptools",
        "compile",
        "--quiet",
        *upgrade_args,
        "-o",
        str(req_filename.relative_to(cwd)),
        "pyproject.toml",
        *extra_args,
        **session_kws,
    )
    if remove_header:
        remove_pip_tools_headers(req_filename)


def compile_dev_requirements(
    session: Session,
    req_filename: Path,
    in_filenames: list[Path] | None = None,
    constraint_filenames: list[Path] | None = None,
    python: str | Path = "python",
    upgrade: bool = True,
    **session_kws,
) -> None:
    """
    Compile development requirements using piptools.

    Args:
        session (Session): The Nox session.
        req_filename (Path): Path to the requirement file to be generated.
        in_filenames (list[Path] | None, optional): List of in-files for generating requirements. Defaults to None.
        constraint_filenames (list[Path] | None, optional): List of constraint files for requirements. Defaults to None.
        python (str | Path, optional): Path to the Python executable. Defaults to "python".
        upgrade (bool, optional): Whether to upgrade packages. Defaults to True.
        **session_kws (dict, optional ): Additional keyword arguments for session.run.
    """
    if not session_can_pip_install(session):
        session.warn("Cannot compile_package_requirements!")
        return

    cwd = Path.cwd()
    rm_file(req_filename)

    upgrade_args = ["--upgrade"] if upgrade else []
    args: list[Path] = []
    if not isinstance(in_filenames, list):
        in_filenames = list(req_filename.parent.glob("*.in"))

    for filename in in_filenames:
        args.append("-r")
        args.append(str(filename.relative_to(cwd)) if isinstance(filename, Path) else filename)

    if isinstance(constraint_filenames, list):
        for filename in constraint_filenames:
            args.append("-c")
            args.append(str(filename.relative_to(cwd)) if isinstance(filename, Path) else filename)

    session.run(
        python,
        "-m",
        "piptools",
        "compile",
        "--quiet",
        *upgrade_args,
        "-o",
        str(req_filename),
        *args,
        **session_kws,
    )


def install_package(
    session: Session,
    package: str | list[str],
    python: str | Path = "python",
    upgrade: bool = True,
    constraint_filenames: list[Path] | None = None,
    **session_kws,
) -> None:
    """
    Install or upgrade a package using pip.

    Args:
        session (Session): The Nox session.
        package (str | List[str]): Package name(s) to install or upgrade.
        python (str | Path, optional): Path to the Python executable. Defaults to "python".
        upgrade (bool, optional): Whether to upgrade the package(s). Defaults to True.
        constraint_filenames (List[Path] | None, optional): List of constraint files for requirements. Defaults to None.
        **session_kws (dict, optional ): Additional keyword arguments for session.run.
    """
    if not session_can_pip_install(session):
        session.warn("Cannot install_package!")
        return

    cwd = Path.cwd()
    upgrade_args = ["--upgrade"] if upgrade else []

    if isinstance(package, str):
        package = [package]

    if not isinstance(package, list):
        msg = "package should be a string or a list of strings!"
        raise TypeError(msg)

    constraints_args = []
    constraints_comment = "without constraints"
    if isinstance(constraint_filenames, list):
        for filename in constraint_filenames:
            constraints_args.append("-c")
            constraints_args.append(str(filename.relative_to(cwd)) if isinstance(filename, Path) else filename)
        constraints_comment = f"with constraints {constraints_args}"

    msg = "Installing" if not upgrade else "Installing / upgrading"
    session.warn(f"{msg} {package} {constraints_comment} ...")

    session.run(
        python,
        "-m",
        "pip",
        "install",
        *package,
        *upgrade_args,
        *constraints_args,
        **session_kws,
    )


def install_requirements(
    session: Session,
    in_filenames: list[Path] | None = None,
    constraint_filenames: list[Path] | None = None,
    python: str | Path = "python",
    **session_kws,
) -> None:
    """
    Install packages listed in requirement files using pip.

    Args:
        session (Session): The Nox session.
        in_filenames (List[Path] | None, optional): List of requirement files to install packages from. Defaults to None.
        constraint_filenames (List[Path] | None, optional): List of constraint files for requirements. Defaults to None.
        python (str | Path, optional): Path to the Python executable. Defaults to "python".
        **session_kws (dict, optional ): Additional keyword arguments for session.run.
    """  # noqa: E501
    if not session_can_pip_install(session):
        session.warn("Cannot install_requirements!")
        return

    cwd = Path.cwd()
    args: list[Path] = []
    if not isinstance(in_filenames, list):
        msg = "in_filenames should be a list of requirement filenames"
        raise TypeError(msg)

    for filename in in_filenames:
        args.append("-r")
        args.append(str(filename.relative_to(cwd)) if isinstance(filename, Path) else filename)

    if isinstance(constraint_filenames, list):
        for filename in constraint_filenames:
            args.append("-c")
            args.append(str(filename.relative_to(cwd)) if isinstance(filename, Path) else filename)

    session.run(
        python,
        "-m",
        "pip",
        "install",
        *args,
        **session_kws,
    )
