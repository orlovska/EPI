# From input number(7 to 9 characters) return all possible phone mnemonics 
# Digits corresponding characters: ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def chars_for_digit(number):
    List = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    return List[int(number)] 


def check_for_more_values(phone_number, result):
    try:
        last_char_of_the_supirior_node = chars_for_digit(phone_number[0])
        if last_char_of_the_supirior_node[-1] in result[-1]:
            return False
    except:
        return True


def phone_mnemonics(phone_number):
    if type(phone_number) not in [str]:
        raise TypeError("Required argument in quotes: '', '234'")
    
    result = []
    mnemonic = ''
    
    def phone_mnemonics_helper(phone_number):
        for digit in chars_for_digit(phone_number[0]):
            nonlocal mnemonic
            mnemonic += digit
                                                    # END OF MNEMONIC - when phone_number decreased to one digit whitch had been added to mnemonic          
            if len(phone_number) > 1:
                phone_mnemonics_helper(phone_number[1:])
            else:
                result.append(mnemonic)
                                                    # Atfer adding to result - CHANGING LAST MNEMONIC LETTER
                mnemonic = mnemonic[:-1]
                                                    # After the end of for loop - CHANGITG SUPERIOR MNEMONIC LETTER
        mnemonic = mnemonic[:-1]
                                                    # COMPLETE ONE RECURSIVE CALL  
        if check_for_more_values(phone_number, result) is False:
            return result
        else:
            return mnemonic
    
                                                    # RECURSION BASE CASE
    if phone_number == '':
        return result 
    else:
        return phone_mnemonics_helper(phone_number)
