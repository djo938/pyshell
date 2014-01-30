#!/usr/bin/python
from pyshell.arg.decorator import shellMethod
from pyshell.arg.argchecker import ArgChecker,listArgChecker
from exception import commandException

class MultiOutput(list): #just a marker class to differentiate an standard list from a multiple output 
    pass

#
# this method check the args with respect to meth
#
# @argument args, the arguments to apply
# @argument meth, the method to wich apply the argument
# @return a dictionary with the argument bounded to the method
#
def selfArgChecker(args,meth):
    if hasattr(meth, "checker"):
        return meth.checker.checkArgs(args)
    else:
        return {} #no available binding

class Command(object):
    #default preProcess
    @shellMethod(args=listArgChecker(ArgChecker()))
    def preProcess(self,args):
        return args

    #default process
    @shellMethod(args=listArgChecker(ArgChecker()))
    def process(self,args):
        return args
    
    #default postProcess
    @shellMethod(args=listArgChecker(ArgChecker()))
    def postProcess(self,args):
        return args
    
    #this method is called on every processing to reset the internal state
    def reset(self):
        pass  #TO OVERRIDE if needed

#
# a multicommand will produce several process with only one call
#
class MultiCommand(list):
    def __init__(self,name,helpMessage,showInHelp=True):
        self.name         = name        #the name of the command
        self.helpMessage  = helpMessage #message to show in the help context
        self.showInHelp   = showInHelp  #is this command must appear in the help context ?
        self.usageBuilder = None        #which (pre/pro/post) process of the first command must be used to create the usage.
        
        self.onlyOnceDict = {}          #this dict is used to prevent the insertion of the an existing dynamic sub command
        self.dymamicCount = 0
        
        self.args         = None        #
        
    def addProcess(self,preProcess=None,process=None,postProcess=None, useArgs = True):
        c = Command(self)
             
        if preProcess != None:
            c.preProcess = preProcess
            
            if self.usageBuilder == None and hasattr(preProcess, "checker"):
                self.usageBuilder = preProcess.checker
        
        if process != None:
            c.process = process
            
            if self.usageBuilder == None and hasattr(process, "checker"):
                self.usageBuilder = process.checker
            
        if postProcess != None:
            c.postProcess = postProcess
            
            if self.usageBuilder == None and hasattr(postProcess, "checker"):
                self.usageBuilder = postProcess.checker
        
        self.append( (c,useArgs,) )
    
    def addStaticCommand(self, cmd, useArgs = True):
        #cmd must be an instance of Command
        if not isinstance(cmd, Command):
            raise commandException("(MultiCommand) addStaticCommand, try to insert a non command object")
            
        #can't add static if dynamic in the list
        if self.dymamicCount > 0:
            raise commandException("(MultiCommand) addStaticCommand, can't insert static command while dynamic command are present, reset the MultiCommand then insert static command")
    
        #if usageBuilder is not set, take the preprocess builder of the cmd 
        if self.usageBuilder == None:
            self.usageBuilder = cmd.preProcess.checker
    
        #add the command
        self.append( (cmd,useArgs,) )
    
    def usage(self):
        if self.usageBuilder == None :
            return self.name+": no args needed"
        else:
            return self.name+" "+self.usageBuilder.usage()

    def reset(self):
        #flush args
        self.args = None
        
        #remove dynamic command
        del self[len(a)-self.dymamicCount:]
        self.dymamicCount = 0
        
        #reset self.onlyOnceDict
        self.onlyOnceDict = {}
        
        #reset counter
        self.preCount = self.proCount = self.postCount = 0
        
        #reset every sub command
        for c,a in self:
            c.preCount  = 0 #this counter is used to prevent an infinite execution of the pre process
            c.proCount  = 0 #this counter is used to prevent an infinite execution of the process
            c.postCount = 0 #this counter is used to prevent an infinite execution of the post process
        
            c.reset()    

    def setArgs(self, args):
        if isinstance(args, MultiOutput):
            self.args = args
        else:
            self.args = MultiOutput([args])
    
    def getArgs(self):
        return self.args 

    def flushArgs(self):
        self.args = None

    def addDynamicCommand(self,c,onlyAddOnce, useArgs = True):
        #cmd must be an instance of Command
        if not isinstance(cmd, Command):
            raise commandException("(MultiCommand) addDynamicCommand, try to insert a non command object")
            
        #check if the method already exist in the dynamic
        h = hash(c)
        if onlyAddOnce and h in self.onlyOnceDict:
            return
            
        self.onlyOnceDict[h] = True
        
        #add the command
        self.append( (c,useArgs,) )
        self.dymamicCount += 1

#
# special command class, with only one command (the starting point)
#
class UniCommand(MultiCommand):
    #def __init__(self,name,helpMessage,showInHelp=True):
    def __init__(self,name,helpMessage,preProcess=None,process=None,postProcess=None,showInHelp=True):
        MultiCommand.__init__(self,name,helpMessage,showInHelp)
        MultiCommand.addProcess(self,preProcess,process,postProcess)

    def addProcess(self,preProcess=None,process=None,postProcess=None):
        pass # blocked the procedure to add more commands



