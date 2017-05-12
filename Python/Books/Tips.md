#### 1. 基本事项
##### 1.    Whitespace
*    http://www.python.org/dev/peps/pep-0008
*    4个空格键代替tab键
*    每行<= 79 字符
*    换行4空格缩进
*    同一文件中,函数或类用两个空行隔开
*    同一类中,函数用单个空行隔开
*    变量赋值前后只能有一个空格

##### 2.    Naming
*    函数,变量和属性用小驼峰
*    `protected instance attributes`用单下划线`_`前缀
*    `private instance attributes`用双下划线`__`前缀
*    `classes and exceptions` 首字母大写
*    模块级别的常量全大写
*    实例方法`instance methods`第一个参数是`self`
*    类方法`class methods`第一个参数是`cls`

##### 3.    Expressions and Statements
*    `if a is not b` inline negation
*    `if not somelist` 判断空数组或字符串时不要用长度表达式
*    `if somelist` 对非空列表或字符串为真, `l = []` 不能用 `if l is not None` 而用 `if l:`
*    `import some-module` 先导入模块
*    `from bar import foo` 只导入所需,且用绝对目录
*   代码检查[pylint](http://www.pylint.org/)
*   `a is b` 相当于 `id(a) == id(b)` 内存空间相同,不可重载
*   ` a == b` 相当于 `a.__eq__(b)` 内容是否相等,可重载
*   `i += 1 `不同于`++i`; `++i`和`--i`不同于自增自减,只是正负号

##### 4.    bytes, str and unicode
*    Python3中`bytes`是`raw 8-bit values`;`str`是`unicode characters`
*    Python2中`str`是`raw 8-bit values`;`unicode`是`unicode characters`
*    `encode` to convert unicode characters to binary data
*    `decode` to convert binary data to unicode characters

```
"""
Python3
"""
def to_str(input):
    if isinstance(input, bytes):
        value = input.decode('utf-8')
    else:
        value = input
    return value

def to_bytes(input):
    if isinstance(input, str):
        value = input.encode('utf-8')
    else:
        value = input
    return value
```

```
"""
Python2
"""
def to_unicode(input):
    if isinstance(input, str):
        value = input.decode('utf-8')
    else:
        value = input
    return value

def to_str(input):
    if isinstance(input, unicode):
        value = input.encode('utf-8')
    else:
        value = input
    return value
```

*   字符串连接用`join()` 优于 `+`
*   格式化字符串用`.format()` 优于 `%`

```
>>> s = ('SELECT * '
...      'FROM table '
...      'WHERE field="value"')
>>> s
'SELECT * FROM table WHERE field="value"'
```

##### 5.    unpacking
```
>>> a, b, *rest = range(10)
>>> a, *rest, b = range(10)
>>> *rest, a, b = range(10)

>>> with open("using_python_to_profit") as f:
        first, *_, last = f.readlines()

def f(*args):
    a, b, *args = args
    pass
```

##### 6.    yield from
```
def dup(n):
  for i in range(n):
      yield i
      yield i
      
def dup(n):
  for i in range(n):
      yield from [i, i]
```

##### 7.    asyncio
Uses new coroutine features and saved state of generators to do asynchronous IO.

```
"""
Taken from Guido's slides from “Tulip: Async I/O for Python 3
by Guido van Rossum, at LinkedIn, Mountain View, Jan 23, 2014
"""
@coroutine
def fetch(host, port):
  r,w = yield from open_connection(host,port)
  w.write(b'GET /HTTP/1.0\r\n\r\n ')
  while (yield from r.readline()).decode('latin-1').strip():
      pass
  body=yield from r.read()
  return body

@coroutine
def start():
  data = yield from fetch('python.org', 80)
  print(data.decode('utf-8'))
```

##### 8.    Standard Library
```
ipaddress
functools.lru_cache

from enum import Enum

from pathlib import Path

import ConfigParser

from collections import Counter

from copy import deepcopy

import argparse

```

##### 9.    Slice Sequences
```
a = ['a','b','c','d','e','f','g','h','i']
assert a[:4] == a[0:4]
assert a[-4:] == a[-4:len(a)]
a[3:-3]
a[::-1]

'''
copy
'''
b = a[:] 
assert b == a and b is not a

'''
same
'''
b = a
assert a is b


odds = a[::2]
evens = a[1::2]

from itertools import islice
```

*    Avoid using start, end and stride in a single slice
*    Avoid negative stride values if possible.

##### 10. 列式推导代替`map/filter`
```
[x**2 for x in alist]
map(lambda x: x^2, alist)

[x**2 for x in alist if x %2 == 0]
map(lambda x: x^2, filter(lambda x: x %2 == 0, alist))

{v: k fro k, v in adict}
{len(k) fro k in adict}
{len(k) fro k in aset}
```

##### 11. 列式推导中避免两个以上的表达式
```
[x for row in amatrix for x in row]
[[x^2 for x in row] for row in amatrix]
[x for x in alist if x > 4 and x % 2 == 0]
```

##### 12. 生成式代替大型列表推导
```
it = (len(x) for x in open('test.txt'))
print(next(it))
print(next(it))

roots = ((x, x**0.5) for x in it)
print(next(roots))
```

##### 13. `enumerate`胜过`range`
```
>>> alist = ['a','b','c','d','e','f','g','h','i']
>>> {idx: item for idx, item in enumerate(alist)}
{0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i'}
>>> {idx: item for idx, item in enumerate(alist, 5)}
{5: 'a', 6: 'b', 7: 'c', 8: 'd', 9: 'e', 10: 'f', 11: 'g', 12: 'h', 13: 'i'}
>>>
```

```
def enumerate(squence, start=0):
    n = start
    for elem in sequence:
        yield n, elem   # 666
        n += 1

# 反序号
def reversed_enumerate(squence):
    n = -1
    for elem in reversed(sequence):
        yield len(sequence) + n, elem
        n -= 1
```

##### 14.    ｀zip｀并行迭代
```
>>> alist = ['a','b','c','d','e','f','g','h','i']
>>> blist = [1,2,3]
>>> {a:b for a,b in zip(alist,blist)}
{'a': 1, 'c': 3, 'b': 2}
```


#### 2. 函数技巧
##### 15. 异常返回`None`
```
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

##### 16. 可变参数
```
def agenerator():
    for i in xrange(10):
        yield i
       
def afunc(*args):
    print(args)

it = agenerator()
afunc(*it)
afunc(1,2,3)
```

##### 17. keyword arguments默认参数即字典参数
```
def afunc(a, b, c=1):
    return a * b * c
```

##### 18. `None`及`Docstrings` 定制化动态默认参数
对参数是`mutable`的变量尤其重要(dict,list,{},[]).

```
def log(msg, when=None):
    """Log a message with a timestamp.
    
    Args:
        msg: Message to print.
        when: datetime of when the message occurred.
            Defaults to the pesent time.
    """
    when = datetime.now() if when is None else when
    print("%s:%s" % (when, msg))
```

##### 19. `with`上下文管理
```
with open('test.txt', 'w') as f:
    f.write('test')
    ... 
```

```
from contextlib import contextmanager

@contextmanager
def tag(name):
    print "<%s>" % name
    yield
    print "</%s>" % name

with tag("h1"):
    print "foo"
```

#### References
http://www.asmeurer.com/python3-presentation/slides.html#72
