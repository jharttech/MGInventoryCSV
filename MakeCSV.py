#!/usr/bin/env python3
from sys import argv, exit
import csv
import os
import subprocess
import time

check = [y,n]

def main():
    setup()

def setup():
    cart = input("Please enter the cart name: ")
    po = input("Please enter the PO Number for this order: ")
    unitCount = int(input("Please enter how many units will be in this cart: "))
    year = input("Please enter the Inventory Year (YY): ")
    semCode = input("Please enter the semester code: ")
    unitType = input("Please enter the unit type (ex: 'P' is printer, 'CB' is chromebook): ")
    startNum = int(input("Please enter the starting unit inventory number: "))
    endNum = ((unitCount - 1) + startNum)
    
main()
