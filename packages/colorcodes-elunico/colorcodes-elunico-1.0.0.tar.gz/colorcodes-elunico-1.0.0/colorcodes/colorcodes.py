import sys


class cfs:
    def __init__(self, s):
        self.str = s

    def __format__(self, format_spec: str) -> str:
        sentinel = object()
        options = {
            'magenta': magenta,
            'blue': blue,
            'green': green,
            'yellow': yellow,
            'red': red,
            'black': black,
            'bold': bold,
            'uline': uline,
            'm': magenta,
            'b': blue,
            'g': green,
            'y': yellow,
            'r': red,
            'k': black,
            '+': bold,
            'u': uline,
            '_': uline,
            'reset': black,
            'off': black,
            's': bold,
            'strong': bold,
        }
        values = format_spec

        result = []
        for i in values:
            if (x := options.get(i, sentinel)) is sentinel:
                raise ValueError("Invalid format specifier: {}".format(i))
            result.append(str(x))

        return ''.join(result) + self.str + black.code


class ColorCode:
    def __init__(self, name: str, code: str) -> None:
        self.name = name
        self.code = code

    def __add__(self, other: 'ColorCode') -> 'ColorCode':
        return ColorCode(self.name + ' ' + other.name, self.code + other.code)

    def __repr__(self) -> str:
        return f'ColorCode({repr(self.name)}, {repr(self.code)})'

    def __str__(self) -> str:
        return self.code

    def __format__(self, __format_spec: str) -> str:
        if __format_spec == 'b':
            return '\033[1m' + self.code
        elif __format_spec:
            raise ValueError(
                "Invalid format specifier: '{}'".format(__format_spec))
        return self.code

    def print(self, *messages: str, end: str = '\n', sep: str = ' ', file=sys.stdout):
        print(self.code, sep='', end='', file=file)
        print(*messages, end=end, sep=sep, file=file)


magenta = ColorCode('magenta', '\033[95m')
blue = ColorCode('blue', '\033[94m')
green = ColorCode('green', '\033[92m')
yellow = ColorCode('yellow', '\033[93m')
red = ColorCode('red', '\033[91m')
black = ColorCode('black', '\033[0m')
bold = ColorCode('bold', '\033[1m')
uline = ColorCode('uline', '\033[4m')
off = ColorCode('off', '\033[0m')


def cprint(color: ColorCode, *messages: str, end: str = '\n', sep: str = ' ', file=sys.stdout):
    print(color, end='', sep='', file=file)
    print(*messages, end=end, sep=sep, file=file)
