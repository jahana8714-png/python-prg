list_1 = input("Enter the first list of integers (separated by comma): ")
list_2 = input("Enter the second list of integers (separated by comma): ")

list1 = [int(x) for x in list_1.split(',')]
list2 = [int(x) for x in list_2.split(',')]

if len(list1) == len(list2):
    print("The lists are the same length:", len(list1))
else:
    print("The lists are not the same length")
print("The sum of elements of list1:", sum(list1))
print("The sum of elements of list2:", sum(list2))

if sum(list1) == sum(list2):
    print("The sums of the lists are the same")
else:
    print("The sums of the lists are not the same")

common = []

for value in list1:
    if value in list2:
        common.append(value)

if common:
    print("The common values in both lists:", common)
else:
    print("No common values found in both lists")
