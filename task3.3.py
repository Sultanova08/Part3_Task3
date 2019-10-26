list_ = input ("Enter the list number: ").split(" ")
step = int(input ("Enter the step:"))

def shift(lst, steps):
    if steps > 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
print(list_)
 
shift(list_,step)
print(list_)


