user_input = input("enter the list of integer separated by spaces:")
results = []
for num in user_input.split():
         if int(num)>100:
                 results.append('over')
         else:
                  results.append(int(num))
print("modified list",results)