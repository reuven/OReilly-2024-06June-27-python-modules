def menu(*args):   # I can take any number of positional arguments
    while True:
        s = input(f'Enter your choice ({'/'.join(args)}): ')
    
        if s in args:
            return s
    
        print(f'{s} is not valid; try again')
    