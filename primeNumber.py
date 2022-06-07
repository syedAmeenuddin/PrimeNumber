# primeNumber Logic => divisible by its own and by 1

# To check the number is prime or not
number=int(input("check prime or number"))
flag1=False
for i in range(2,number):
  if (number%i)==0:
    flag1 = True
if flag1=False:
  print(f'{number} is an Prime Number')
else:
  print(f'{number} is not an Prime Number')
  
  
 
# code for n th prime number. in my case i need 100th prime number
check_nth_number=int(input("enter the nth number"))
num=0
count=0
flag2=False
while count!=check_nth_number+1:
    num+=1
    flag2=False
    for i in range(2,num):
        if (num%i)==0:
            flag2=True            
    if flag2==False:
        print(f'{num} Its an prime Number')
        count+=1
    if count==check_nth_number:
        print(f'{num} is an {count}th prime Number')
        break
