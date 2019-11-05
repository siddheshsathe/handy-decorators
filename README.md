[![Build Status](https://travis-ci.org/siddheshsathe/handy-decorators.svg?branch=master)](https://travis-ci.org/siddheshsathe/handy-decorators)
---
# Handy Decorators
---
This is a set of `handy decorators` which one can use for their day-to-day life coding.

## Installation Method
Install it via pip
```bash
pip install handy-decorators
```

## Description
The set of decorators contain some daily needed decorators for being used in our day to day coding life. This has following set of decorators.

### trycatch
This decorator surounds your function with a `try-except` block and if your code/function raises an exception, it's caught by this decorator and reported by logging.
```python
>>> from decorators import trycatch
>>> @trycatch
... def func():
...     print(0/0) # Division by 0 must raise exception
...
>>> func()
Exception occurred: [integer division or modulo by zero]
>>>
```

### timer
This decorator will calculate a time required in seconds by your function for execution.
```python
>>> from decorators import timer
>>> @timer
... def a():
...     import time
...     print('Hi')
...     time.sleep(1)
...
>>> a()
Hi
Time taken by the function is [1.00103902817] sec
>>>
```

### singleton
This decorator is for making your class [`singleton`](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html).
<br>
The features given by this decorator are:
* If instances of same class are created with **same** args and kwargs, decorator will return previously existing instance
* If instances of same class are created with **different** args and kwargs, decorator will create a different one for you and store the newly created instance

```python
>>> from decorators import singleton
>>>
>>> @singleton
... class A:
...     def __init__(self, *args, **kwargs):
...         pass
...
>>>
>>> a = A(name='Siddhesh')
>>> b = A(name='Siddhesh', lname='Sathe')
>>> c = A(name='Siddhesh', lname='Sathe')
>>> a is b  # has to be different
False
>>> b is c  # has to be same
True
>>>
```

### create_n_threads
This decorator launches the function/method call in number of threads mentioned.

```python
>>> from decorators import create_n_threads
>>> @create_n_threads(thread_count=2)
... def p(*args, **kwargs):
...     pass
...
>>> p()
Thread started for function <function p at 0x7f6725ecccf8>
Thread started for function <function p at 0x7f6725ecccf8>
>>>
```

### run_in_thread
This decorator launches the function/method call in a separate thread.
* Using standard threading.Thread for creating thread
* Can pass args and kwargs to the function
* Will start a thread but will give no control over it
```
>>> from decorators import run_in_thread
>>> @run_in_thread
... def display(name, *args, **kwargs):
...     for i in range(5):
...             print('Printing {} from thread'.format(name))
...
>>> display('Siddhesh')
Printing ('Siddhesh',) from thread
Thread started for function <function display at 0x7f1d60f7cb90>
Printing ('Siddhesh',) from thread
Printing ('Siddhesh',) from thread
Printing ('Siddhesh',) from thread
Printing ('Siddhesh',) from thread
>>>
```

---
Please create an issue if more decorators are needed.
