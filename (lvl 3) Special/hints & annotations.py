# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> hints & annotations

empty_string: str
integer: int = 42


def add_numbers2(*args: int) -> int:
    result = int()
    for i in args:
        result += i
    return result
def print_numbers(a: int, b: int, c: int) -> None:
    print(a + b + c)


# pip install mypy (install mypy)
# mypy <path/file.py> (run Static Code Analysis)
