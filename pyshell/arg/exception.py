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

from pyshell.utils.exception import ERROR
from pyshell.utils.exception import PyshellException
from pyshell.utils.exception import USER_ERROR


class ArgException(PyshellException):
    def __init__(self, value, usage=""):
        PyshellException.__init__(self, USER_ERROR)
        self.value = value
        self.usage = usage

    def __str__(self):
        return str(self.value)


class ArgInitializationException(PyshellException):
    def __init__(self, value):
        PyshellException.__init__(self, ERROR)
        self.value = value

    def __str__(self):
        return str(self.value)


class DecoratorException(PyshellException):
    def __init__(self, value):
        PyshellException.__init__(self, ERROR)
        self.value = value

    def __str__(self):
        return str(self.value)
