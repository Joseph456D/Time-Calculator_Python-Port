def input_time():
    while True:
        time = input("Enter the time in HH MM SS format: ").split()
        hh, mm, ss = map(int, time)
        if mm >= 60 or ss >= 60:
            print("Wrong Input. Type Again.")
        else:
            return hh, mm, ss

def calculation(time1, time2, choice):
    if choice == 1:  # Addition
        time1[0] += time2[0]
        time1[1] += time2[1]
        time1[2] += time2[2]

        time1[1] += time1[2] // 60
        time1[2] %= 60
        time1[0] += time1[1] // 60
        time1[1] %= 60


    elif choice == 2:  # Subtraction
        time1[0] -= time2[0]
        time1[1] -= time2[1]
        time1[2] -= time2[2]

        if time1[2] < 0:
            time1[2] += 60
            time1[1] -= 1

        if time1[1] < 0:
            time1[1] += 60
            time1[0] -= 1


time1 = list(input_time())
    
while True:
    print(f'Press \033[1m"1"\033[0m for adding, \033[1m"2"\033[0m for subtracting: ', end='')
    choice = input()
    while choice not in ['1', '2']:
        print("Wrong choice. Press Correct Option.")
        print(f'Press \033[1m"1"\033[0m for adding, \033[1m"2"\033[0m for subtracting: ', end='')
        choice = input()

    time2 = list(input_time())

    calculation(time1, time2, int(choice))

    print(f"The resultant time is {time1[0]:02d}:{time1[1]:02d}:{time1[2]:02d}")
        
    continue_choice = input(f'Press \033[1m"1"\033[0m to continue and \033[1m"0"\033[0m to stop: ')
    if continue_choice != '1':
        break


