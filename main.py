"""
#####################################################################################

                    THIS CODE WAS WRITTEN BY AUSSIE7004
              Contact @ aussie7004@gmail.com or Aussie#7004 on Discord

#####################################################################################

"""


#If you don't have these installed, you can install them by opening your CMD or Terminal and typing pip install <package name>

#Pyfiglet is a library that allows for ascii style banners. This is responsible for my "DNS Scanner" banner
import pyfiglet
import sys
import socket


class Main():

    choices = 0
    domain = True
    IPsave = 0
    IPsaveBool = False


    def __init__(self):
        pass

    def Title(self):
        banner = pyfiglet.figlet_format("      DNS Scanner")
        print (banner)

        print ("                   Made by Aussie7004 aka CountTo8\n")


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


        if self.choices == 1:
            import DNSResolver
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



