# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.data):
#             curr_index = self.index
#             self.index += 1
#             return self.data[curr_index]
#         else:
#             raise StopIteration
#
#
# my_iterator = MyIterator([1, 2, 3, 4, 5])


# def even_range(start, end):
#     current = start
#     while current < end:
#         if current % 2 == 0:
#             yield current
#         current += 1
#
#
# # 使用生成器产生偶数
# even_nums = even_range(0, 10)
#
# # 逐个获取生成器产生的值
# print(next(even_nums))  # 输出: 0
# print(next(even_nums))  # 输出: 2
# print(next(even_nums))  # 输出: 4
# print(next(even_nums))  # 输出: 6
# print(next(even_nums))  # 输出: 8

# import time
#
# def calculate_time(func):
#     def wrapper():
#         start_time = time.time()
#         func()  # 调用被修饰的函数
#         end_time = time.time()
#         print("运行时间: ", end_time - start_time, "秒")
#     return wrapper
#
# @calculate_time
# def my_function():
#     time.sleep(1)  # 模拟函数执行的耗时操作
#
# my_function()

# # 创建一个包含1到10的平方的列表
# squares = [x**2 for x in range(1, 11)]
# print(squares)
#
# # 创建一个包含1到10的平方的集合
# squares = {x**2 for x in range(1, 11)}
# print(squares)
#
# # 创建一个字典，键为1到5的数字，值为该数的平方
# squares = {x: x**2 for x in range(1, 6)}
# print(squares)

# import copy
#
# # 原对象
# original_list = [1, 2, [3, 4]]
#
# # 浅拷贝
# shallow_copy = copy.copy(original_list)
#
# # 深拷贝
# deep_copy = copy.deepcopy(original_list)
#
# # 修改原对象中的可变对象
# original_list[2].append(5)
#
# # 输出结果
# print("原对象: ", original_list)
# print("浅拷贝: ", shallow_copy)
# print("深拷贝: ", deep_copy)


import threading

# 定义一个函数作为线程的执行任务
def print_numbers():
    for i in range(1, 6):
        print(i)

# 创建线程对象
thread1 = threading.Thread(target=print_numbers)

# 启动线程
thread1.start()

# 主线程继续执行其他任务
for i in range(6, 11):
    print(i)

# 等待线程执行完毕
thread1.join()