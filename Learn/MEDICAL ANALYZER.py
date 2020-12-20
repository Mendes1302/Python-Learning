bigger = smaller = 0
response = 'Y'
person = list()
people = list()

while True:
    person.append(str(input("\nWhat is first name of person? ")))
    person.append(int(input("\nWhat is the person's weight [Kg]? ")))
    people.append(person[:])
    person.clear()
    
    response = str(input("\nDo you wish to continue [Y/N]: "))
    if response.upper() in 'N':
        break
    else:
        if response.upper() != 'Y':
            print('\n\033[1;31mCommand error!! try again\033[0;0m')
            
for i, k in enumerate(people):
    if i == 0:
        bigger = smaller = k[1]
    elif k[1] >= bigger:
        bigger = k[1]
    elif k[1] <= smaller:
        smaller = k[1]

print(f"\nIt has a total of {len(people)} people.")
print(f"The greatest weight was {bigger} Kg ", end='')

for b in people:
    if b[1] == bigger:
        print(f"being the {b[0]}.")
        break
    
print(f"The lowest weight was {smaller} Kg", end='')
for b in people:
    if b[1] == smaller:
        print(f" being the {b[0]}.")
        break
