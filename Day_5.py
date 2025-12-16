def calculate_total(exp):
    total=0
    for item in exp:
        total+=item
    return total
tom_exp_list=[2100,3400,3500]

joe_exp_list=[200,500,700]

toms_total=calculate_total(tom_exp_list)
joe_total=calculate_total(joe_exp_list)

print("Toms total expesnse",toms_total)
print("Joes total expense ",joe_total)
total=0
for item in tom_exp_list:
    total+=item
print("Toms total expense:",total)

total=0
for item in joe_exp_list:
    total+=item
print("Joes total expense",total)
def sum(a,b):
    total=a+b
    return total

n=sum(5,6)
print("Total",n)
