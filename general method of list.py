# append()
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

# extend()
nums = [1, 2]
nums.extend([3, 4])
print(nums)

# insert()
colors = ["red", "blue"]
colors.insert(1, "green")
print(colors)

# remove()
nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)

# pop()
stack = [1, 2, 3]
item = stack.pop()
print(item)
print(stack)

# clear()
data = [1, 2, 3]
data.clear()
print(data)

# index()
letters = ['a', 'b', 'c', 'b']
print(letters.index('b'))

# count()
nums = [1, 2, 2, 3]
print(nums.count(2))

# sort()
scores = [3, 1, 2]
scores.sort()
print(scores)

# sorted()
scores = [3, 1, 2]
new_scores = sorted(scores)
print(new_scores)
print(scores)

# reverse()
names = ['Alice', 'Bob', 'Charlie']
names.reverse()
print(names)

# copy()
a = [1, 2, 3]
b = a.copy()
print(b)

# 切片（slice）
nums = [10, 20, 30, 40, 50]
print(nums[1:4])
print(nums[::-1])
