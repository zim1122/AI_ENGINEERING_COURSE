exp =[2340,2500,2100,3100,2980]
total=0
for item in exp:
    total=total+item
print(total)
for i in range(1,11):
    print(i*i)
for i in range(len(exp)):
    print('Month:',(i+1),'Expense:',exp[i])
    total=total+exp[i]
    
    print('Total expense is:',total)
    print(len(exp))
key_location="dyning"
location=["garage","reading room","dyning","closet"]
for i in location:
    if i==key_location:
        print("key is found in :",i)
        break
else:
        print("key is not found")

for i in range(2,14):
    if i%2==1:
        continue
    print(i)

i=1
while i<=5:
    print(i)
    i=i+1


        

    
    




