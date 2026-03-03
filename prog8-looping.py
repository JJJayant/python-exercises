
names=['Jayant', 'Nikita', 'Satyarth', 'Anshul', 'Shivam']
for i in names:
    print(i)
    for j in i:
        print(j)

print("\n")
for k in range(3,10,2):
    print(k)

print("\n")
l=int(input("Enter a number less than 13: "))
while(l<13):
    print(l*2)
    l+=1
else:
    print("The number is now greater than or equal to 13")

for i in range(12):
    if(i ==7):
        continue
    if(i ==10):
        break
    print("5 X", i+1, "=", 5*(i+1))
print("Loop ko chodkar nikal gaya")

#There is no do-while loop in Python but we can achieve the same functionality using a while loop
m=0
while True:
    print(m)
    m+=1
    if(m>=5):
        break
