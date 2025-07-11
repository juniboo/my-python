# 创建字典
d1 = {'name': 'Alice', 'age': 25}
d2 = dict(name='Bob', age=30)
d3 = dict([('a', 1), ('b', 2)])
d4 = {}  # 空字典

# 访问值
print(d1['name'])         # 通过键访问值
# print(d1['gender'])     # 如果键不存在会报错
print(d1.get('gender'))   # 不存在返回 None
print(d1.get('gender', 'unknown'))  # 不存在返回默认值

# 修改/添加键值对
d1['age'] = 26            # 修改已有值
d1['gender'] = 'female'   # 添加新键值对

# 删除元素
del d1['gender']          # 删除指定键
# d1.pop('gender')        # 也可用 pop 删除并返回值
d1.pop('age')             # 删除并返回对应值
print(d1)

# 清空字典
d1.clear()

# 删除整个字典
# del d1

# 遍历字典
d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
    print(k, d[k])        # 遍历键和值

for k, v in d.items():
    print(k, v)           # 遍历键值对

# 遍历键
print(list(d.keys()))

# 遍历值
print(list(d.values()))

# 获取所有键值对
print(list(d.items()))

# 判断键是否存在
print('a' in d)           # True
print('z' not in d)       # True

# 字典合并
d1 = {'x': 1, 'y': 2}
d2 = {'y': 100, 'z': 3}
d3 = {**d1, **d2}         # Python 3.5+ 的合并方式
print(d3)

d1.update(d2)             # 用 d2 更新 d1
print(d1)

# 设置默认值
d = {}
d.setdefault('score', 0)  # 如果没有该键则添加，并设默认值
print(d)

# 字典推导式
squares = {x: x**2 for x in range(5)}
print(squares)

# 嵌套字典
people = {
    'alice': {'age': 25, 'city': 'Beijing'},
    'bob': {'age': 30, 'city': 'Shanghai'}
}
print(people['alice']['city'])

# 从Keys创建默认值字典
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)

# 排序字典（按key）
for k in sorted(d3):
    print(k, d3[k])
