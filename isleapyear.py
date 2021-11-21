def isleapyear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
                # print("{0} was a leap year".format(year))
            else:
                return False
                # print("{0} was not a leap year".format(year))
        else:
            return True
            # print("{0} was a leap year".format(year))
    else:
        return False
        # print("{0} was not a leap year".format(year))


# mybirthyear = 2000

# if isleapyear(mybirthyear):
#     print("Year {0} was a leap year".format(mybirthyear))
