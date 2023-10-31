from operations import add
from division import divisionIn
from potencia import power
from Resta import resta
from Multiplicacion import multiplicacion
from module import modulo


def game():
    score = 0
    
    
    while True:
        print('======== Menu ========'
        '\n1. Add'
        '\n2. resta'
        '\n3. multiplicacion'
        '\n4. division'
        '\n5. potencia'
        '\n6. modulo'
        '\n0. Exit')
        option = int(input('\nChoice an option: '))
        if option == 0:
            break
        num_1 = float(input('Enter first number: '))
        num_2 = float(input('Enter second number: '))
        answer = float(input('Enter you answer: '))
        if option == 1:
            resultf = add(num_1, num_2)

            if resultf == answer:

                score += 1
                print('Correct!!')
        else:
            print('Incorrect')


        if option == 2:
            resultf = resta(num_1, num_2)

            if resultf == answer:

                score += 1
                print('Correct!!')
        else:
            print('Incorrect')

        
        if option == 3:
            resultf = multiplicacion(num_1, num_2)

            if resultf == answer:

                score += 2
                print('Correct!!')
        else:
            print('Incorrect')


        if option == 4:
            resultf = divisionIn(num_1, num_2)

            if resultf == answer:

                score += 2
                print('Correct!!')
        else:
            print('Incorrect')


        if option == 5:
            resultf = power(num_1, num_2)
            
            if resultf == answer:

                score += 4
            print('Correct!!')
        else:
            print('Incorrect')

        
        if option == 6:
            resultf = modulo(num_1, num_2)
            
            if resultf == answer:

                score += 4
            print('Correct!!')
        else:
            print('Incorrect')
    


    print(f'======== Game Over ========'
    f'\nYou score is {score}'
    '\nKeep going!')
game()
