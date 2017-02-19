#!/usr/bin/env python -t
# -*- coding: utf-8 -*-

# Copyright (C) 2017  Jonathan Delvaux <pyshell@djoproject.net>

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

from pyshell.arg.accessor.parameter import AbstractParameterAccessor
from pyshell.arg.accessor.parameter import AbstractParameterDynamicAccessor
from pyshell.utils.constants import ENVIRONMENT_ATTRIBUTE_NAME

DYNAMIC_ACCESSOR_TYPENAME = "environment dynamic"
ACCESSOR_TYPENAME = "environment"


class EnvironmentAccessor(AbstractParameterAccessor):
    def __init__(self, environment_string_path):
        AbstractParameterAccessor.__init__(self,
                                           environment_string_path,
                                           ENVIRONMENT_ATTRIBUTE_NAME)

    def getManager(self, container):
        return container.getEnvironmentManager()

    @classmethod
    def getTypeName(cls):
        return ACCESSOR_TYPENAME


class EnvironmentDynamicAccessor(AbstractParameterDynamicAccessor):
    def __init__(self):
        AbstractParameterDynamicAccessor.__init__(self,
                                                  ENVIRONMENT_ATTRIBUTE_NAME)

    def getManager(self, container):
        return container.getEnvironmentManager()

    @classmethod
    def getTypeName(cls):
        return DYNAMIC_ACCESSOR_TYPENAME