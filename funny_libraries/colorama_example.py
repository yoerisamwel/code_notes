from colorama import init, Fore

init(autoreset=True)
print(Fore.CYAN + 'some red text')
print('automatically back to default color again')

init(autoreset=True)
print(Fore.RED + 'some red text')  # Now it's actually red text
print('automatically back to default color again')

'''
The colorama module is useful for creating terminal text output that 
stands out by adding color. The init(autoreset=True) call is particularly 
helpful as it automatically resets the text color back to the default after 
each print statement, preventing color changes from affecting subsequent text 
that is printed.
'''