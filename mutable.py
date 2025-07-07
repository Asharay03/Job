# var1=[1,2,3,"4",'5','abc',True,False,None,(1,2,3),{1,2,3}]
# for i in var1:
#  print(type(i))


# a=10
# b=20
# c=b/a
# if c%1==0:
#  print(c) 

# s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# for i in s:
#     if(i%3==0):
#         print('Divisible by 3')
#     else:
#         print("Not Divisible by 3")

# a=10
# b=5
# c=a%b
# print(c)

# a=[1,2,3]
# b=a
# b.append(4)
# c=b
# c.append(5)
# print(a)

# a=10
# d=50
# print(a+d)

# d1 = {"name": 'a', 2: 'b', 3: 'c' ,True: 'd', False: 'e', None: 'f'}
# print(d1[1])
# print("Enter your temperature")
# avg_temp=0
# total_temp=[]
# for i in range(5):
#     temperature=int(input("Enter your temperature = "))
#     temp=int(temperature)
#     if temp>= 45 and temp<= 100:
#         print("Very Hot")
#     elif temp>= 40 and temp< 45:
#         print("Hot")
#     elif temp>= 30 and temp< 40:
#         print("Normal")
#     elif temp>= 20 and temp< 30:
#         print("Cold")    
#     else:
#         print("Very Cold")  
#     total_temp.append(temp)
# for i in range(5):
#     avg_temp=int(avg_temp+total_temp[i])
# print("Average temperature recorded:", avg_temp/5)
# maxtemp=0
# for i in range(5):
#     maxtemp=int(max(total_temp))
# print("Maximum temperature recorded:", maxtemp)

# total=0
# numbers = []
# for i in range(5):
#     user_input = input("Enter a number (or type 'done'): ")
#     if user_input.lower() == 'done':
#         break
#     try:
#         number = int(user_input)
#         numbers.append(number)
#     except ValueError:
#         print("Invalid input. Please enter a valid number or 'done'.")
# for i in range(5):
#     total=int(total+numbers[i])
# print("Numbers entered:", total/5)

# t=(True,1,2,3,4)
# print(t.count(True))

# strings=["ABCD","BCDA","ABCD","DABC"]
# for i in range(0,3):
#  for j in range(0,4):
#   if(strings[i][j]==strings[i+1][j]):
#     print(strings[i][j])

# s=[1,2,3,4,5]
# for i in range(4, -1, -1):
#    print(s[i])

a={1}
print(type(a))