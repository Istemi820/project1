#lists =
#for i  in range(-100,50):
 #   if i % 3 == 0 and i % 5 == 0:
  #     # pow(2,3)
   #     number = abs(i**3)
    #    lists.append(number)
#print(lists)
#lists = [abs(pow(x,3))  for x in range(-100,50) if x % 3 == 0 and x % 5 ==0]
#print(lists)
#def filter_list(range1, range2):
 #   lists = [abs(pow(x, 3)) for x in range(range1, range2) if x % 3 == 0 and x % 5 == 0]
  #  return lists
#list1 = filter_list(-100,100)
#print(list1)

#cyal = {
 #   'home': '2этаж', 'car': 'Bmw x7'
#}
#saical  = {
 #   'home':'etaj', 'car': 'lhl'
#}
#python_boot = [cyal, saical]
#car = [x.get('car') for x in python_boot]
#print(car)
#python_boot = [cyal, saical]
#home = list()
#for i in python_boot:
 #   home.append(i.get('home'))
#print(home)

#from datetime import datetime
#def time(func):
 #   def wrapper():
  #      start = datetime.now()
   #     func()
    #    end = datetime.now() - start
     #   print(end)
    #return wrapper

#@time
#def func1():
 #   start = datetime.now()
  #  lists = []
   # for i in range(5, 1000000):
   #     lists.append(i)
    #end = datetime.now() - start
    #print('Время for', end)
    #return lists

#@time
#def func2():
 #   start = datetime.now()
  #   lists = [x for x in range(1,1000000)]
   #  end = datetime.now() - start
    #print('Время list comprehentions', end)
    #return lists
#func1()
#func2()

def gumburger(cotlet):
    def wrapper(*args, **kwargs):
        print("Vverhnya bulca")
        cotlet(*args, **kwargs)
        print("nijnya bulca")

    return wrapper

@gumburger
def cotlet(ingr):
    print(f"cotleta iz {ingr}")
cotlet("chicen")

lists = ["Cyial", "Meerim", "Iscender"]
print(f"m - {lists[1]}")
print("{0},{3}".format(lists[1],lists[2],lists[0],lists[0]))

d = {
    "name": "Vica",
    "age": 18
    }
name = d.pop("name")
d.update({"name": "Eldar"})
print(len(d))
print(d)
#print(name)
