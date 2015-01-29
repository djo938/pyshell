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

import unittest
from pyshell.utils.parsing import Parser

class ParserTest(unittest.TestCase):
    def setUp(self):
        pass
    
    ####### ONE COMMAND ######

    def test_singleCommand1(self):
        p = Parser("abc def ghi")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) ])

    def test_singleCommand2(self):
        p = Parser("abc def ghi | ")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) ])

    def test_singleCommand3(self):
        p = Parser("abc def ghi | |")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) ])

    def test_singleCommand4(self):
        p = Parser("abc def ghi | ||")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) ])

    def test_singleCommand5(self):
        p = Parser("|abc def ghi")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) ])

    def test_singleCommand6(self):
        p = Parser("| |abc def ghi")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) ])

    def test_singleCommand7(self):
        p = Parser("||| abc def ghi ")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) ])

    #### TWO COMMAND ####
        
    def test_multipleCommand1(self):
        p = Parser("abc def ghi | jkl mno pqr")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) , ( ('jkl', 'mno', 'pqr'),(),(),) ])

    def test_multipleCommand2(self):
        p = Parser("| |abc def ghi | jkl mno pqr|")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) , ( ('jkl', 'mno', 'pqr'),(),(),) ])

    def test_multipleCommand3(self):
        p = Parser("abc def ghi | jkl mno pqr|")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) , ( ('jkl', 'mno', 'pqr'),(),(),) ])

    def test_multipleCommand4(self):
        p = Parser("abc def ghi | jkl mno pqr| |")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) , ( ('jkl', 'mno', 'pqr'),(),(),) ])

    def test_multipleCommand5(self):
        p = Parser("abc def ghi || jkl mno pqr")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) , ( ('jkl', 'mno', 'pqr'),(),(),) ])

    def test_multipleCommand6(self):
        p = Parser("abc def ghi | | | jkl mno pqr")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) , ( ('jkl', 'mno', 'pqr'),(),(),) ])

    def test_multipleCommand7(self):
        p = Parser("| abc def ghi | jkl mno pqr|")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) , ( ('jkl', 'mno', 'pqr'),(),(),) ])

    def test_multipleCommand8(self):
        p = Parser("||abc def ghi | jkl mno pqr| |")
        p.parse()
        self.assertEqual(p,[ ( ('abc', 'def', 'ghi'),(),(),) , ( ('jkl', 'mno', 'pqr'),(),(),) ])
        
    ##### THREE COMMAND ######
    def test_multipleCommand9(self):
        p = Parser("abc def ghi | jkl mno pqr | stu vwx yz")
        p.parse()
        self.assertEqual(p,[ (('abc', 'def', 'ghi'),(),(),), ( ('jkl', 'mno', 'pqr'),(),(),), ( ("stu","vwx","yz"),(),(),)])

    def test_multipleCommand10(self):
        p = Parser("|||abc def ghi |||| jkl mno pqr |||| stu vwx yz|||")
        p.parse()
        self.assertEqual(p,[ (('abc', 'def', 'ghi'),(),(),), ( ('jkl', 'mno', 'pqr'),(),(),), ( ("stu","vwx","yz"),(),(),)])

    def test_multipleCommand11(self):
        p = Parser("abc def ghi ||| jkl mno pqr ||| stu vwx yz")
        p.parse()
        self.assertEqual(p,[ (('abc', 'def', 'ghi'),(),(),), ( ('jkl', 'mno', 'pqr'),(),(),), ( ("stu","vwx","yz"),(),(),)])

    def test_multipleCommand12(self):
        p = Parser("||||abc def ghi | jkl mno pqr | stu vwx yz")
        p.parse()
        self.assertEqual(p,[ (('abc', 'def', 'ghi'),(),(),), ( ('jkl', 'mno', 'pqr'),(),(),), ( ("stu","vwx","yz"),(),(),)])

    def test_multipleCommand13(self):
        p = Parser("abc def ghi | jkl mno pqr | stu vwx yz|||")
        p.parse()
        self.assertEqual(p,[ (('abc', 'def', 'ghi'),(),(),), ( ('jkl', 'mno', 'pqr'),(),(),), ( ("stu","vwx","yz"),(),(),)])

    def test_multipleCommand14(self):
        p = Parser("abc def ghi | jkl mno pqr |||| stu vwx yz")
        p.parse()
        self.assertEqual(p,[ (('abc', 'def', 'ghi'),(),(),), ( ('jkl', 'mno', 'pqr'),(),(),), ( ("stu","vwx","yz"),(),(),)])

    def test_multipleCommand15(self):
        p = Parser("abc def ghi |||| jkl mno pqr | stu vwx yz")
        p.parse()
        self.assertEqual(p,[ (('abc', 'def', 'ghi'),(),(),), ( ('jkl', 'mno', 'pqr'),(),(),), ( ("stu","vwx","yz"),(),(),)])

    def test_multipleCommand16(self):
        p = Parser("|||abc def ghi | jkl mno pqr | stu vwx yz|")
        p.parse()
        self.assertEqual(p,[ (('abc', 'def', 'ghi'),(),(),), ( ('jkl', 'mno', 'pqr'),(),(),), ( ("stu","vwx","yz"),(),(),)])

    def test_multipleCommand17(self):
        p = Parser("|abc def ghi | jkl mno pqr | stu vwx yz|")
        p.parse()
        self.assertEqual(p,[ (('abc', 'def', 'ghi'),(),(),), ( ('jkl', 'mno', 'pqr'),(),(),), ( ("stu","vwx","yz"),(),(),)])

    ##### WRAPPED AREA #######
    def test_wrapped1(self):
        p = Parser("aa \"$ | \"")
        p.parse()
        self.assertEqual(p,[ (('aa','$ | ',),(),(),) ])
        
    def test_wrapped2(self):
        p = Parser("aa\"$ | \"")
        p.parse()
        self.assertEqual(p,[ (('aa$ | ',),(),(),) ])
        
    def test_wrapped3(self):
        p = Parser("aa\\\"$ | \"")
        p.parse()
        self.assertEqual(p,[(('aa"$',),(),(),)])
        
    def test_wrapped4(self):
        p = Parser("aa\"$ | \"bb")
        p.parse()
        self.assertEqual(p,[(('aa$ | bb',),(),(),)])

    ##### ESCAPE CHAR ########
    def test_escape1(self):
        p = Parser("a\|")
        p.parse()
        self.assertEqual(p,[( ('a|',),(),(),)])

    def test_escape2(self):
        p = Parser("a\|bc\de\\\\ plip| plop")
        p.parse()
        self.assertEqual(p,[(('a|bcde\\','plip',),(),(),),(('plop',),(),(),)])
    
    #### VAR CHAR ####

    #echo $\a
    def test_var1(self):
        p = Parser("aa bb cc $\\d")
        p.parse()
        self.assertEqual(p,[(('aa','bb','cc','$d',),(3,),(),)])

    #echo $a
    def test_var2(self):
        p = Parser("aa bb cc $d")
        p.parse()
        self.assertEqual(p,[(('aa','bb','cc','$d',),(3,),(),)])

    #echo "$\a"
        #$\a
    def test_var3(self):
        p = Parser("aa bb cc \"$\\d\"")
        p.parse()
        self.assertEqual(p,[(('aa','bb','cc','$d',),(3,),(),)])

    #echo "$a"
    def test_var4(self):
        p = Parser("aa bb cc \"$d\"")
        p.parse()
        self.assertEqual(p,[(('aa','bb','cc','$d',),(3,),(),)])
        
    def test_var5(self):
        p = Parser("aa bb cc \"$ d\"")
        p.parse()
        self.assertEqual(p,[(('aa','bb','cc','$ d',),(),(),)])
        
    def test_var6(self):
        p = Parser("aa bb cc $\\ d")
        p.parse()
        self.assertEqual(p,[(('aa','bb','cc','$ d',),(),(),)])
        
    def test_var7(self):
        p = Parser("aa bb cc \"$\"")
        p.parse()
        self.assertEqual(p,[(('aa','bb','cc','$',),(),(),)])
        
    def test_var8(self):
        p = Parser("aa bb cc $")
        p.parse()
        self.assertEqual(p,[(('aa','bb','cc','$',),(),(),)])   
             
    #TODO test parameter spotting
    #TODO test background

if __name__ == '__main__':
    unittest.main()