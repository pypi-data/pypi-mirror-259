from __future__ import annotations

import subprocess


class GitError(Exception):
    pass


def get_username() -> str:
    """
    Get the user name

    Returns:
        Name of the user

    Raises:
        ValueError: If there is an error retrieving the user name.
    """
    try:
        p = subprocess.run(
            "git config --get user.name",
            shell=True,
            capture_output=True,
            text=True,
            check=True,
        )
        if not p.returncode:
            return p.stdout.strip()
    except subprocess.CalledProcessError as e:
        msg = f"Error getting username: {e}"
        raise ValueError(msg) from None
    return ""


def get_email() -> str:
    """
    Get the user email

    Returns:
        E-mail of the user

    Raises:
        ValueError: If there is an error retrieving the user email.
    """
    try:
        p = subprocess.run(
            "git config --get user.email",
            shell=True,
            capture_output=True,
            text=True,
            check=True,
        )
        if not p.returncode:
            return p.stdout.strip()
    except subprocess.CalledProcessError as e:
        msg = f"Error getting username: {e}"
        raise ValueError(msg) from None
    return ""


def get_branch() -> str:
    """
    Get the name of the current Git branch.

    Returns:
        Name of the current branch.

    Raises:
        ValueError: If there is an error retrieving the branch name.
    """
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        msg = f"Error getting branch name: {e}"
        raise ValueError(msg) from None
    except FileNotFoundError:
        msg = "Git executable not found. Make sure Git is installed and available in your system."
        raise ValueError(msg) from None


def get_hash(short: bool = False) -> str:
    """Get the current commit hash

    Args:
        short (bool, optional): Do we ant the short hash. Defaults to False.

    Returns:
        The current commit hash
    """
    cmds = [
        "git rev-parse",
        "--short" if short else "",
        "--verify HEAD",
    ]
    return (
        subprocess.run(
            " ".join(cmds).strip(),
            shell=True,
            check=True,
            capture_output=True,
        )
        .stdout.decode()
        .strip()
    )


def get_status() -> list[str]:
    """
    Get the results of `git status`.

    Returns:
        List of lines representing the git status.

    Raises:
        ValueError: If there is an error retrieving git status.
    """
    # https://github.com/c4urself/bump2version/blob/bc95374d0dff73e610bed520846f88859815e532/bumpversion/vcs.py#L66
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            check=True,
            capture_output=True,
            text=True,
        )
        output_lines = result.stdout.splitlines()
        non_ignored_lines = [line.strip() for line in output_lines if not line.strip().startswith("??")]
        return non_ignored_lines
    except subprocess.CalledProcessError as e:
        msg = f"Error getting git status: {e}"
        raise ValueError(msg) from None
    except FileNotFoundError:
        msg = "Git executable not found. Make sure Git is installed and available in your system."
        raise ValueError(msg) from None


def has_changes() -> bool:
    """
    Check if there are unchecked changes in the Git repository.

    Returns:
        True if there are unchecked changes, False otherwise.

    Raises:
        ValueError: If there is an error checking for Git changes.
    """
    try:
        return len(get_status()) > 0
    except subprocess.CalledProcessError as e:
        msg = f"Error checking for changes: {e}"
        raise ValueError(msg) from None
    except FileNotFoundError:
        msg = "Git executable not found. Make sure Git is installed and available in your system."
        raise ValueError(msg) from None


def check_on_main_no_changes() -> None:
    if has_changes():
        msg = "All changes must be committed or removed before publishing"
        raise GitError(msg)
    branch = get_branch()
    if branch != "main":
        msg = f"Must be on 'main' branch. Currently on {branch!r} branch"
        raise GitError(msg)
