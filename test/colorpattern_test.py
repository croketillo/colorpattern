from colorpattern.colorpattern import *


pattern1 = SetPattern(r'\d+',color=Fore.GREEN)
pattern2 = SetPattern(r'Colorpattern',color=Fore.LIGHTRED_EX, underline=True)
pattern3 = SetPattern(r'Croketillo',color=Fore.RED,back=Back.LIGHTYELLOW_EX, style=Style.BRIGHT)
email = SetPattern(r'\b[A-Za-z0.9._%+-]+@[A-Za-z0.9.-]+\.[A-Z|a-z]{2,7}\b', color=Fore.LIGHTCYAN_EX)

start_color([pattern1,pattern2,pattern3, email])

print('2133 Colorpattern 432423')
print('By Croketillo - croketillo@gmail.com')
