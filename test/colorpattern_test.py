from colorpattern.colorpattern import *

def main():
    # Define your color patterns
    pattern1 = SetPattern(r'\d+', color=Fore.GREEN)
    pattern2 = SetPattern(r'Colorpattern', color=Fore.LIGHTRED_EX, underline=True)
    pattern3 = SetPattern(r'Croketillo', color=Fore.BLACK, back=Back.LIGHTWHITE_EX, style=Style.BRIGHT)
    email = SetPattern(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', color=Fore.BLUE)
    strike= SetPattern(r'NEW!!!', strikethrough=True)
    blink=SetPattern(r'BLINK', blink=True)
    italic=SetPattern(r'ITALIC TEXT', italic=True)

    # Initialize colorization and get the original print function and applied patterns
    print("\nSTART COLORIZED PRINT")
    print('-----------------------')
    start_color([pattern1, pattern2, pattern3, email, strike, italic,blink])

    # Use the custom print function with colorization
    print('Colorpattern v1.4.5')
    print('By Croketillo - croketillo@gmail.com')
    print('NEW!!! - NOW YOU CAN INCLUDE STRIKETHROUGH IN PATTERNS')
    print('This is a BLINK and ITALIC TEXT test')

    # End colorization and restore the original print function
    end_color()
    print("\nNORMAL PRINT")
    # Now, printing returns to normal

    print('-----------------------')
    print('Colorpattern v1.4.5')
    print('By Croketillo - croketillo@gmail.com')
    print('NEW!!! - NOW YOU CAN INCLUDE STRIKETHROUGH IN PATTERNS')
    print('This is a BLINK and ITALIC TEXT test')

    # You can re-enable colorization with new patterns if necessary
    new_pattern = SetPattern(r'new pattern', color=Fore.LIGHTCYAN_EX)

    # Use the custom print function with new patterns
    print("\nSTART COLORIZED PRINT AGAIN")
    start_color([pattern1, new_pattern])

    print('-----------------------')
    print('This is a new pattern. 123456')

    # End colorization and restore the original print function
    end_color()
    print("\nNORMAL PRINT AGAIN")
    # Now, printing returns to normal even with the new patterns
    print('-----------------------')
    print('This is a normal message again. 12345')

if __name__ == "__main__":
    main()
