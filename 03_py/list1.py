'''
Tracy Ye
Loonch
SoftDev
K03 _py : Reviewing lists in python.
Time Spent: 30 mins
'''

def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] ==6:
    return True
  return False

def same_first_last(nums):
  if len(nums) > 0 and nums[0] == nums[len(nums)-1]:
    return True
  return False

def make_pi():
 pi = [3, 1, 4]
 return pi

def common_end(a, b):
  if (a[0] == b[0] or a[len(a)-1] == b[len(b)-1]):
    return True
  return False

def sum3(nums):
  sum = 0
  for i in nums:
    sum += i
  return sum

def rotate_left3(nums):
  newList = [nums[1]] + nums[2:len(nums)] + [nums[0]]
  return newList

def reverse3(nums):
  return nums[::-1]

def max_end3(nums):
  x = max(nums[0], nums[len(nums)-1])
  ret = []
  for i in nums:
    ret += [x]
  return ret

def sum2(nums):
  if len(nums) >= 2:
    return nums[0]+nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0

def middle_way(a, b):
  l = [a[1], b[1]]
  return l

def make_ends(nums):
  return [nums[0], nums[len(nums)-1]]

def has23(nums):
  for i in nums:
    if i == 2 or i == 3:
      return True
  return False

