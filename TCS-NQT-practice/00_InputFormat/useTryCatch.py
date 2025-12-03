x = input()
try:
  x = 9/0
except Exception as e:
  raise ZeroDivisionError(str(type(x))+ "" + x)