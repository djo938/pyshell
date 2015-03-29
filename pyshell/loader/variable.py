#!/usr/bin/python
# -*- coding: utf-8 -*-

#Copyright (C) 2015  Jonathan Delvaux <pyshell@djoproject.net>

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pyshell.loader.parameter import registerAddValues, registerSet, ParameterAbstractLoader
from pyshell.system.variable  import VarParameter
from pyshell.utils.constants  import VARIABLE_ATTRIBUTE_NAME

def registerAddValuesToVariable(contextKey, value, subLoaderName = None):
    registerAddValues(envKey, value, VariableLoader, subLoaderName)

def registerSetVariable(contextKey, context, noErrorIfKeyExist = False, override = False, subLoaderName = None):
	registerSet(key, obj, VariableLoader, VarParameter, noErrorIfKeyExist, override, subLoaderName)
	
class VariableLoader(ParameterAbstractLoader):
    def __init__(self):
        ParameterAbstractLoader.__init__(self, VARIABLE_ATTRIBUTE_NAME)