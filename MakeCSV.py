import sys
import csv
import re
import subprocess
import glob


class Setup:
    def __init__(
        self, cart, po, unit_count, year, sem_code, unit_type, start_num, end_num
    ):
        self.info = (
            cart,
            po,
            unit_count,
            year,
            sem_code,
            unit_type,
            start_num,
            end_num,
        )

        return self.info

    @classmethod
    def get(cls):
        cart = input("Please enter the cart name: ")
        po = input("Please enter the PO Number for the order: ")
        while True:
            unit_count = input("Please enter the number of units for the order: ")
            if not re.search(r"^[0-9]+$", unit_count):
                print(f"Invalid Unit count")
            else:
                unit_count = int(unit_count)
                break
        while True:
            year = input("Please enter the inventory year (ex. 22): ")
            if not re.search(r"^(?:2[2-9])$", year):
                print(f"Invalid year")
            else:
                break
        while True:
            sem_code = input("Please enter the semester code (FA, SP, SU): ").upper()
            if not re.search(r"^(FA|SP|SU)$", sem_code):
                print(f"Invalid Semester Code")
            else:
                break
        while True:
            unit_type = input(
                "Please enter the type of units (CB, P, PJ, HF): "
            ).upper()
            if not re.search(r"^(CB|PJ|P|HF)$", unit_type):
                print("Invalid Unit Type")
            else:
                break
        while True:
            start_num = input("Please enter the starting serial number: ")
            if not re.search(r"^[0-9]{4}$", start_num):
                print("Invalid start number, ex. 2234")
            else:
                validate = input(
                    f"You have entered {start_num} as starting serial number, is that correct? y/n "
                ).lower()
                if re.search(r"^(y|n)$", validate, flags=re.IGNORECASE):
                    start_num = int(start_num)
                    break
        end_num = (unit_count - 1) + start_num

        return cart, po, unit_count, year, sem_code, unit_type, start_num, end_num


class Compose:
    def __init__(self, info):
        self.new_file(info)
        self.write_file(info)

    def __str__(self):
        return f"New file {self.filename} has been composed."

    def new_file(self, info):
        self.filename = f"{info[0]}-PO{info[1]}-Units{info[2]}-{info[6]}-{info[7]}.csv"
        return self.filename

    def write_file(self, info):
        for i in range(0, int(info[2])):
            self.current_num = int(info[6]) + i
            self.asset_tag = (
                info[3] + info[4] + str(self.current_num) + info[5],
                "",
                "",
                "",
            )
            with open(self.filename, mode="a") as csv_file:
                unit_file = csv.writer(csv_file, delimiter=",")
                unit_file.writerow(self.asset_tag)


class Duplicate:
    def __init__(self, info):
        self.check(info)

    def check(self, info):
        self.test = []
        self.files = glob.glob("*.csv")
        for i in range(0, len(self.files)):
            self.repeat_check = subprocess.Popen(
                ["grep", str(info[6]), self.files[i]], stdout=subprocess.PIPE
            )
            self.search = self.repeat_check.stdout.read().decode().strip()
            self.search = str(self.search)
            print(f"\n{self.search} Found!! ---------> {self.files[i]}\n")
            if re.search(r"^(.*)" + re.escape(str(info[6])) + "(.*)$", self.search):
                raise ValueError("\n\tYou have a duplicate serial number!!\n")

        return False

def main():
    setup = Setup.get()
    Duplicate(setup)
    compose = Compose(setup)
    print(compose)


if __name__ == "__main__":
    main()
