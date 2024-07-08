num = 3

for j in range(2,101):
    if all(j%i !=0 for i in range(2,j)):
        print(f"{j} prime num")
    else:
        print(f"{j} is not a prime num")