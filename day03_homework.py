while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime number"
                 "   4) Section Prime number   5) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')

    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')

    elif menu == '3':
        number = int(input("Input number : "))
        is_prime = True
        if number < 2:
            print(f'{number} is NOT prime number!')
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(f'{number} is prime number''\n')
                continue
            else:
                print(f'{number} is NOT prime number!''\n')
                continue

    elif menu == '4':
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                pass
                # pass
                continue
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(number, end=' ')
        print('\n')

    elif menu == '5':
        print("Quit Program")
        break