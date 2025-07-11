# 通用数据容器：list, tuple, str, dict, set

# ✅ 1. len() 获取长度
print(len([1, 2, 3]))
print(len((1, 2, 3)))
print(len("abc"))
print(len({'a': 1, 'b': 2}))
print(len({1, 2, 3}))

# ✅ 2. in / not in 判断成员
print(2 in [1, 2, 3])
print('a' in "cat")
print('b' in {'a': 1, 'b': 2})  # 对字典是查key
print(3 not in {1, 2, 4})

# ✅ 3. 遍历容器
for item in [1, 2, 3]:
    print(item)

for ch in "hello":
    print(ch)

for key in {'x': 1, 'y': 2}:
    print(key)

for k, v in {'x': 1, 'y': 2}.items():
    print(k, v)

for item in {9, 8, 7}:
    print(item)

# ✅ 4. max() / min()
print(max([3, 5, 1]))
print(min("hello"))
print(max({3, 1, 7}))
print(max({'a': 1, 'c': 3}))  # 默认比较 key

# ✅ 5. sum() 适用于数字容器
print(sum([1, 2, 3]))
print(sum((4, 5, 6)))
# print(sum("123"))  # 字符串不能直接 sum

# ✅ 6. sorted() 排序（不改变原对象）
print(sorted([3, 1, 2]))           # [1, 2, 3]
print(sorted("cba"))              # ['a', 'b', 'c']
print(sorted({'b': 2, 'a': 1}))    # ['a', 'b'] (按key)

# ✅ 7. reversed() 反转（返回迭代器）
print(list(reversed([1, 2, 3])))
print(''.join(reversed("abc")))   # cba

# ✅ 8. enumerate() 获取索引和值
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)

# ✅ 9. zip() 同时遍历多个容器
a = [1, 2, 3]
b = ['x', 'y', 'z']
for i, j in zip(a, b):
    print(i, j)

# ✅ 10. any() / all()
print(any([0, 0, 1]))     # 只要有一个为真就为True
print(all([1, 2, 3]))     # 所有为真才为True
print(all([]))            # 空容器返回True（约定俗成）

# ✅ 11. 类型转换
print(list("abc"))       # ['a', 'b', 'c']
print(tuple([1, 2]))     # (1, 2)
print(set([1, 2, 2]))     # {1, 2}
print(dict([('a', 1), ('b', 2)]))

# ✅ 12. 容器的等值比较（结构与内容都相等）
print([1, 2] == [1, 2])       # True
print((1, 2) == (1, 2))       # True
print({'a': 1} == {'a': 1})   # True
print({1, 2} == {2, 1})       # True（集合无序）

# ✅ 13. map() 和 filter()（常用于字符串、列表、元组）
print(list(map(str.upper, ['apple', 'banana'])))  # ['APPLE', 'BANANA']
print(list(filter(lambda x: x > 2, [1, 2, 3, 4]))) # [3, 4]

# ✅ 14. unpacking 解包
a, b, c = [1, 2, 3]
x, *y = "abcd"         # x='a', y=['b', 'c', 'd']
print(x, y)
