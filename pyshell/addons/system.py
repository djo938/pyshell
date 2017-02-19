#!/usr/bin/env python -t
# -*- coding: utf-8 -*-

# Copyright (C) 2016  Jonathan Delvaux <pyshell@djoproject.net>

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

from tries import multiLevelTries

from pyshell.addons.utils.addon import tryToImportLoaderFromFile
from pyshell.arg.accessor.default import DefaultAccessor
from pyshell.arg.accessor.environment import EnvironmentAccessor
from pyshell.arg.checker.default import DefaultChecker
from pyshell.arg.checker.file import FilePathArgChecker
from pyshell.arg.checker.integer import IntegerArgChecker
from pyshell.arg.checker.list import ListArgChecker
from pyshell.arg.checker.string43 import StringArgChecker
from pyshell.arg.decorator import shellMethod
from pyshell.register.command import registerCommand
from pyshell.register.context import registerContext
from pyshell.register.environment import registerEnvironment
from pyshell.register.file import enableConfigSaving
from pyshell.system.parameter.context import ContextParameter
from pyshell.system.parameter.environment import EnvironmentParameter
from pyshell.system.setting.context import ContextGlobalSettings
from pyshell.system.setting.environment import EnvironmentGlobalSettings
from pyshell.utils.constants import CONTEXT_COLORATION_DARK
from pyshell.utils.constants import CONTEXT_COLORATION_KEY
from pyshell.utils.constants import CONTEXT_COLORATION_LIGHT
from pyshell.utils.constants import CONTEXT_COLORATION_NONE
from pyshell.utils.constants import CONTEXT_EXECUTION_DAEMON
from pyshell.utils.constants import CONTEXT_EXECUTION_KEY
from pyshell.utils.constants import CONTEXT_EXECUTION_SHELL
from pyshell.utils.constants import DEBUG_ENVIRONMENT_NAME
from pyshell.utils.constants import DEFAULT_CONFIG_DIRECTORY
from pyshell.utils.constants import ENVIRONMENT_ADDON_TO_LOAD_DEFAULT
from pyshell.utils.constants import ENVIRONMENT_ADDON_TO_LOAD_KEY
from pyshell.utils.constants import ENVIRONMENT_CONFIG_DIRECTORY_KEY
from pyshell.utils.constants import ENVIRONMENT_HISTORY_FILE_NAME_KEY
from pyshell.utils.constants import ENVIRONMENT_HISTORY_FILE_NAME_VALUE
from pyshell.utils.constants import ENVIRONMENT_LEVEL_TRIES_KEY
from pyshell.utils.constants import ENVIRONMENT_PROMPT_DEFAULT
from pyshell.utils.constants import ENVIRONMENT_PROMPT_KEY
from pyshell.utils.constants import ENVIRONMENT_SAVE_KEYS_DEFAULT
from pyshell.utils.constants import ENVIRONMENT_SAVE_KEYS_KEY
from pyshell.utils.constants import ENVIRONMENT_TAB_SIZE_KEY
from pyshell.utils.constants import ENVIRONMENT_USE_HISTORY_KEY
from pyshell.utils.constants import ENVIRONMENT_USE_HISTORY_VALUE
from pyshell.utils.constants import TAB_SIZE
from pyshell.utils.exception import ListOfException
from pyshell.utils.printing import error
from pyshell.utils.printing import notice


default_string_arg_checker = DefaultChecker.getString()
default_arg_checker = DefaultChecker.getArg()
default_boolean_arg_checker = DefaultChecker.getBoolean()
default_integer_arg_checker = DefaultChecker.getInteger()

# # init original params # #
checker = FilePathArgChecker(exist=None,
                             readable=True,
                             writtable=None,
                             is_file=False)

settings = EnvironmentGlobalSettings(transient=True,
                                     read_only=False,
                                     removable=False,
                                     checker=checker)

param = EnvironmentParameter(value=DEFAULT_CONFIG_DIRECTORY, settings=settings)
registerEnvironment(ENVIRONMENT_CONFIG_DIRECTORY_KEY, param)

##

settings = EnvironmentGlobalSettings(transient=False,
                                     read_only=False,
                                     removable=False,
                                     checker=default_string_arg_checker)

param = EnvironmentParameter(value=ENVIRONMENT_PROMPT_DEFAULT,
                             settings=settings)

registerEnvironment(ENVIRONMENT_PROMPT_KEY, param)

##

settings = EnvironmentGlobalSettings(transient=False,
                                     read_only=False,
                                     removable=False,
                                     checker=IntegerArgChecker(0))

param = EnvironmentParameter(value=TAB_SIZE, settings=settings)
registerEnvironment(ENVIRONMENT_TAB_SIZE_KEY, param)

##

param = EnvironmentParameter(
    value=multiLevelTries(),
    settings=EnvironmentGlobalSettings(transient=True,
                                       read_only=True,
                                       removable=False,
                                       checker=default_arg_checker))

registerEnvironment(ENVIRONMENT_LEVEL_TRIES_KEY, param)

##

settings = EnvironmentGlobalSettings(transient=False,
                                     read_only=False,
                                     removable=False,
                                     checker=default_boolean_arg_checker)

param = EnvironmentParameter(value=ENVIRONMENT_SAVE_KEYS_DEFAULT,
                             settings=settings)

registerEnvironment(ENVIRONMENT_SAVE_KEYS_KEY, param)

##

checker = FilePathArgChecker(exist=None,
                             readable=True,
                             writtable=None,
                             is_file=True)

settings = EnvironmentGlobalSettings(
    transient=False,
    read_only=False,
    removable=False,
    checker=checker)

param = EnvironmentParameter(value=ENVIRONMENT_HISTORY_FILE_NAME_VALUE,
                             settings=settings)

registerEnvironment(ENVIRONMENT_HISTORY_FILE_NAME_KEY, param)

##

settings = EnvironmentGlobalSettings(
    transient=False,
    read_only=False,
    removable=False,
    checker=default_boolean_arg_checker)

param = EnvironmentParameter(value=ENVIRONMENT_USE_HISTORY_VALUE,
                             settings=settings)

registerEnvironment(ENVIRONMENT_USE_HISTORY_KEY, param)

##

settings = EnvironmentGlobalSettings(
    transient=False,
    read_only=False,
    removable=False,
    checker=ListArgChecker(default_string_arg_checker))

param = EnvironmentParameter(value=ENVIRONMENT_ADDON_TO_LOAD_DEFAULT,
                             settings=settings)

registerEnvironment(ENVIRONMENT_ADDON_TO_LOAD_KEY, param)

##

settings = ContextGlobalSettings(removable=False,
                                 read_only=False,
                                 transient=False,
                                 transient_index=False,
                                 checker=default_integer_arg_checker)

param = ContextParameter(value=tuple(range(0, 5)), settings=settings)
settings.setDefaultIndex(0)
settings.setIndex(1)
settings.setReadOnly(True)

registerContext(DEBUG_ENVIRONMENT_NAME, param)

##

settings = ContextGlobalSettings(removable=False,
                                 read_only=False,
                                 transient=True,
                                 transient_index=True,
                                 checker=default_string_arg_checker)
values = (CONTEXT_EXECUTION_SHELL,
          CONTEXT_EXECUTION_DAEMON,)

param = ContextParameter(value=values, settings=settings)
settings.setDefaultIndex(0)
settings.setReadOnly(True)

registerContext(CONTEXT_EXECUTION_KEY, param)

##

settings = ContextGlobalSettings(removable=False,
                                 read_only=False,
                                 transient=False,
                                 transient_index=False,
                                 checker=default_string_arg_checker)

values = (CONTEXT_COLORATION_LIGHT,
          CONTEXT_COLORATION_DARK,
          CONTEXT_COLORATION_NONE,)

param = ContextParameter(value=values, settings=settings)
settings.setDefaultIndex(0)
settings.setReadOnly(True)

registerContext(CONTEXT_COLORATION_KEY, param)

##


@shellMethod(name=DefaultChecker.getString(),
             profile_name=StringArgChecker(),
             parameters=DefaultAccessor.getContainer())
def loadAddonFun(name, parameters, profile_name=None):
    "load an addon"

    addon_dico = parameters.getAddonManager()

    # is it already loaded ?
    if name in addon_dico:
        addon_loader = addon_dico[name]
        loaded_name = addon_loader.getInformations().getLoadedProfileName()

        # no loaded profile ?
        if loaded_name is not None:
            # TODO normalize profile_name (see register/utils/addon.py)
            if profile_name != loaded_name:
                # TODO improve the error message
                error("another profile name is already loaded")

            loaded_profile = addon_loader.getRootLoaderProfile(loaded_name)
            if loaded_profile.isLoaded():
                notice(name + " already loaded !")
                return
            elif loaded_profile.isLoading():
                notice(name + " already loading !")
    else:
        # load and register
        loader = tryToImportLoaderFromFile(name)
        addon_dico[name] = loader

    loader.load(container=parameters, profile_name=profile_name)
    notice(name + " loaded !")


@shellMethod(
    addon_list_on_start_up=EnvironmentAccessor(
        ENVIRONMENT_ADDON_TO_LOAD_KEY),
    params=DefaultAccessor.getContainer())
# TODO no profile_name argument ?
def loadAddonOnStartUp(addon_list_on_start_up, params):

    if addon_list_on_start_up is None:
        return
    addon_list = addon_list_on_start_up.getValue()

    error_list = ListOfException()
    for addon_name in addon_list:
        try:
            loadAddonFun(addon_name, params)
        except Exception as ex:
            # TODO the information about the failing addon is lost here...
            # E.G. if an addon is already loaded, only the profile name will be
            # printed, not the addon name...
            error_list.addException(ex)

    if error_list.isThrowable():
        raise error_list

registerCommand(("addon", "load",), pro=loadAddonFun)
registerCommand(("addon", "onstartup", "load",), pro=loadAddonOnStartUp)
enableConfigSaving()
