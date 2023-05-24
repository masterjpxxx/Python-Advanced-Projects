def checkcasing(value):
    if value.isupper():
        print(f'{value} is in uppercase!')
    elif value.islower():
        print(f'{value} is in lowercase!')
        
    
    
value = input('Input a string: ')
checkcasing(value)