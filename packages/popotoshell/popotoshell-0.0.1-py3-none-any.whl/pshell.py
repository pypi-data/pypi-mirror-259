#!/usr/bin/python3
import json
import sys
import socket
import threading
import default_shell
import argparse

class pshell(default_shell.default_shell):
    def __init__(self, initfile="pshell.init"):
        super().__init__(initfile)
        self.customshellEnabled=False
        self.intro="""

                                       em_Po
                                  toModem_
                               opotoModem
                             _PopotoModem_
                    potoModem_PopotoModem_Popot
                m_PopotoModem_PopotoModem_PopotoM
             odem_PopotoModem_PopotoModem_PopotoModem
            Modem_PopotoModem_PopotoModem_PopotoModem_Pop
          toModem_PopotoModem_PopotoModem_PopotoModem_Popot
        potoModem_PopotoModem_PopotoModem_PopotoModem_PopotoM
       opotoModem_PopotoModem_PopotoModem_PopotoModem_PopotoMo
      PopotoModem_PopotoModem                     dem_PopotoMode
      PopotoModem_PopotoModem_Popoto                   opotoModem
       opotoModem_PopotoModem_Popot                          Modem_
       opotoModem_                                              em_PopotoM
      Popoto                                                      _PopotoMode
     _Po                                                           PopotoModem
                                                                    o
                                                                     po
                     Welcome to the Popoto Modem Shell!

                          Communicating Naturally
"""

        #for storing previous prompt
        self.originalprompt = ''
        #storing previous verbosity
        self.previousverbosity = 3
        self.InterPlayDelay = 5
        # This is the prompt of the custom shell, currently set to nothing
        self.customprompt = ""

        self.customshellEnabled = False

    def precmd(self, line):
        # precmd preprocesses the entered command before the cmd loop calls the apropriate function
        line = super().precmd(line)
        return line
    
    def do_setHop(self, line):
        """
        The transmitJSON method sends an arbitrary user JSON message for transmission out the 
        acoustic modem. 
        
        :param      JSmessage:  The Users JSON message
        :type       JSmessage:  string
        """
        
        args = line.split(" ",2)
         # Format the user JSON message into a setHop message for Popoto like this
        # '{"Command":"setHop","Arguments":"Destination:B, Offset: 12, Bytes: 3,4,5,6,7,8,9"}' 

        message = '{"Command":"setHop","Arguments":"Destination:' + args[0]+', Offset:' + args[1]+', Bytes:'+args[2]+'"}'
        # Verify the JSON message integrity and send along to Popoto

        try:            
            testJson = json.loads(message)
            print("Sending " + message)
            message = message + '\n'
            self.popoto.cmdsocket.sendall(message.encode())
        except:
            print("Invalid JSON message: ", JSmessage)

        
    def do_customshell(self,line):
        """
        Quiets the output
        accepts all pshell commands
        """

        # toggling between custom shell enabled and disabled
        self.customshellEnabled = not self.customshellEnabled

        # if enabled store pshell state values and spin up a parsing thread for customshell
        if self.customshellEnabled:
            # storing original prompt
            self.originalprompt = self.prompt
            # storing previous verbosity level
            self.previousverbosity = self.popoto.verbose
            # muting all messages
            self.popoto.verbose = 0

            self.popoto.drainReplyQquiet()

            # custom prompt is empty so this acts to mute the prompt for the Custom shell
            self.prompt = self.customprompt

            # starting customshell response parsing loop in background
            self.ParseCustomThread = threading.Thread(target=self.customParsingLoop, name="CustomParsingLoop")
            self.ParseCustomThread.start()
        else:
            # resetting the verbosity to its previous level along with the prompt
            self.prompt = self.originalprompt
            self.popoto.verbose = self.previousverbosity

    def customParsingLoop(self, line=None):
        pass
        # loop to parse and process until custom shell is disabled
       
        # INSERT YOUR CUSTOM PARSING LOOP HERE!
        print("Warning: No parsing loop defined!")  # Remove this line when information is parsed



    def openDataSocket(self):
        self.datasocket = socket(AF_INET, SOCK_STREAM)
        self.datasocket.connect((self.ip, self.dataport))
        self.datasocket.settimeout(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='pshell', description='''Popoto modem interactive shell
                                     processes commands and interacts with the popoto application''')
    parser.add_argument('--initfile', default='pshell.init',help="specify a text file init script ")
    parser.add_argument('--unittest', default=False, type= bool, help = "run the pshell command and exit")
    parser.add_argument('--port', default=17000, help = "Base command port ")
    parser.add_argument('--ip', default='localhost')
    parser.add_argument('--connect', default=False, type=bool)
    parser.add_argument('rest', nargs='*')
    
    # output = [module.__name__ for module in sys.modules.values() if module]
    # output = sorted(output)
    # print('The list of imported Python modules are :',output)
    
    args = parser.parse_intermixed_args()

    print("Init File:", args.initfile)
    print("Unit Test:", args.unittest)
    
    ps = pshell(args.initfile)
    connected = False

    if args.connect == True:
        ps.onecmd("connect {} {}".format(args.ip, args.port))

    for c in args.rest:
        ps.onecmd(c)

    if args.unittest == False:
        done = False
        while(done == False):
            try:
                ps.cmdloop()
                done = True
            except Exception as e:
                if ps.verbose_exceptions:
                    print(e.with_traceback(None))
                else:
                    print("Invalid Input {}".format(sys.exc_info()[0] ))
                ps.intro = ""
    else:
        ps.onecmd('exit')




