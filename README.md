# 🎉 Python Decorators - Explained the Fun Way! 🍔☕

Welcome to this beginner-friendly and fun explanation of **Python Decorators**!  
If you've ever wondered what decorators are and how they work, think of this as your cheat sheet wrapped in humor, chai, and burger combos! 😄

---

## 📌 What is a Decorator?

A **decorator** in Python is a function that adds extra features or behavior to another function **without changing its original code**.

Think of it like:

- **Plain Chai 🫖** → Your normal function  
- **Chai on a Tray with Biscuits 🍪** → Your decorated function

You're not changing the chai... you're just upgrading the experience!

---

## 🎬 Code Examples

### 1. Basic Decorator

```python
def stylish_decorator(func):
    def wrapper():
        print("👔 Wrapping it up in style!")
        func()
        print("👞 That was classy, wasn’t it?")
    return wrapper

@stylish_decorator
def say_hello():
    print("Hello!")

say_hello()
