# 创建字符串
s1 = 'hello'
s2 = "world"
s3 = """multi
line"""             # 多行字符串
s4 = str(123)        # 转换为字符串

# 拼接字符串
s5 = s1 + ' ' + s2
print(s5)

# 重复字符串
print(s1 * 3)        # 输出 'hellohellohello'

# 获取长度
print(len(s1))

# 访问字符
print(s1[0])         # 第一个字符
print(s1[-1])        # 最后一个字符

# 字符串切片
print(s1[1:4])       # 索引1到3
print(s1[::-1])      # 反转字符串

# 遍历字符串
for char in s1:
    print(char)

# 成员判断
print('e' in s1)     # True
print('z' not in s1) # True

# 大小写转换
print(s1.upper())    # 全部大写
print(s1.lower())    # 全部小写
print(s1.capitalize())  # 首字母大写
print(s1.title())    # 每个单词首字母大写
print(s1.swapcase()) # 大小写互换

# 去除空白
s6 = "  hello  "
print(s6.strip())    # 去除首尾空格
print(s6.lstrip())   # 去除左侧空格
print(s6.rstrip())   # 去除右侧空格

# 查找和替换
print(s5.find('lo'))       # 查找子串索引
print(s5.rfind('o'))       # 从右开始查找
print(s5.index('lo'))      # 同 find，但找不到会报错
print(s5.replace('world', 'Python'))

# 拆分和连接
print(s5.split())          # 默认按空格分割
print('a,b,c'.split(','))  # 按逗号分割
print('-'.join(['1', '2', '3']))  # 用-连接

# 判断字符串内容
print(s1.isalpha())        # 是否全是字母
print("123".isdigit())     # 是否全是数字
print("abc123".isalnum())  # 是否是字母+数字
print("hello".islower())   # 是否全是小写
print("HELLO".isupper())   # 是否全是大写
print("   ".isspace())     # 是否全是空白字符

# 字符串格式化
name = "Tom"
age = 18
print("My name is {}, I'm {} years old.".format(name, age))
print(f"My name is {name}, I'm {age} years old.")  # f-string

# 判断前缀/后缀
print(s1.startswith('he'))  # 是否以'he'开头
print(s1.endswith('lo'))    # 是否以'lo'结尾

# 字符串比较
print("apple" < "banana")   # 字典序比较

# 编码与解码
s7 = "你好"
b = s7.encode('utf-8')      # 编码为字节
print(b)
print(b.decode('utf-8'))    # 解码为字符串

# 转义字符
print("Line1\nLine2")       # 换行
print("He said \"Hi\".")    # 转义引号
