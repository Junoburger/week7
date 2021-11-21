def main():
    fahr = (float(input("Please enter a temprature in fahrenheit: ")))
    cel = fahrenheit_to_celcius(fahr)
    print("Fahrenheit:", fahr, "=", cel, "degrees celcius")


def fahrenheit_to_celcius(F):
    C = (F - 32) * (5/9)
    return C


main()
