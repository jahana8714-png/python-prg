numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

positive = [x for x in numbers if x > 0]

print("Positive numbers:", positive)




n = int (input ("enter N :") )
number = [ int (input ("enter number :")) for i in range (n) ]
squares = [ x * x for x in number]
print("squares:", squares) 

word = input ("enter a word ")
vowels = [ ch for ch in word if ch.lower() in "aeiou"]
print ("vowels:",vowels)

word = input ("enter a word:")
values = [ord (ch)  for ch in word]
print ("ordinal values:", values)