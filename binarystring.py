# binarystring.py cmt
from __future__ import print_function

def bincon(decimal):
    print(decimal)
    print("*******")
    binstr = "" #binstr is a string
    for i in range(8):
        bin = decimal % 2
        decimal = decimal // 2
        #print(bin)
        binstr = binstr + str(bin)
        print(binstr)
    print("---------")
    for i in range(7,0,-1):
        print(binstr[i], end = "")


def main():
    print("Input -1 To exit the program")
    print("Input a positive integer less than 256")
    done = 0
    while (done >= 0):
        print("")
        dec = input("Input an integer : ")
        bincon(dec)
        #print("done", done)
        done = dec
        if dec < 0:
                break

main()
