num =12
# If given number is greater than 1
if num > 1:
for i in range(2, int(num/2)+1):
if (num % i) == 0:
print(num, "is not a prime number")
break
else:
print(num, "is a prime number")
break
else:
print(num, "is not a prime number")
