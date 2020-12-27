num = 10
for i in range(10):
    print(" " * (num-i-1) + "*" * (2*i+1))

for n in range(int(num/2)):
    print(" " * int(num-num/4) + "*" * int(num/2))

print("")
print("txt" * 5)