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

        # Using while loops to verify integrity of the input, if input is invalid,
        # program will ask for input again until valid
        while True:
            unit_count = input("Please enter the number of units for the order: ")
            # Use regex to verify integrity of input
            if not re.search(r"^[0-9]+$", unit_count):
                print(f"Invalid Unit count")
            else:
                # If the input is valid, convert it to an int
                unit_count = int(unit_count)
                break

        # Using while loops to verify integrity of the input, if input is invalid,
        # program will ask for input again until valid
        while True:
            year = input("Please enter the inventory year (ex. 22): ")
            # Use regex to verify integrity of input
            if not re.search(r"^(?:2[2-9])$", year):
                print(f"Invalid year")
            else:
                break

        # Using while loops to verify integrity of the input, if input is invalid,
        # program will ask for input again until valid
        while True:
            sem_code = input("Please enter the semester code (FA, SP, SU): ").upper()
            # Use regex to verify integrity of input
            if not re.search(r"^(FA|SP|SU)$", sem_code):
                print(f"Invalid Semester Code")
            else:
                break

        # Using while loops to verify integrity of the input, if input is invalid,
        # program will ask for input again until valid
        while True:
            unit_type = input(
                "Please enter the type of units (CB, P, PJ, HF): "
            ).upper()
            # Use regex to verify integrity of input
            if not re.search(r"^(CB|PJ|P|HF)$", unit_type):
                print("Invalid Unit Type")
            else:
                break

        # Using while loops to verify integrity of the input, if input is invalid,
        # program will ask for input again until valid
        while True:
            start_num = input("Please enter the starting serial number: ")
            # Use regex to verify integrity of input
            if not re.search(
                r"^[0-9]{4}$", start_num
            ):  # Expand this to {5} if serial is above 9999
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


def compose(info):
    filename = f"{info[0]}-PO{info[1]}-Units{info[2]}-{info[6]}-{info[7]}.csv"
    for i in range(0, int(info[2])):
        current_num = int(info[6]) + i
        asset_tag = (
            info[3] + info[4] + str(current_num) + info[5],
            "",
            "",
            "",
        )
        with open(filename, mode="a") as csv_file:
            unit_file = csv.writer(csv_file, delimiter=",")
            unit_file.writerow(asset_tag)
    return f"New file {filename} has been composed."


def duplicate(info):
    files = glob.glob("*.csv")
    for i in range(0, len(files)):
        repeat_check = subprocess.Popen(
            ["grep", str(info[6]), files[i]], stdout=subprocess.PIPE
        )
        search = str(repeat_check.stdout.read().decode().strip())
        if re.search(r"^(.*)" + re.escape(str(info[6])) + "(.*)$", search):
            raise ValueError(
                f"\nYou have a duplicate serial number!!: \n\n{search} --> file: {files[i]}\n"
            )
    return False


def main():
    if len(sys.argv) > 1:
        sys.exit("Too many command arguments.  Usage: python3 project.py")
    else:
        setup = Setup.get()
        check = duplicate(setup)
        if check == False:
            compose(setup)


if __name__ == "__main__":
    main()
