#!/usr/bin/env python3
from sys import argv, exit
import csv
import os
import subprocess
import time

check = ['y','n']

def main():
    info = setup()

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
        infoDict.update({'semCode' : input("Please enter the semester code: ")})
        infoDict.update({'unitType' : input("Please enter the unit type (ex: 'P' is printer, 'CB' is chromebook): ")})
        infoDict.update({'startNum' : int(input("Please enter the starting unit inventory number: "))})
        infoDict.update({'endNum' : ((infoDict.get('unitCount', 'Error getting unit count!!') - 1) + infoDict.get('startNum', 'Error getting start number!!'))})
        while correct not in check:
            print(infoDict)
            correct = input("Does the above information look correct? (y/n)").lower()
            if correct != 'y' and correct in check:
                continue
            elif correct in check:
                return(infoDict)

main()
