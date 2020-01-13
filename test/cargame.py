command_input = ''
started = False
while True:
    command_input = input('> ').upper()
    if command_input=='HELP':
        print(''' start -  to start the car
        stop - to stop the car
        quit - to exit''')
    elif command_input=='START':
        if started:
            print('Car already Started')
        else:
            started=True
            print('Car started - Ready to go..')
    elif command_input=='STOP':
        if not started :
            print('Car already Stopped')

        else:
            started =False
            print('Car stopped')
    elif command_input=='QUIT':
        break

    else:
        print("I don't understand that... ")
