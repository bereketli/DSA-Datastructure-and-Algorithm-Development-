def swap_case(s):
    atr =""
    for string in s:
        if string == string.lower():
            atr += string.upper()
        elif string == string.upper():
            atr += string.lower()
        else:
             atr += string
        
        
            
    return atr

