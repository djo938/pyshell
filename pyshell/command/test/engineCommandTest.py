#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from pyshell.command.exception import *
from pyshell.arg.decorator import shellMethod
from pyshell.arg.argchecker import ArgChecker
from pyshell.command.command import *
from pyshell.command.engine import *

@shellMethod(arg=ArgChecker()) 
def plop(arg):
    return arg
    
def noneFun():
    pass

class splitAndMergeTest(unittest.TestCase): 
    def setUp(self):
        self.mc = MultiCommand()
        self.mc.addProcess(noneFun,noneFun,noneFun)
        
        self.mc2 = MultiCommand()
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        
        self.e = engineV3([self.mc,self.mc2,self.mc2],[[],[],[]], [[{},{},{}],[{},{},{}],[{},{},{}]])

    #_willThisCmdBeCompletlyDisabled(self, cmdID, startSkipRange, rangeLength=1)
    def test_willThisCmdBeCompletlyDisabled(self):
        mc = MultiCommand()
        for i in range(0,6):
            mc.addProcess(noneFun,noneFun,noneFun)

        self.e = engineV3([mc],[[]], [[{},{},{}]])

        #must return False
            #empty before range, at least on item true in the after range

        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 0, 1))
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 0, 2))
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 0, 5))

            #not empty before range but no value set to true, at least on item true in the after range

        mc.disableCmd(0)
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 1, 1))
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 1, 2))
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 1, 4))

        mc.disableCmd(1)
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 2, 1))
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 2, 2))
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 2, 3))

            #empty after range, at least on item true in the before range

        mc.enableCmd(0)
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 4, 1))
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 3, 2))
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 2, 3))
            
            #range must have a size of 1 or more than 1
            #skip range must have a size of 0, 1 or more than 1

        #this test will explore every node
        mc.enableCmd(1)
        mc.disableCmd(5)
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 0, 0))
        self.assertFalse(self.e._willThisCmdBeCompletlyDisabled(0, 6, 0))
        
        mc.enableCmd(5)
        #mist return True
            #empty before and empty after range
        self.assertTrue(self.e._willThisCmdBeCompletlyDisabled(0, 0, 6))

            #empty before range and after range only set to False
        mc.disableCmd(5)
        mc.disableCmd(4)
        self.assertTrue(self.e._willThisCmdBeCompletlyDisabled(0, 0, 5))
        self.assertTrue(self.e._willThisCmdBeCompletlyDisabled(0, 0, 4))
        mc.enableCmd(5)
        mc.enableCmd(4)

            #before range not empty but only with false value, after range empty
        mc.disableCmd(0)
        mc.disableCmd(1)
        self.assertTrue(self.e._willThisCmdBeCompletlyDisabled(0, 1, 5))
        self.assertTrue(self.e._willThisCmdBeCompletlyDisabled(0, 2, 4))

            #before range not empty but only with false value, after range not empty but only with false value
        mc.disableCmd(5)
        mc.disableCmd(4)
        self.assertTrue(self.e._willThisCmdBeCompletlyDisabled(0, 1, 4))
        self.assertTrue(self.e._willThisCmdBeCompletlyDisabled(0, 1, 3))
        self.assertTrue(self.e._willThisCmdBeCompletlyDisabled(0, 2, 3))
        self.assertTrue(self.e._willThisCmdBeCompletlyDisabled(0, 2, 2))
            
            #range must have a size of 1 or more than 1
            #skip range must have a size of 0, 1 or more than 1
        
    #_willThisDataBunchBeCompletlyDisabled(self, dataIndex, startSkipRange, rangeLength=1)
    def test_willThisDataBunchBeCompletlyDisabled_NoneDatabunch(self):
        mc = MultiCommand()
        for i in range(0,6):
            mc.addProcess(noneFun,noneFun,noneFun)

        self.e = engineV3([mc],[[]], [[{},{},{}]])

        #must return False
            #empty before range, at least on item true in the after range

        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 5))

            #not empty before range but no value set to true, at least on item true in the after range

        mc.disableCmd(0)
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 4))

        mc.disableCmd(1)
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 3))

            #empty after range, at least on item true in the before range

        mc.enableCmd(0)
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 4, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 3, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 3))
            
            #range must have a size of 1 or more than 1
            #skip range must have a size of 0, 1 or more than 1

        #this test will explore every node
        mc.enableCmd(1)
        mc.disableCmd(5)
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 0))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 6, 0))
        
        mc.enableCmd(5)
        #mist return True
            #empty before and empty after range
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 6))

            #empty before range and after range only set to False
        mc.disableCmd(5)
        mc.disableCmd(4)
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 5))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 4))
        mc.enableCmd(5)
        mc.enableCmd(4)

            #before range not empty but only with false value, after range empty
        mc.disableCmd(0)
        mc.disableCmd(1)
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 5))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 4))

            #before range not empty but only with false value, after range not empty but only with false value
        mc.disableCmd(5)
        mc.disableCmd(4)
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 4))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 3))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 3))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 2))
            
            #range must have a size of 1 or more than 1
            #skip range must have a size of 0, 1 or more than 1

    def test_willThisDataBunchBeCompletlyDisabled_NotNoneDatabunch(self):
        mc = MultiCommand()
        for i in range(0,6):
            mc.addProcess(noneFun,noneFun,noneFun)

        self.e = engineV3([mc],[[]], [[{},{},{}]])
        self.e.stack.setEnableMapOnIndex(0,[True]*6)
        emap = self.e.stack.enablingMap(0)

        #must return False
            #empty before range, at least on item true in the after range

        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 5))

            #not empty before range but no value set to true, at least on item true in the after range

        emap[0] = False
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 4))

        emap[1] = False
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 3))

            #empty after range, at least on item true in the before range

        emap[0] = True
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 4, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 3, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 3))
            
            #range must have a size of 1 or more than 1
            #skip range must have a size of 0, 1 or more than 1

        #this test will explore every node
        emap[1] = True
        emap[5] = False
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 0))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyDisabled(0, 6, 0))
        
        emap[5] = True
        #mist return True
            #empty before and empty after range
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 6))

            #empty before range and after range only set to False
        emap[5] = False
        emap[4] = False
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 5))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 0, 4))
        emap[5] = True
        emap[4] = True

            #before range not empty but only with false value, after range empty
        emap[0] = False
        emap[1] = False
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 5))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 4))

            #before range not empty but only with false value, after range not empty but only with false value
        emap[5] = False
        emap[4] = False
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 4))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 1, 3))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 3))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyDisabled(0, 2, 2))
            
            #range must have a size of 1 or more than 1
            #skip range must have a size of 0, 1 or more than 1
        #same test as previous, but every cmd are enabled and enableMap keep the values, msut give the same results
    
    #_willThisDataBunchBeCompletlyEnabled(self, dataIndex, startSkipRange, rangeLength=1)
    def test_willThisDataBunchBeCompletlyEnabled(self):
        mc = MultiCommand()
        for i in range(0,6):
            mc.addProcess(noneFun,noneFun,noneFun)

        self.e = engineV3([mc],[[]], [[{},{},{}]])

        #map none
        self.assertTrue(self.e._willThisDataBunchBeCompletlyEnabled(0, 1, 3))

        self.e.stack.setEnableMapOnIndex(0,[False]*6)
        emap = self.e.stack.enablingMap(0)

        #must return False
            #empty before range, at least on item true in the after range

        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 0, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 0, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 0, 5))

            #not empty before range but no value set to true, at least on item true in the after range

        emap[0] = True
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 1, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 1, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 1, 4))

        emap[1] = True
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 2, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 2, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 2, 3))

            #empty after range, at least on item true in the before range

        emap[0] = False
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 4, 1))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 3, 2))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 2, 3))
            
            #range must have a size of 1 or more than 1
            #skip range must have a size of 0, 1 or more than 1

        #this test will explore every node
        emap[1] = False
        emap[5] = True
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 0, 0))
        self.assertFalse(self.e._willThisDataBunchBeCompletlyEnabled(0, 6, 0))
        
        emap[5] = False
        #mist return True
            #empty before and empty after range
        self.assertTrue(self.e._willThisDataBunchBeCompletlyEnabled(0, 0, 6))

            #empty before range and after range only set to False
        emap[5] = True
        emap[4] = True
        self.assertTrue(self.e._willThisDataBunchBeCompletlyEnabled(0, 0, 5))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyEnabled(0, 0, 4))
        emap[5] = False
        emap[4] = False

            #before range not empty but only with false value, after range empty
        emap[0] = True
        emap[1] = True
        self.assertTrue(self.e._willThisDataBunchBeCompletlyEnabled(0, 1, 5))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyEnabled(0, 2, 4))

            #before range not empty but only with false value, after range not empty but only with false value
        emap[5] = True
        emap[4] = True
        self.assertTrue(self.e._willThisDataBunchBeCompletlyEnabled(0, 1, 4))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyEnabled(0, 1, 3))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyEnabled(0, 2, 3))
        self.assertTrue(self.e._willThisDataBunchBeCompletlyEnabled(0, 2, 2))
    
    #_skipOnCmd(self,cmdID, subCmdID, skipCount = 1)
    def test_skipOnCmd(self):
        #FAILED
            #skip count < 1
        self.assertRaises(executionException,self.e._skipOnCmd,0,0,-10)

            #invalic cmd index
        self.assertRaises(executionException,self.e._skipOnCmd,25,0,1)

            #invalid sub cmd index
        self.assertRaises(executionException,self.e._skipOnCmd,0,25,1)

            #this will completly disable a entire cmd
        self.assertRaises(executionException,self.e._skipOnCmd,0,0,1)

            #this will disable compeltly a databunch at the current cmdID
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        del self.e.stack[:]
        self.e.stack.append(  (["a"], [0,0], PREPROCESS_INSTRUCTION, [True, False, False], )  )
        self.assertRaises(executionException,self.e._skipOnCmd,1,0,1)

            #this will disable compeltly a databunch at a different cmdID but with the same command
        del self.e.stack[:]
        self.e.stack.append(  (["a"], [0,0,0], PREPROCESS_INSTRUCTION, [True, False, False], )  )
        self.assertRaises(executionException,self.e._skipOnCmd,1,0,1)

        #SUCCESS
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)

        del self.e.stack[:]
        self.e._skipOnCmd(1,0,1)
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(0))
        for i in range(1,6):
            self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))

        self.e._skipOnCmd(1,0,2)
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(0))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(1))
        for i in range(2,6):
            self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))

        self.e._skipOnCmd(1,4,1)
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(0))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(1))
        for i in range(2,4):
            self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(4))
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(5))

        self.e._skipOnCmd(1,4,2)
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(0))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(1))
        for i in range(2,4):
            self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(4))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(5))

        self.e._skipOnCmd(1,2,1)
        for i in range(2,4):
            if i == 3:
                self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))
                continue
            self.assertTrue(self.e.cmdList[1].isdisabledCmd(i))

        self.assertRaises(executionException,self.e._skipOnCmd,1,2,2)

        for i in range(0,6):
            self.e.cmdList[1].enableCmd(i)

        del self.e.stack[:]
        self.e.stack.append(  (["a"], [0,0], PREPROCESS_INSTRUCTION, [True, True, True, False, False, False], )  )

        self.e._skipOnCmd(1,0,1)
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(0))
        for i in range(1,6):
            self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))

        self.e._skipOnCmd(1,0,2)
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(0))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(1))
        for i in range(2,6):
            self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))

        self.assertRaises(executionException,self.e._skipOnCmd,1,2,1)

        del self.e.stack[:]
        self.e.stack.append(  (["a"], [0,0], PREPROCESS_INSTRUCTION, [False, False, True, True, True, True], )  )

        self.e._skipOnCmd(1,4,1)
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(0))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(1))
        for i in range(2,4):
            self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(4))
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(5))

        self.e._skipOnCmd(1,4,2)
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(0))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(1))
        for i in range(2,4):
            self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(4))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(5))

        self.e._skipOnCmd(1,2,1)
        for i in range(0,6):
            if i == 3:
                self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))
                continue
            self.assertTrue(self.e.cmdList[1].isdisabledCmd(i))

        self.assertRaises(executionException,self.e._skipOnCmd,1,2,2)

            #disable range
                #at the biggining
                #at the end
                #in the middle
            #range of length 1 or more than 1
            #with empty stack or not
            #with pre/post/pro process on the stack
            #switch to False some already false, or not

    #_enableOnCmd(self, cmdID, subCmdID, enableCount = 1)
    def test_enableOnCmd(self):
        #FAILED
            #skip count < 1
        self.assertRaises(executionException,self.e._enableOnCmd,0,0,-10)

            #invalic cmd index
        self.assertRaises(executionException,self.e._enableOnCmd,25,0,1)

            #invalid sub cmd index
        self.assertRaises(executionException,self.e._enableOnCmd,0,25,1)
            
        #SUCCESS
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)

        for i in range(0,6):
            self.e.cmdList[1].disableCmd(i)

        self.e._enableOnCmd(1,0,1)
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(0))
        for i in range(1,6):
            self.assertTrue(self.e.cmdList[1].isdisabledCmd(i))

        self.e._enableOnCmd(1,0,2)
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(0))
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(1))
        for i in range(2,6):
            self.assertTrue(self.e.cmdList[1].isdisabledCmd(i))

        self.e._enableOnCmd(1,4,1)
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(0))
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(1))
        for i in range(2,4):
            self.assertTrue(self.e.cmdList[1].isdisabledCmd(i))
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(4))
        self.assertTrue(self.e.cmdList[1].isdisabledCmd(5))

        self.e._enableOnCmd(1,4,2)
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(0))
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(1))
        for i in range(2,4):
            self.assertTrue(self.e.cmdList[1].isdisabledCmd(i))
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(4))
        self.assertFalse(self.e.cmdList[1].isdisabledCmd(5))

        self.e._enableOnCmd(1,2,1)
        for i in range(2,4):
            if i == 3:
                self.assertTrue(self.e.cmdList[1].isdisabledCmd(i))
                continue
            self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))

        self.e._enableOnCmd(1,2,2)
        for i in range(0,6):
            self.assertFalse(self.e.cmdList[1].isdisabledCmd(i))

            #enable range
                #at the biggining
                #at the end
                #in the middle
            #range of length 1 or more than 1
            #switch to true some already true, or not
    
    #_skipOnDataBunch(self, dataBunchIndex, subCmdID, skipCount = 1)
    def test_skipOnDataBunch(self):
        #FAILED
            #skip count < 1
        self.assertRaises(executionException, self.e._skipOnDataBunch,0,0,-8000)
            
            #empty stack
        del self.e.stack[:]
        self.assertRaises(executionException, self.e._skipOnDataBunch,0,0,1)

            #invalic dataBunchIndex index
        self.e.stack.append(  (["a"], [0], PREPROCESS_INSTRUCTION, None, ) )
        self.assertRaises(executionException, self.e._skipOnDataBunch,43,0,1)

            #invalid sub cmd index
        self.assertRaises(executionException, self.e._skipOnDataBunch,0,123,1)

            #not a preprocess
        del self.e.stack[:]
        self.e.stack.append(  (["a"], [0], PROCESS_INSTRUCTION, None, ) )
        self.assertRaises(executionException, self.e._skipOnDataBunch,0,0,1)

            #will be completly disabled
        del self.e.stack[:]
        self.e.stack.append(  (["a"], [0,0], PREPROCESS_INSTRUCTION, None, ) )
        self.assertRaises(executionException, self.e._skipOnDataBunch,0,0,1000)

        #SUCCESS
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)

        self.e._skipOnDataBunch(0,0,1)
        emap = self.e.stack.enablingMapOnIndex(0)
        self.assertFalse(emap[0])
        for i in range(1,6):
            self.assertTrue(emap[i])

        self.e._skipOnDataBunch(0,0,2)
        emap = self.e.stack.enablingMapOnIndex(0)
        self.assertFalse(emap[0])
        self.assertFalse(emap[1])
        for i in range(2,6):
            self.assertTrue(emap[i])

        self.e._skipOnDataBunch(0,4,1)
        emap = self.e.stack.enablingMapOnIndex(0)
        self.assertFalse(emap[0])
        self.assertFalse(emap[1])
        for i in range(2,4):
            self.assertTrue(emap[i])
        self.assertFalse(emap[4])
        self.assertTrue(emap[5])

        self.e._skipOnDataBunch(0,4,2)
        self.assertFalse(emap[0])
        self.assertFalse(emap[1])
        for i in range(2,4):
            self.assertTrue(emap[i])
        self.assertFalse(emap[4])
        self.assertFalse(emap[5])

        self.e._skipOnDataBunch(0,2,1)
        for i in range(2,4):
            if i == 3:
                self.assertTrue(emap[i])
                continue
            self.assertFalse(emap[i])

        self.assertRaises(executionException,self.e._skipOnDataBunch,0,2,2)

    #_enableOnDataBunch(self, dataBunchIndex, subCmdID, enableCount = 1)
    def test_enableOnDataBunch(self):
        #FAILED
            #skip count < 1
        self.assertRaises(executionException, self.e._enableOnDataBunch,0,0,-8000)

            #empty stack
        del self.e.stack[:]
        self.assertRaises(executionException, self.e._enableOnDataBunch,0,0,1)

            #invalic dataBunchIndex index
        self.e.stack.append(  (["a"], [0], PREPROCESS_INSTRUCTION, None, ) )
        self.assertRaises(executionException, self.e._enableOnDataBunch,43,0,1)

            #invalid sub cmd index
        self.assertRaises(executionException, self.e._enableOnDataBunch,0,123,1)

            #not a preprocess
        del self.e.stack[:]
        self.e.stack.append(  (["a"], [0], PROCESS_INSTRUCTION, None, ) )
        self.assertRaises(executionException, self.e._enableOnDataBunch,0,0,1)
            
        #SUCCESS
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)
        self.mc2.addProcess(noneFun,noneFun,noneFun)

            #totaly reenabled a databunch
                #original map was None, or not
        del self.e.stack[:]
        self.e.stack.append(  (["a"], [0,0], PREPROCESS_INSTRUCTION, [False, False, False, False, False, False], ) )

        self.e._enableOnDataBunch(0,0,1)
        emap = self.e.stack.enablingMapOnIndex(0)
        self.assertTrue(emap[0])
        for i in range(1,6):
            self.assertFalse(emap[i])

        self.e._enableOnDataBunch(0,0,2)
        self.assertTrue(emap[0])
        self.assertTrue(emap[1])
        for i in range(2,6):
            self.assertFalse(emap[i])

        self.e._enableOnDataBunch(0,4,1)
        self.assertTrue(emap[0])
        self.assertTrue(emap[1])
        for i in range(2,4):
            self.assertFalse(emap[i])
        self.assertTrue(emap[4])
        self.assertFalse(emap[5])

        self.e._enableOnDataBunch(0,4,2)
        self.assertTrue(emap[0])
        self.assertTrue(emap[1])
        for i in range(2,4):
            self.assertFalse(emap[i])
        self.assertTrue(emap[4])
        self.assertTrue(emap[5])

        self.e._enableOnDataBunch(0,2,1)
        for i in range(2,4):
            if i == 3:
                self.assertFalse(emap[i])
                continue

            self.assertTrue(emap[i])

        self.e._enableOnDataBunch(0,2,2)
        self.assertIs(self.e.stack.enablingMapOnIndex(0), None)

            #enable range
                #at the biggining
                #at the end
                #in the middle
            #range of length 1 or more than 1
            #enablingMap is none, or not
            #switch to True some already True, or not
 
    #skipNextSubCommandOnTheCurrentData(self, skipCount=1):
    def test_skipNextSubCommandOnTheCurrentData(self):
        #FAILED
            #invalid skip count
        self.assertRaises( executionException, self.e.skipNextSubCommandOnTheCurrentData,-234)

            #empty stack
        del self.e.stack[:]
        self.assertRaises( executionException, self.e.skipNextSubCommandOnTheCurrentData,1)

            #not pre at top
        self.e.stack.append(  (["a"], [0], PROCESS_INSTRUCTION, None, ) )
        self.assertRaises( executionException, self.e.skipNextSubCommandOnTheCurrentData,1)
            
        #SUCCESS
            #add random skip count and check
        del self.e.stack[:]
        self.e.stack.append(  (["a"], [0], PREPROCESS_INSTRUCTION, None, ) )
        self.e.skipNextSubCommandOnTheCurrentData(100)
        self.assertIs(self.e.stack.subCmdIndexOnIndex(0), 100)

    #skipNextSubCommandForTheEntireDataBunch(self, skipCount=1):
    def test_skipNextSubCommandForTheEntireDataBunch(self):
        #FAILED
            #empty stack
        del self.e.stack[:]
        self.assertRaises( executionException, self.e.skipNextSubCommandForTheEntireDataBunch,1)

        #SUCCESS
            #no test to do

    #skipNextSubCommandForTheEntireExecution(self, skipCount=1):
    def test_skipNextSubCommandForTheEntireExecution(self):
        #FAILED
            #empty stack
        del self.e.stack[:]
        self.assertRaises( executionException, self.e.skipNextSubCommandForTheEntireExecution,1)

            #no preprocess at top
        self.e.stack.append(  (["a"], [0], PROCESS_INSTRUCTION, None, ) )
        self.assertRaises( executionException, self.e.skipNextSubCommandForTheEntireExecution,1)

        #SUCCESS
            #no test to do

    #disableEnablingMapOnDataBunch(self,index=0):
    def test_disableEnablingMapOnDataBunch(self):
        #FAILED
            #invalid index stack
        self.assertRaises( executionException, self.e.disableEnablingMapOnDataBunch,8000)

            #not pre at index
        self.e.stack.append(  (["a"], [0], PROCESS_INSTRUCTION, None, ) )
        self.assertRaises( executionException, self.e.disableEnablingMapOnDataBunch,-1)

        #SUCCESS
        self.e.stack.append(  (["a"], [0], PREPROCESS_INSTRUCTION, [True], ) )
        self.e.disableEnablingMapOnDataBunch(-1)
        self.assertIs(self.e.stack.enablingMapOnIndex(-1), None)
            #valid disabling
                #where already none
                #where not
        self.e.stack.append(  (["a"], [0], PREPROCESS_INSTRUCTION, None, ) )
        self.e.disableEnablingMapOnDataBunch(-1)
        self.assertIs(self.e.stack.enablingMapOnIndex(-1), None)

    #flushArgs(self, index=None)
    def test_flushArgs(self):
        #FAILED
            #None index and empty stack
        del self.e.stack[:]
        self.assertRaises(executionException, self.e.flushArgs)
        
            #invalid index
        self.assertRaises(executionException, self.e.flushArgs, -8000)
        self.assertRaises(executionException, self.e.flushArgs, 123)
        
        #SUCCESS
            #valid index
        self.e.argsList[0].append("toto")
        self.e.argsList[1].append("tata")
        
        self.e.flushArgs(1)
        self.assertEqual(self.e.argsList[0],["toto"])
        self.assertEqual(self.e.argsList[1],None)

    #addSubCommand(self, cmd, cmdID = None, onlyAddOnce = True, useArgs = True)
    def test_addSubCommand(self):
        #FAILED
            #invalid sub cmd instance
        self.assertRaises(executionException, self.e.addSubCommand, None)
        self.assertRaises(executionException, self.e.addSubCommand, "toto")
        self.assertRaises(executionException, self.e.addSubCommand, 52)
        
            #cmdID is None, and empty stack
        del self.e.stack[:]
        self.assertRaises(executionException, self.e.addSubCommand,Command())
        
            #invalid cmd index
        self.assertRaises(executionException, self.e.addSubCommand,Command(), -8000)
        self.assertRaises(executionException, self.e.addSubCommand,Command(), 123)
            
        #SUCCESS
            #with empty stack
        self.e.addSubCommand(Command(), 1)  
        self.assertEqual(len(self.e.cmdList[1]), 2)
        
            #with not empty stack
        self.e.stack.append( (["a","b","c"], [0], PREPROCESS_INSTRUCTION, None,) )
        self.e.stack.append( (["d","e","f"], [0,1], PREPROCESS_INSTRUCTION, None,) )
        
            #none cmd id must return the cmd index at the top
        self.e.addSubCommand(Command(), None)
        self.assertEqual(len(self.e.cmdList[0]), 1)
        self.assertEqual(len(self.e.cmdList[1]), 3)
        
        self.e.stack.append( (["d","e","f"], [0,1], PREPROCESS_INSTRUCTION, [True,False,True],) ) 
        self.e.stack.append( (["d","e","f"], [0,1,0], PREPROCESS_INSTRUCTION, [True,False,True],) ) 
        
            #with stack (with random data on stack, not only matching result, != path, != preprocess)
        self.e.addSubCommand(Command(), 1)
                #with path not using this cmd
                #with path using this cmd
                    #with None map
                    #with map enabled
                #with cmd used several times in the cmdList
        self.assertEqual(self.e.stack[1][3],None)
        self.assertEqual(len(self.e.stack[2][3]),4)
        self.assertEqual(len(self.e.stack[3][3]),4)

    #addCommand(self, cmd, convertProcessToPreProcess = False)
    def test_addCommand(self):
        #FAILED
            #try to insert a not MultiCommand instance
        self.assertRaises(executionException, self.e.addCommand, None)
        self.assertRaises(executionException, self.e.addCommand, "toto")
        self.assertRaises(executionException, self.e.addCommand, 52)
        
            #try to insert with process at top
                #with more than one data
        del self.e.stack[:]
        self.e.stack.append( (["a","b","c"], [0], PROCESS_INSTRUCTION, None,) )
        self.assertRaises(executionException, self.e.addCommand, self.mc)
        
            #try to insert with postprocess at top with process in the middle
        del self.e.stack[:]
        self.e.stack.append( (["a","b","c"], [0], PROCESS_INSTRUCTION, None,) )
        self.e.stack.append( (["a"], [0], POSTPROCESS_INSTRUCTION, None,) )
        self.assertRaises(executionException, self.e.addCommand, self.mc)
        
        #SUCCESS
            #try to insert with process at top
                #with only one data
        del self.e.stack[:]
        self.e.stack.append( (["a"], [0], PROCESS_INSTRUCTION, None,) )
        self.e.addCommand(self.mc)
                
            #try to insert with postprocess at top without process in the middle
        del self.e.stack[:]
        self.e.stack.append( (["a"], [0], POSTPROCESS_INSTRUCTION, None,) )
        self.e.addCommand(self.mc)
            
            #insert a valid one with process in the stack, and see if they are correctly converted
        del self.e.stack[:]
        self.e.stack.append( (["a","b","c"], [0], PROCESS_INSTRUCTION, None,) )
        self.e.stack.append( (["a"], [0], POSTPROCESS_INSTRUCTION, None,) )
        self.e.addCommand(self.mc, True)        
        self.assertEqual(self.e.stack[0][2], PREPROCESS_INSTRUCTION)
        
    def test_isCurrentRootCommand(self):
        mc = MultiCommand()
        mc.addProcess(plop,plop,plop)
        mc.addProcess(plop,plop,plop)
        mc.addProcess(plop,plop,plop)

        engine = engineV3([mc,mc,mc],[[],[],[]], [[{},{},{}],[{},{},{}],[{},{},{}]])

        self.assertTrue(engine.isCurrentRootCommand())

        engine.stack[-1][1].append(2)
        self.assertFalse(engine.isCurrentRootCommand())

        del engine.stack[:]
        self.assertRaises(executionException, engine.isCurrentRootCommand)
    
    
if __name__ == '__main__':
    unittest.main()
