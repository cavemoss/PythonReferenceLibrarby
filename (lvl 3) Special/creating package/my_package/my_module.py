def function(text: str, times: int | None = None):
    if times is not None:
        print((text + ' ') * times)
    else:
        print(text + ' ')
