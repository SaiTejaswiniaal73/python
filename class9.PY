# for i in range(1,11):#class
#     if i==7:
#         continue
#     for j in range(1,5):#roll numbers
#         print(i,j)

# for i in range(1,11):#class
   
#     for j in range(1,5):#roll numbers
#             if i==7:
#                 continue
#             print(i,j)

# for i in range(1,11):#class
#     for j in range(1,11):#roll numbers
#             if (i==7  or i==8) and j>4:
#                 continue
#             print(i,j)

count=0
i=0
while i<10:
    print(i)
    if i==7:
        i=i+1
        continue
    i=i+1
    j=1
    while j<31:
        print(i,j)
        j+=1
    print(j)