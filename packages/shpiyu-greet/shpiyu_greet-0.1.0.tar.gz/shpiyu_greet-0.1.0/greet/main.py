import random

_messages = (
    "Hello, have a nice day!",
    "Welcome to the world of Python!",
    "We're glad you are here!",
    "Have an amazing day!",
)


def get_messages():
    return _messages[:]


def greet():
    return _messages[random.randint(0, len(_messages) - 1)]
