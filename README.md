# ColorPattern

ColorPattern is a Python module designed for enhancing text output in the console by applying color to specific patterns. It offers a flexible way to define patterns and apply different text colors, background colors, styles, and underlines to matching text in the output.

## Installation

You can install ColorPattern using pip:

```pip install colorpattern ```


## USAGE

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

## License

This project is licensed under the GNU-GLP,3 License - see the LICENSE file for details.