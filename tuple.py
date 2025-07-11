# 创建元组
t1 = (1, 2, 3)
t2 = 4, 5, 6           # 小括号可省略
t3 = tuple([7, 8])     # 从列表创建
t4 = ()                # 空元组
t5 = (5,)              # 单元素元组必须加逗号

# 访问元素
print(t1[0])           # 访问第一个元素
print(t1[-1])          # 访问最后一个元素

# 切片操作
print(t1[1:3])         # 切片获取子元组
print(t1[:2])          # 从开头切到索引1
print(t1[::-1])        # 反转元组

# 遍历元组
for item in t2:
    print(item)

# 成员判断
print(2 in t1)         # 元素是否存在
print(9 not in t1)     # 元素是否不存在

# 拼接元组
t6 = t1 + t2
print(t6)

# 重复元组
print(t1 * 2)          # 元组重复两次

# 获取长度
print(len(t6))

# 元素计数
print(t6.count(2))     # 统计2出现次数

# 查找索引
print(t6.index(3))     # 获取3的索引位置

# 嵌套元组
t_nested = ((1, 2), (3, 4))
print(t_nested[1][0])  # 访问嵌套元素

# 元组解包
a, b, c = t1
print(a, b, c)

# 星号解包
t7 = (10, 20, 30, 40, 50)
x, *y, z = t7
print(x)               # 10
print(y)               # [20, 30, 40]
print(z)               # 50

# 使用enumerate
for i, val in enumerate(t2):
    print(i, val)

# 元组作为字典key
d = {(1, 2): "point"}
print(d[(1, 2)])

# 元组不可变特性
# t1[0] = 99  # 会报错，元组不支持修改
