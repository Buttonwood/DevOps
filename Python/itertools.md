#### [迭代器](https://docs.python.org/3/library/itertools.html#itertools.starmap)
1.	Lazy evaluation 惰性求值
2.	适合遍历大文件和集合,省内存

##### 1. 无限迭代器
```
count(firstval=0, step=1)
cycle(iterable)
repeat(object[,times])

import itertools
nums = itertools.count(10, 2)
cycle_strings = itertools.cycle('ABC')
[item for item in itertools.repeat('hello world', 3)]
[item for item in itertools.repeat([1, 2, 3, 4], 3)]
```

##### 2. 有限迭代器
```
// 接收多个可迭代对象作为参数，将它们『连接』起来，作为一个新的迭代器返回
chain(iterable1, iterable2, iterable3, ...)
[item for item in itertools.chain([1, 2, 3, 4], ['a', 'b', 'c'])]
string = chain.from_iterable('ABCD')

// 用于对数据进行筛选，当 selectors 的某个元素为 true 时，则保留 data 对应位置的元素，否则去除
compress(data, selectors)
list(itertools.compress('ABCDEF', [1, 1, 0, 1, 0, 1]))
list(itertools.compress('ABCDEF', [True, False, True]))

//predicate 是函数，iterable 是可迭代对象。对于 iterable 中的元素，如果 predicate(item) 为 true，则丢弃该元素，否则返回该项及所有后续项
dropwhile(predicate, iterable)

>>> from itertools import dropwhile
>>> list(dropwhile(lambda x: x < 5, [1, 3, 6, 2, 1]))
[6, 2, 1]
>>> list(dropwhile(lambda x: x > 3, [2, 1, 6, 5, 4]))
[2, 1, 6, 5, 4]

// iterable 是一个可迭代对象，keyfunc 是分组函数，用于对 iterable 的连续项进行分组，如果不指定，则默认对 iterable 中的连续相同项进行分组，返回一个 (key, sub-iterator) 的迭代器。
groupby(iterable[, keyfunc])
>>> from itertools import groupby
>>> for key, value_iter in groupby('aaabbbaaccd'):
...     print key, ':', list(value_iter)

// 使用 len 函数作为分组函数
>>> data = ['a', 'bb', 'ccc', 'dd', 'eee', 'f']
>>> for key, value_iter in groupby(data, len):
...     print key, ':', list(value_iter)


// 将 iterable 中 function(item) 为 True 的元素组成一个迭代器返回，如果 function 是 None，则返回 iterable 中所有计算为 True 的项。
ifilter(function or None, sequence)
>>> from itertools import ifilter
>>>
>>> list(ifilter(lambda x: x < 6, range(10)))
[0, 1, 2, 3, 4, 5]
>>>
>>> list(ifilter(None, [0, 1, 2, 0, 3, 4]))
[1, 2, 3, 4]

// ifilterfalse 的使用形式和 ifilter 类似，它将 iterable 中 function(item) 为 False 的元素组成一个迭代器返回，如果 function 是 None，则返回 iterable 中所有计算为 False 的项。
ifilterfalse
>>> from itertools import ifilterfalse
>>>
>>> list(ifilterfalse(lambda x: x < 6, range(10)))
[6, 7, 8, 9]
>>>
>>> list(ifilter(None, [0, 1, 2, 0, 3, 4]))
[0, 0]
```
