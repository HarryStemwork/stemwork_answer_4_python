def GCD(num1,num2):
    gcd = 1
    n = 2
    while n <= n1 and n <= n2:
      if n1 % n == 0 and n2 % n == 0:
        gcd = n
      n += 1
    return gcd

n1,n2 = eval(input("Please enter two numbers: "))
print(f"The Greatest Common Number is {GCD(n1,n2)}")
