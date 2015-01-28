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

from pyshell.utils.exception   import DefaultPyshellException, PARSE_ERROR

#BNF GRAMMAR OF A COMMAND
# 
## RULE 1 ## <commands>  ::= <command> <threading> <EOL> | <command> "|" <commands>
## RULE 2 ## <threading> ::= " &" | ""
## RULE 3 ## <command>   ::= <token> | <token> " " <command>
## RULE 4 ## <token>     ::= <string> | "$" <string> | "\$" <string> | "-" <text> | "-" <text> <string> | "\-" <string>
## RULE 5 ## <string>    ::= <text> | <text> "\ " <string> #TODO conflict with command rule
#
#

#TODO
    #TODO create a simple parser be able to parse a list of string
        #no parsing to do, just prepare the output
        #create an abstract parser class

    #finish to refactor addons/alias.py
    #finish to refactor utils/alias.py

    #finish the grammar then refactor the parsing system

    #keep track of running event and be able to kill one or all of them
        #manage it in alias object with a static list
            #an alias add itself in the list before to start then remove itself from the list at the end of its execution
            
    #create an addon "background" to
        #fire a command on background
            #like the '&' but the parsing of the command occur later
        #kill a command on background with an id
            #hard kill
            #light kill (stop on next command)
        #list all command executing on background

class Parser(list):
    "This object will parse a command line withou any resolution of process, argument, or parameter"
    
    #TODO
        #be able to escape '&'
    
    def __init__(self,string):
        
        if type(string) != str and type(string) != unicode:
            raise DefaultPyshellException("fail to init parser object, a string was expected, got '"+str(type(string))+"'",PARSE_ERROR)
    
        list.__init__(self)
        self.currentToken    = None
        self.currentCommand  = []
        self.argSpotted      = []
        self.paramSpotted    = []
        self._innerParser    = self._parse
        self.string          = string
        self.escapeChar      = False
        self.runInBackground = False
        self.isParsed        = False
        self.wrapped         = False

    def _pushCommandInList(self):
        if len(self.currentCommand) > 0:
            self.append(  (tuple(self.currentCommand),tuple(self.argSpotted),tuple(self.paramSpotted),)  )
            del self.currentCommand[:]
            del self.argSpotted[:]
            del self.paramSpotted[:]
    
    def _pushTokenInCommand(self):
        if self.currentToken is not None:
            if len(self.currentToken) > 0:
                self.currentCommand.append(self.currentToken)
            
                index = len(self.currentCommand) -1

                if index in self.argSpotted and (' ' in self.currentToken or len(self.currentToken) == 1):
                    self.argSpotted.remove(index)

                elif index in self.paramSpotted:
                    if (' ' in self.currentToken or len(self.currentToken) == 1):
                        self.paramSpotted.remove(index)
                    else:
                        try:
                            float(self.currentToken)
                            self.paramSpotted.remove(index)
                        except ValueError:
                            pass
            
            self.currentToken = None
            self.wrapped = False

    def _parse(self,char):
        if self.currentToken is None:
            if char in (' ','\t','\n','\r',):
                return
                
            if char == '|':
                self._pushCommandInList()
                return
                
            self.currentToken = ""

        if self.escapeChar:
            self.currentToken += char
            self.escapeChar    = False

        elif char == '\\':
            self.escapeChar    = True
        elif char == '"':
            self.wrapped = not self.wrapped
        elif not self.wrapped and char in (' ','|','\t','\n','\r',):
            self._pushTokenInCommand()
                
            if char == '|':
                self._pushCommandInList()
        elif char == '$' and len(self.currentToken) == 0:
            self.argSpotted.append(len(self.currentCommand))
            self.currentToken += char
        elif char == '-' and len(self.currentToken) == 0:
            self.paramSpotted.append(len(self.currentCommand))
            self.currentToken += char
        else:
            self.currentToken += char

    def parse(self):
        del self[:]
    
        self.string = self.string.strip(' \t\n\r')
        
        if len(self.string) == 0:
            return
                
        for i in xrange(0,len(self.string)):
            char = self.string[i]
            self._parse(char)    
            
        #push intermediate data
        self._pushTokenInCommand()
        self._pushCommandInList()
        
        #compute runInBackground
        if len(self) > 0:
            if self[-1][0][-1] == '&':
                self.runInBackground = True
                del self[-1][0][-1]
            elif self[-1][0][-1][-1] == '&':
                self.runInBackground = True
                self[-1][0][-1] = self[-1][0][-1][:-1]
                
        self.isParsed = True
            
    def isToRunInBackground(self):
        return self.runInBackground
        
    def isParsed(self):
        return 



