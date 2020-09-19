from pprint import pprint


class Bool(int):
    "Just like `bool`, except values display as T and F instead of 'True' and 'False'"
    __str__ = __repr__ = lambda self: T if self else F
    

T = Bool(True)
F = Bool(False)

data = {
    'IW': 0.2,
    'B': {
        T: 0.6,
        F: 0.9
    },
    'SM': {
        T: 0.5,
        F: 0.9
    },
    'R': {
        T: 0.9,
        F: 0.1
    },
    'I': {
        T: 0.9,
        F: 0.2
    },
    'G': 0.9,
    'S': {
        (T, T ,T): 0.9,
        (T, T, F): 0.5,
        (T, F, F): 0.1,
        (F, F, F): 0.01,
        (T, F, T): 0.2,
        (F, T, F): 0.1,
        (F, T, T): 0.15,
        (F, F, T): 0.05
    },
    'M': {
        T: 0.99,
        F: 0.01
    }
}
