def checkPause(statement):
    if statement.upper() == 'PAUSE':
        return True
    else:
        return False
def int_data_validation(validation_statement):
    not_validated = True
    while not_validated:
        try:
            statement = input(str(validation_statement))
            check = checkPause(statement)
            if check == True:
                return 'confirmed'
            int_data_validated=int(statement)
            if int_data_validated >= 0 and  int_data_validated<=8:
                not_validated = False
                return int_data_validated
            else:
                print('                                            type a number greater or equal to 1 but less than or equal to 8')
        except ValueError:
            print('                                            please type a number')
def Xcord_data_validation(validation_statement):
    chars = ['A','B','C','D','E','F','G','H']
    not_validated = True
    while not_validated:
        try:
            data_validated=input(str(validation_statement))
            check = checkPause(data_validated)
            if check == True:
                return 'confirmed'
            if data_validated.upper() in chars:
                not_validated = False
                return data_validated
            else:
                print('                                            type a a character that is from a - h')
        except ValueError:
            print('                                            please type a character that is from a - h')