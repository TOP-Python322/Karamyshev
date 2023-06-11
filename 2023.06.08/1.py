def strong_password(password):  #making a function with object "password" which will use as main object
    if len(password) < 8:  #make sure it length not less than 8
        return False  #if it so return False
        
    has_lowercase = False   #making a list of flags which shall help us rightr mark making
    has_uppercase = False
    has_digit = False
    has_special_chars = False
    
    for char in password:
        if char.islower():    #if it contain just any lower char
            has_lowercase = True
        elif char.isupper(): #if it contain just any upper char
            has_uppercase = True
        elif char.isdigit(): #if it contain just any number char
            has_digit = True
        else:                #if it contain just other sort of chars
            has_special_chars = True 
            
    return has_lowercase and has_uppercase and has_digit and has_special_chars  #if any conditions satisfy we return True for all has_* flags 
    
password_input = input("\nEnter ur password: ")
if strong_password(password_input):
    print("\nStrong password dude")   #if true
else:
    print("\nYou shall not pass, boy") #if false

                                 