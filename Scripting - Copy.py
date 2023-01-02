while True:
    try:
        x = float(input('Enter a the price of the item + tax:'))
        break  
    except ValueError:
        print('That\'s not a valid number!')
    except KeyboardInterrupt:
        print('\nNo input taken')
    finally:   
        print('\nProgram Executed\n')