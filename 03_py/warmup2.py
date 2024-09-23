'''
Tracy Ye
Loonch
SoftDev
K03 _py : Reviewing lists in python.
Time Spent: 30
'''

def string_times(str, n):
  return str*n

def front_times(str, n):
  if len(str) <= 3:
    return str*n
  else:
    return str[:3]*n

def string_bits(str):
  x = True
  ret = ""
  for i in str:
    if x == True:
      ret+=i
      x = False
    elif x == False:
      x = True
  return ret

def string_splosion(str):
  ret = ""
  i = 0
  while i <= len(str):
    ret += str[:i]
    i+=1
  return ret

def last2(str):
  cnt = 0
  i = 0
  while i <= len(str)-3:
    if str[i:i+2] == str[-2:]:
      cnt+=1
    i+=1
  return cnt

def array_count9(nums):
  cnt = 0
  for i in nums:
    if i == 9:
      cnt+=1
  return cnt

def array_front9(nums):
  i = 0
  while i <= min(3, len(nums)-1):
    if nums[i] == 9:
      return True
    i+=1
  return False

def array123(nums):
  i = 0
  while i < len(nums)-2:
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
    i +=1
  return False

def string_match(a, b):
  cnt = 0
  i = 0
  while i < min(len(a), len(b))-1:
    if a[i:i+2] == b[i:i+2]:
      cnt+=1
    i+=1
  return cnt