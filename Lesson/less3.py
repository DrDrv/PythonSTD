# def f(x):
#     return x**2

# g = f
# print(type(f))
# print(g(1))

# def calc1(x):
#     return x+10
# def calc2(x):
#     return x*10

# # # print(calc(10))
# # # print(calc1(10))

# # def math(op, x):
# #     print(op(x))

# # math(calc2,10)
# # math(calc1,10)

# # def sum(x,y):
# #     return x+y

# summ = lambda x, y: x+y

# def mylt(x,y):
#     return x*y

# def calc(op, a, b):
#     print(op(a,b))
#     return

# calc(summ, 4,5)

################ 
# Списки

# list = []
# for i in range(1,101):
#     if( i%2 ==0):
#         list.append(i)
# print(list)
# list = [i for i in range(1, 101) if i % 2 == 0]
# print(list)

# list = [(i,i) for i in range(1, 101) if i % 2 == 0]
# print(list)

# from ast import Lambda


# list_in = (1,2,3,5,8,15,23,38)
# def f(x):
#     return x**2

# list_out = [(i,f(i)) for i in list_in if i % 2 == 0]
# print(list_out)

# # MAP

# li = [x for x in range(1,20)]
# print(li)
# li = list(map(lambda x:x+10, li))
# print(li)
