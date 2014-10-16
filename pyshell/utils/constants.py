#!/usr/bin/python
# -*- coding: utf-8 -*-

#Copyright (C) 2014  Jonathan Delvaux <pyshell@djoproject,net>

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

import os

KEYSTORE_SECTION_NAME  = "keystore"
DEFAULT_KEYSTORE_FILE  = os.path.join(os.path.expanduser("~"), ".pyshell_keystore")

CONTEXT_NAME           = "context"
ENVIRONMENT_NAME       = "environment"
DEFAULT_PARAMETER_FILE = os.path.join(os.path.expanduser("~"), ".pyshellrc")
MAIN_CATEGORY          = "main"
PARAMETER_NAME         = "parameter"
DEFAULT_SEPARATOR      = ","
ADDONLIST_KEY          = "loader_addon"
DEFAULT_SUBADDON_NAME  = "default"