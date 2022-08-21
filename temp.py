def main():
    choice = input("Deseja converter que unidade?\n\nC - Celsius\nF - Fahrenheit\nK - Kelvin\n\n")
    if choice == 'c':
        celcius()
    elif choice == 'f':
        fahrenheit()
    elif choice == 'k':
        kelvin()

def celcius():
    temp = int(input("\nDigite a temperatura em Celsius: \n\n"))
    f = 1.8 * temp + 32
    print()
    print("{:.2f}".format(f), "°F")

    k = temp - 273
    print(f'{k} K')

def fahrenheit():
    temp = int(input("\nDigite a temperatura em Fahrenheit: \n\n"))
    c = ((temp - 32) * 5) / 9
    print(f'\n{c} °C')

    k = c - 273
    print(f'{k} K')

def kelvin():
    temp = int(input("\nDigite a temperatura em Kelvin: \n\n"))
    c = temp - 273
    print(f'\n{c} °C')

    f = 1.8 * c + 32
    print("{:.2f}".format(f), "°F")

main()
