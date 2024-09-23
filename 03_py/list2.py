'''
Tracy Ye
Loonch
SoftDev
K03 _py : Reviewing lists in python.
Time Spent: 30
'''

def count_evens(nums):
  cnt = 0
  for i in nums:
    if i%2 == 0:
      cnt+=1
  return cnt

def big_diff(nums):
  min = nums[0]
  max = nums[0]
  for i in nums:
    if i < min:
      min = i
    if i > max:
      max = i
  return max - min

def centered_average(nums):
  nums.sort()
  return sum(nums[1:len(nums)-1])/(len(nums)-2)

def sum13(nums):
  sum = 0
  i = 0
  while i <= len(nums)-1:
    if nums[i] == 13:
      i+=2
    else:
      sum+=nums[i]
      i+=1
  return sum

def sum67(nums):
  sum = 0
  i = 0
  skip = False
  while i <= len(nums)-1:
    if skip == False:
      if nums[i] != 6:
        sum+=nums[i]
      else:
        skip = True
    else:
      if nums[i] == 7:
        skip = False
    i+=1
  return sum
      
def has22(nums):
  i = 0;
  is2 = False
  while i <= len(nums)-1:
    if is2 == False:
      if nums[i] == 2:
        is2 = True
    else:
      if nums[i] == 2:
        return True
      else:
        is2 = False
    i+=1
  return False