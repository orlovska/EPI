# From input number(7 to 9 characters) return all possible phone mnemonics 
# Digits corresponding characters: ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


lst = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

def phone_mnemonics(phone_number):
    if type(phone_number) not in [str]:
        raise TypeError("Required argument in quotes: '', '234'")
    
    result = []
    mnemonic = [0] * len(phone_number)
    digit = 0
   
    def phone_mnemonics_helper(digit):
        # Base case
        if digit == len(phone_number):
            result.append(''.join(mnemonic))
            return result

        for char in lst[int(phone_number[digit])]:
            mnemonic[digit] = char
            phone_mnemonics_helper(digit +1)
        return result
       
    return phone_mnemonics_helper(digit)     