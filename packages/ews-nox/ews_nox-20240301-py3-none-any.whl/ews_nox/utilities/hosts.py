from __future__ import annotations

import os
import socket
from functools import wraps
from urllib.error import URLError
from urllib.request import urlopen

from nox import Session


def get_hostname() -> str:
    """Get the hostname"""
    return socket.gethostname().upper()


def is_remote_host_online(
    host_name,
    port: int = 0,
    extra: str = "",
    session: Session = None,
    timeout: int = 1,
    ssl: bool = False,
) -> bool:
    extra = extra.strip()
    addr = f"{host_name}:{port:d}" if port > 0 else host_name
    prefix = "http" if not ssl else "https"
    url = f"{prefix}://{addr}{extra}"
    if session is not None:
        session.log(f"Testing {url!r}")
    try:
        urlopen(url, timeout=timeout)  # noqa: S310
        return True
    except URLError:
        pass
    return False


def get_is_connected_to_internet(url: str = "google.com", ssl: bool = True, timeout: int = 1) -> bool:
    return is_remote_host_online(url, ssl=True, timeout=timeout)


def is_session_offline(session: Session, warn: bool = True):
    is_offline = False
    is_offline = True if "--offline" in session.posargs else os.getenv("OFFLINE", "0").upper() in ["YES", "1", "TRUE"]
    if is_offline and warn:
        session.warn("Working offline")

    return is_offline


def add_offline_posargs_if_necessary(**kwargs):
    is_online = kwargs.pop("is_online", None)
    if is_online is None:
        is_online = get_is_connected_to_internet()

    dev_offline = os.getenv("DEV_OFFLINE", "0").upper() in ["YES", "1", "TRUE"]
    is_online = is_online and not dev_offline

    def outter_func(func):
        @wraps(func)
        def new_func(*args, **kwargs):
            if args and isinstance(args[0], Session):
                if not is_online:
                    args[0].posargs.append("--offline")
                else:
                    args[0].posargs.append("--online")

            return func(*args, **kwargs)

        return new_func

    return outter_func
