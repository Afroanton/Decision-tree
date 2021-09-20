import dtree as tree
import monkdata as m

monk = tree.entropy(m.monk1)
monk2 = tree.entropy(m.monk2)
monk3 = tree.entropy(m.monk3)

print(monk)
print(monk2)
print(monk3)

#Results:
# monk 1  =  1.0
# monk 2  =  0.957117428264771
# monk 3  =  0.9998061328047111