#!/usr/bin/env python3

from datetime import datetime, time


def main():
    choice = "y"
    while choice.lower() == "y":
        # a welcome message
        print("Birthday Calculator")
        print()

        name = input("Enter name: ")
        day = input("Enter birthday (MM/DD/YY): ")
        today = datetime.today
        

        bday = datetime.strptime(day, "%m/%d/%y")
        tday = datetime.now()
        if bday.year > tday.year:
            new_year = bday.year - 100
            bday = datetime(new_year, bday.month, bday.day)


        c = bday.strftime("%A, %B %d, %Y")
        print("Birthday: ", c)
        k = tday.strftime("%A, %B %d, %Y")
        print("Today: ", k)


        age = tday.year - bday.year
        temp_bday = datetime(2020, bday.month, bday.day)
        until_bday = tday - temp_bday
        if temp_bday > tday:
            print(name, "is", age - 1, "years old.")
            print(name, "'s birthday is in", until_bday.days * -1, "days.")
        elif temp_bday.days < tday:
            print(name, "is", age, "years old.")
            if until_bday == 0:
                print(name, "'s birthday is today!")
            else:
                print(name, "'s birthday was", until_bday.days, "days ago.")

        choice = input("Continue? (y or n): ")
        print()

if __name__ == "__main__":
    main()
