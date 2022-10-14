#!/usr/bin/env python3
from sys import argv, exit
import csv
import os
import subprocess
import time

divider = "######################################################################################"

def main():
    confirm = None
    os.system('cat jhart_shell_logo.txt')
    print((divider + '\n')*2)
    while confirm != 'y':
        info = setup()
        newFile = str(info.get('cart', "Error getting Cart name!!") + "-PO" + info.get('po', "Error getting PO Number")
                    + "-Units" + str(info.get('unitCount', 'Error getting Unit count!!')) + "-" +
                    str(info.get('startNum', 'Error getting Start number!!')) + "-" + str(info.get('endNum', 'Error getting Ending Number!!'))+".csv")
        while confirm not in check:
            confirm = input("Your new file will be named: " + newFile + " Is this correct? (y/n) ").lower()
            dupCheck = duplicateCheck(str(info.get('startNum')),template,newFile)
        if confirm == 'y' and dupCheck:
            print("You have entered duplicate inventory numbers, check your info and try again!!!")
            confirm = None
    composeFile(newFile,str(info.get('startNum')),info.get('unitCount'),info.get('year'),info.get('semCode'),info.get('unitType'))
    print("You new file " + newFile + " has been created.  Thank you and have a great day! -JHart")



def setup():
    valid = False
    infoDict = {
    'cart': None,
    'po' : None,
    'unitCount' : None,
    'year' : None,
    'semCode' : None,
    'unitType' : None,
    'startNum' : None,
    'endNum' : None
    }
    while not valid:
        correct = None
        infoDict.update({'cart' : input("Please enter the cart name: ")})
        infoDict.update({'po' : input("Please enter the PO Number for this order: ")})
        infoDict.update({'unitCount' : int(input("Please enter how many units will be in this cart: "))})
        infoDict.update({'year' : input("Please enter the Inventory Year (YY): ")})
        infoDict.update({'semCode' : input("Please enter the semester code: ").upper()})
        infoDict.update({'unitType' : input("Please enter the unit type (ex: 'P' is printer, 'CB' is chromebook): ").upper()})
        infoDict.update({'startNum' : int(input("Please enter the starting unit inventory number: "))})
        infoDict.update({'endNum' : ((infoDict.get('unitCount', 'Error getting unit count!!') - 1) + infoDict.get('startNum', 'Error getting start number!!'))})
        while correct not in check:
            print(infoDict)
            correct = input("Does the above information look correct? (y/n) ").lower()
            if correct != 'y' and correct in check:
                continue
            elif correct in check:
                return(infoDict)

def duplicateCheck(startingNum,csvTemplate,newFile):
    repeatCheck = None
    COMMAND = ('grep ' + startingNum + ' *.csv')
    repeatCheck = subprocess.call(COMMAND, stdout=open(os.devnull, 'w'), stderr=open(os.devnull), shell=True)
    if repeatCheck == 1 or repeatCheck == 2:
        subprocess.call(['cp',csvTemplate,newFile])
        return False
    elif repeatCheck == 0:
        return True
    else:
        print("Unknown error, turning off the lights now!!")
        exit(1)

def composeFile(newFile,startNum,unitCount,year,semCode,unitType):
    for i in range(0,unitCount):
        currentNum = (int(startNum) + i)
        assetTag = (year + semCode + str(currentNum) + unitType,"","","")
        with open(newFile, mode='a') as csvFile:
            unitFile = csv.writer(csvFile, delimiter=',')
            unitFile.writerow(assetTag)

main()
