# list1=[1,2,3,4,5,23,-23,100]
# sum=0
# count=0
# for i in list1:
#     sum=sum+i
#     count+=1
# print(sum)
# if count==0:
#     print("empty list")
# else:
#     print(sum/count)

# list2=[[1,2,3,4],[5,23],[-23,100,34],[3,4,5,6]]
# sum=0
# for i in list2:
#     # print(i)
#     for j in i:
#         # print(j)
#         sum=sum+j
# print(sum)
    
# function

# print("started")
# print(4/3*3.14*10*10*10)
# print("ended")

# print("started")
# print(4/3*3.14*20*20*20)
# print("ended")

# print("started")
# print(4/3*3.14*30*30*30)
# print("ended")

#we have to write every time in change of radius

# using function

# def calc_volume(r):
#     print("started")
#     print(4/3*3.14*r*r*r)
#     print("ended")

# calc_volume(20)
# # calc_volume(30)

# def calc_volume(r,pie):
#     print("started")
#     print(4/3*3.14*r*r*r)
#     print("ended")

# calc_volume(20,23)

# def calc_volume(r,pie=3.14):
#     print(pie)
#     print(4/3*3.14*r*r*r)  
# calc_volume(20,23)
# calc_volume(10)

# defalut paramenter should be at last only any time
#funtion with return callled as normal

# def calc_volume(r,pie=3.14):
#     print(pie)
#     return (4/3)*3.14*r*r*r
# result =calc_volume(20,23)
# print(result)

# def sum(a,b):
#     return a+b
# print(sum(3,5))

def sum(a,b,*c):
    print(type(c))
    sum=a+b
    for i in c:
        sum=sum+i
    return sum
print(sum(3,5,3,4,5,6,8,8,6,8))

