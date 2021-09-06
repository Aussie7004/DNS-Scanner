"""
#####################################################################################

                    THIS CODE WAS WRITTEN BY AUSSIE7004
              Contact @ aussie7004@gmail.com or Aussie#7004 on Discord

#####################################################################################

"""


#If you don't have these installed, you can install them by opening your CMD or Terminal and typing pip install <package name>

#Pyfiglet is a library that allows for ascii style banners. This is responsible for my "DNS Scanner" banner
import pyfiglet
#Sys is just responsible for program functions (Used mainly in this code for sys.exit() which exits the code when called)
import sys
#Socket allows you to connect to the specific nodes, etc, in order to resolve the hostnames from the DNS specified and scan for open ports
import socket


class Main():

    choices = 0
    domain = True
    IPsave = 0
    IPsaveBool = False

#Initiation function which allows global variables to be individual when called in functions

    def __init__(self):
        pass

#This prints the banner 'DNS Scanner' in ascii style as well as 'Made by Aussie7004 aka CountTo8 (subtle plug)

    def Title(self):
        banner = pyfiglet.figlet_format("      DNS Scanner")
        print (banner)

        print ("                   Made by Aussie7004 aka CountTo8\n")

#This function just prints the available options (more coming soon)

    def options(self):
        print("\nPick an option from below: ")
        self.choices = int(
            input("\n1. DNS Resolver\n2. Port Scanner\n99. Quit\n\n"))

#Def optionPick is where the user picks which option they want to use in the program - This was done so that the later on if I or someone were to add more options, they
#didn't need to fill the options function with a whole bunch of if statements, etc...

    def optionPick(self):

        if self.choices > 2 and self.choices != 99 or self.choices < 1:
            while self.choices > 2 and self.choices != 99 or self.choices < 1:
                print("\nEnter a valid choice:")
                self.choices = int(input("\n1. DNS Resolver\n2. Port Scanner\n99. Quit\n\n"))

#If user inputs 1, the DNS Resolver will get imported
        if self.choices == 1:
            import DNSResolver
#If user inputs 2, the Port Scanner will get imported
        elif self.choices == 2:
            import PortScanner

        elif self.choices == 99:
            sys.exit()

def main():
    sr.Title()
    sr.options()
    sr.optionPick()

sr = Main()

main()



