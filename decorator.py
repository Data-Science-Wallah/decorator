# 💡 What’s a Decorator?
# A decorator in Python is just a function that adds extra functionality to another function – without      modifying the original function's code.
# It's like giving your function a power-up! 🚀




def sty_deco(func):
    def wrapper():
        print("warapping it up in style")
        func()
        print("that was classy, wasn't it")
    return wrapper

@sty_deco
def say_hello():
    print("Hello!")

say_hello()