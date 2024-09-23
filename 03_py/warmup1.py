'''
Tracy Ye
Loonch
SoftDev
K03 _py : Reviewing lists in python.
Time Spent: 30
'''

def monkey_trouble(a_smile, b_smile):
  if (a_smile == b_smile):
    return True
  return False

def sum_double(a, b):
  if a == b:
    return 4*a
  return a+b

def diff21(n):
  if n>21:
    return abs(n-21)*2
  return abs(n-21)

def parrot_trouble(talking, hour):
  if talking == True:
    if hour<7 or hour>20:
      return True
  return False

def makes10(a, b):
  if a==10 or b==10 or a+b == 10:
    return True
  return False
  
def near_hundred(n):
  if (n>=90 and n<=110) or (n>=190 and n <=210):
    return True
  return False

def pos_neg(a, b, negative):
  if negative == True and a < 0 and b < 0:
    return True
  elif negative == False and ((a<0 and b>0) or (a>0 and b<0)):
    return True
  return False

def not_string(str):
  if str[0:3] != "not":
    return "not " + str
  return str

def missing_char(str, n):
  return str[0:n] + str[n+1:]

def front_back(str):
  if len(str) <= 1:
    return str
  if len(str) == 2:
    return str[1]+str[0]
  else:
    return str[len(str)-1]+str[1:len(str)-1]+str[0]

def front3(str):
  if len(str) <= 3:
    return str *3
  else:
    return str[0:3] *3
