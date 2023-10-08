# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> imports

if __name__ == '__main__':
    import my_module
    my_module.function()

if __name__ == '__main__':
    import my_module as mod
    mod.function()

if __name__ == '__main__':
    from my_module import *
    function()

if __name__ == '__main__':
    from my_module import function
    function()

help('modules')
