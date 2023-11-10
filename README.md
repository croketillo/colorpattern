# ColorPattern

ColorPattern is a Python module designed for enhancing text output in the console by applying color to specific patterns. It offers a flexible way to define patterns and apply different text colors, background colors, styles, and underlines to matching text in the output.

## Installation

You can install ColorPattern using pip:

```pip install colorpattern ```


## Usage

```python
from colorpattern import SetPattern, start_color

# Define color patterns
pattern1 = SetPattern(r'\d+', color='green', back='black', style='bright', underline=True)
pattern2 = SetPattern(r'error', color='red', back='yellow', style='dim', underline=False)
pattern3 = SetPattern(r'pattern', back='blue', style='reset_all', underline=True)

# Initialize color for patterns
start_color([pattern1, pattern2, pattern3])

# Your code with colorized output
print("123 error 456 pattern")
```

## Patterns

- `pattern`: Regular expression pattern to match in the text.
- `color`: Text color (e.g., 'green', 'red', 'yellow').
- `back`: Background color (e.g., 'black', 'blue', 'white').
- `style`: Text style (e.g., 'bright', 'dim', 'reset_all').
- `underline`: Set to `True` for underlining matched text.

## Colors (colorama):

### Text Colors (Fore):
Fore.BLACK
Fore.RED
Fore.GREEN
Fore.YELLOW
Fore.BLUE
Fore.MAGENTA
Fore.CYAN
Fore.WHITE
Fore.LIGHTBLACK_EX
Fore.LIGHTRED_EX
Fore.LIGHTGREEN_EX
Fore.LIGHTYELLOW_EX
Fore.LIGHTBLUE_EX
Fore.LIGHTMAGENTA_EX
Fore.LIGHTCYAN_EX
Fore.LIGHTWHITE_EX
Fore.RESET

### Background Colors (Back):
Back.BLACK
Back.RED
Back.GREEN
Back.YELLOW
Back.BLUE
Back.MAGENTA
Back.CYAN
Back.WHITE
Back.LIGHTBLACK_EX
Back.LIGHTRED_EX
Back.LIGHTGREEN_EX
Back.LIGHTYELLOW_EX
Back.LIGHTBLUE_EX
Back.LIGHTMAGENTA_EX
Back.LIGHTCYAN_EX
Back.LIGHTWHITE_EX
Back.RESET

### Text Styles (Style):
Style.NORMAL
Style.BRIGHT or Style.DIM
Style.RESET_ALL
Style.BRIGHT (Bright style)
Style.DIM (Dim style)
Style.NORMAL (Reset brightness and opacity)

## License

This project is licensed under the GNU-GLP,3 License - see the LICENSE file for details.
