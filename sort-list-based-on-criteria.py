#Write a function that calculates the nth Fibonacci number in O(n) time or better without using any "for" or "while" loops.
#(Feel free to use the space below or submit a link to your work.)
#- You can use any programming language you like.
#- The function you submit shall be runnable.*

def recur_fibo(n):
 if n <= 1:
  return n 
 else:
  return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
 print("Please enter a positive integer")
else:
  print("nth number of Fibonacci sequence is: " + str(recur_fibo(nterms)))

# Write an immutable function that merges the following inputs into a single list. (Feel free to use the space below or submit a link to your work.)
#Inputs
#- Original list of strings
#- List of strings to be added
#- List of strings to be removed
#Return
#- List shall only contain unique values
#- List shall be ordered as follows
#--- Most character count to least character count
#--- In the event of a tie, reverse alphabetical
#Other Notes
#- You can use any programming language you like
#- The function you submit shall be runnable
#For example:


originalList = ['one', 'two', 'three',]
addList = ['one', 'two', 'five', 'six']
deleteList = ['two', 'five']
#Result List = ['three', 'six', 'one']*

def mergeInput(originalList, addList, deleteList):
  resultList = [x for x in originalList]
  
  for i in range(len(addList)):
      if addList[i] not in originalList:
          resultList.append(addList[i])
  print(resultList)
  for i in  range(len(deleteList)):
    while deleteList[i] in resultList:
      resultList.remove(deleteList[i])
  print(resultList)
  resultList.sort(key=lambda item: (len(item),item), reverse=True)
  return resultList

print(mergeInput(originalList, addList, deleteList))