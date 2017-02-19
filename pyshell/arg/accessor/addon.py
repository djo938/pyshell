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

from pyshell.arg.accessor.container import ContainerAccessor

TYPENAME = "addon"


class AddonAccessor(ContainerAccessor):
    def hasAccessorValue(self):
        if not ContainerAccessor.hasAccessorValue(self):
            return False

        container = ContainerAccessor.getAccessorValue(self)

        return container.getAddonManager() is not None

    def getAccessorValue(self):
        return ContainerAccessor.getAccessorValue(self).getAddonManager()

    def buildErrorMessage(self):
        if not ContainerAccessor.hasAccessorValue(self):
            return ContainerAccessor.buildErrorMessage(self)
        return "container provided has no addon list defined"

    @classmethod
    def getTypeName(cls):
        return TYPENAME
