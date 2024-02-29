# Copyright CNRS/Inria/UCA
# Contributor(s): Eric Debreuve (since 2023)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

"""
Alternative implementations: using logging.Filter or logging.LoggerAdapter.
"""
import logging as lggg
from pathlib import Path as path_t
from typing import Callable, Literal

from logger_36.instance import LOGGER
from logger_36.type.console import console_handler_t
from logger_36.type.file import file_handler_t
from logger_36.type.generic import can_show_message_p, generic_handler_t


def AddGenericHandler(
    interface: can_show_message_p | Callable[[str], None],
    /,
    *args,
    level: int = lggg.INFO,
    supports_html: bool = False,
    **kwargs,
) -> None:
    """"""
    handler = generic_handler_t(interface, *args, supports_html=supports_html, **kwargs)
    handler.setLevel(level)
    LOGGER.addHandler(handler)


def AddFileHandler(
    path: str | path_t, /, *args, level: int = lggg.INFO, **kwargs
) -> None:
    """"""
    if isinstance(path, str):
        path = path_t(path)
    if path.exists():
        raise ValueError(f"{path}: File already exists")

    handler = file_handler_t(path, *args, **kwargs)
    handler.setLevel(level)
    LOGGER.addHandler(handler)


def SetLOGLevel(level: int, /, *, which: Literal["c", "f", "a"] = "a") -> None:
    """
    which: c=console, f=file, a=all
    """
    if which not in "cfa":
        raise ValueError(
            f"{which}: Invalid handler specifier. "
            f'Expected="c" for console, "f" for file, or "a" for all'
        )

    for handler in LOGGER.handlers:
        if (
            (which == "a")
            or ((which == "c") and isinstance(handler, console_handler_t))
            or ((which == "f") and isinstance(handler, file_handler_t))
        ):
            handler.setLevel(level)


def SetExitOnError(exit_on_error: bool, /) -> None:
    """"""
    for handler in LOGGER.handlers:
        if hasattr(handler, "exit_on_error"):
            handler.exit_on_error = exit_on_error
