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

import logging as lggg
from pathlib import Path as path_t
from typing import TextIO

from rich.console import Console as console_t

from logger_36.instance import LOGGER


def SaveLOGasHTML(path: str | path_t | TextIO = None) -> None:
    """
    From first console handler found.
    """
    cannot_save = "Cannot save logging record as HTML"

    if path is None:
        for handler in LOGGER.handlers:
            if isinstance(handler, lggg.FileHandler):
                path = path_t(handler.baseFilename).with_suffix(".htm")
                break
        if path is None:
            LOGGER.warning(f"{cannot_save}: No file handler to build a filename from.")
            return
        if path.exists():
            LOGGER.warning(
                f'{cannot_save}: Automatically generated path "{path}" already exists.'
            )
            return
    elif isinstance(path, str):
        path = path_t(path)

    actual_file = isinstance(path, path_t)
    if actual_file and path.exists():
        LOGGER.warning(f'{cannot_save}: File "{path}" already exists.')
        return

    console = None
    found = False
    for handler in LOGGER.handlers:
        console = getattr(handler, "console", None)
        if found := isinstance(console, console_t):
            break

    if found:
        html = console.export_html()
        if actual_file:
            with open(path, "w") as accessor:
                accessor.write(html)
        else:
            path.write(html)
    else:
        LOGGER.warning(f"{cannot_save}: No handler has a RICH console.")
