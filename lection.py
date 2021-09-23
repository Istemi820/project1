#cash = [1212,2434,4656,6767,787]
#rashod = 0.2
#count = 0
#for i in cash:
 #   count = count + 1
#print(count)
#itog = count -(count * rashod)
#print(itog)
#def get_cash(cash_list, rashod):
 #   count = 0
  #  for i in cash:
   #     count = count + i
    #itog = count - (count * rashod)
    #return itog
#print(get_cash(cash, rashod))
#def get(*args, **kwargs):
 #   if args:
  #      print(args)
   ##    print(kwargs)
#get(1,'A', True, a = 34, b = False)
#def itog(**kwargs):
 #   count = len(kwargs)
  #  shet = 0
   ##    shet += x
    #return shet/count
#print(itog(mat = 100, fiz = 50))
#debts = {"Ron": 4500, "Leo": 5600, "Sonny": 7000}
#for x,y in debts.items():
  #  print(x,y)

def get_num(*args):
    a = 0
    for i in args:
        if type(i) == int:
            a += i
    return a
print(get_num(1, False, 2,3,5, "jhhoi"))