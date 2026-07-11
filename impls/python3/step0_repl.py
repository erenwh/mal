def READ(source: str) -> str:
    return source


def EVAL(ast: str) -> str:
    return ast


def PRINT(form: str) -> str:
    return form


def rep(source: str) -> str:
    return PRINT(EVAL(READ(source)))

if __name__ == '__main__':
    while True:
        try:
            print(rep(input('user> ')))
        except EOFError:
            break