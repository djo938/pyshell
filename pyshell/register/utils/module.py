#!/usr/bin/env python -t
# -*- coding: utf-8 -*-

# Copyright (C) 2014  Jonathan Delvaux <pyshell@djoproject.net>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import inspect

from pyshell.register.exception import LoaderException


def getNearestModule():
    nearest_frame = None
    for record in inspect.stack():
        frame, path, line_number, parent_stmp, line_string, unknown = record
        if parent_stmp == "<module>":
            nearest_frame = frame
            break

    if nearest_frame is None:
        # there is no way to test this statement
        excmsg = "(module) getNearestModule, fail to find the nearest frame"
        raise LoaderException(excmsg)

    mod = inspect.getmodule(nearest_frame)
    return mod
