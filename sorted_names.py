names=[]
print("Enter names one by one. Type'done' to finish:")
while True:
    name=input("Enter a name:").strip()
    if name.lower() == 'done':
        break
    if name!="":
        names.append(name)

print(f"\nTotal number of names entered:{len(names)}")
unique_sorted = sorted(set(names))
print("Final sorted list without duplicates:")
for n in unique_sorted:
    print(n)
