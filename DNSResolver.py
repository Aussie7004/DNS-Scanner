"""
#####################################################################################

                    THIS CODE WAS WRITTEN BY AUSSIE7004
            Contact @ aussie7004@gmail.com or Aussie#7004 on Discord

#####################################################################################

"""

import sys
import socket


domain = False
        
try:
    DNS = input("Enter the DNS you would like to resolve or press Ctrl C to exit: ")
    if domain == False:
        try:       
            
            host = socket.gethostbyname(DNS)

            # This will print the IP address instead of the whole hostname
            ip = repr(host)

            
            print("\nThe hostname for {} is {}".format(DNS, host))

            domain = True
            if domain == True:
                exitChoice = input("Would you like to continue to the port scanner? ").lower()

                if exitChoice == "yes" or exitChoice == "y":
                    print("\nAlright. Copy this IP if you would like to use it in the port scanner {}\n".format(ip))
                    import PortScanner
                    
                elif exitChoice == "no" or exitChoice == "n":
                        print("\nThank you for using DNS Scanner made by Aussie7004 aka CountTo8")
                        input("\nPress Enter to exit")
                        sys.exit()

        except:
            #If domain is still false after the user enters the 'DNS', it will come back with an error
            if domain == False:
                print("Invalid hostname.")
            sys.exit()

except KeyboardInterrupt:
    print("\n\nYou pressed Ctrl C... Quitting")
    sys.exit()
