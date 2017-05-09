#### 基本
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
*    `if somelist` 对非空列表或字符串为真
*    `import some-module` 先导入模块
*    `from bar import foo` 只导入所需,且用绝对目录
*    代码检查[pylint](http://www.pylint.org/)

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
