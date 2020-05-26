# a = '''hello
# world
# 哈哈哈哈'''
# print(a)

# b = """hello
# world
# 哈哈哈哈
# """
# print(b)


# 编写一个程序，判断用户输入的数是正数还是负数。

# while True:
#     a = int(input('输入：'))
#     if a > 0:
#         print('正数')
#     elif a == 0:
#         print('既不是正数也不说负数')
#     else:
#         print('负数')


# 10. 请按照以下要求完成编程。
# 要求如下：
# 1)接收用户输入的两个数字；
# 2)使用if-else语句比较它们的大小

# while True:
#     a = float(input('第一个数'))
#     b = float(input('第二个数'))
#     if a > b:
#         print('a大于b')
#     elif a < b:
#         print('a小于b')
#     elif a == b:
#         print('a=b')

# num1 = int(input('输入：'))
# calculate = ['+','-','*','/']
# num2 = int(input('输入：'))

# if num1 != 0 and num2 != 0:
#     if calculate == '+':
#         print(num1 + num2)

#     print(num1 + num2)
    
#     # print(num1+calculate[0]+num2)


# i = 0
# sum = 0
# while i<=10:
#     sum += i
#     i += 1
# print(sum)

# i = 0
# sum = 0
# while i<101:
#     if i%2 == 1:
#         sum += i
#     i += 1
#     print(sum)

# i = 1
# while i < 6:
#     j = 0
#     while j<i:
#         print('*',end='')
#         j+=1
#     print('')
#     i += 1
# i=5
# while i>0:
#     j=0
#     while j<i:
#         print('*',end='')
#         j+=1
    
#     print('')
#     i -= 1


# i = 1
# while i<=9:
#     j = 1
#     while j<=i:
#         print("%d * %d = %d"%(i,j,i*j),end='\t')
#         j+=1
#     i+=1
#     print('')

# dict1 = {"name":"xioaming","age":"18"}
# for key in dict1:
#     print(key+"的值是："+dict1[key])

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d * %d = %d"%(i,j,i*j),end='\t')
#     print('')

# 所有整数和
# sum =0
# for i in range(0,101):
#     sum += i
#     i += 1
# print(sum)

# 奇数
# sum =0
# for i in range(0,101):
#     if i % 2 == 1:
#         sum += i
#         i += 1
# print(sum)


# 偶数
# sum =0
# for i in range(0,101):
#     if i % 2 == 0:
#         sum += i
#         i += 1
# print(sum)

# for i in range(10):
#     print('----')
#     if i == 5:
#         break
#     print(i)
# print('程序结束')

for i in range(10):
    print('----')
    if i == 5:
        continue
    print(i)
print('程序结束')

