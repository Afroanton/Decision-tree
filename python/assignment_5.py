import monkdata as m
import dtree as tree

t = tree.buildTree(m.monk1, m.attributes)
print(tree.check(t, m.monk1test))

t = tree.buildTree(m.monk1, m.attributes)
print(tree.check(t, m.monk1))

#Results 1
# 0.8287037037037037
# 1.0

t = tree.buildTree(m.monk2, m.attributes)
print(tree.check(t, m.monk2test))

t = tree.buildTree(m.monk2, m.attributes)
print(tree.check(t, m.monk2))

#Results 2
# 0.6921296296296297
# 1.0

t = tree.buildTree(m.monk3, m.attributes)
print(tree.check(t, m.monk3test))

t = tree.buildTree(m.monk3, m.attributes)
print(tree.check(t, m.monk3))

#Results 3
# 0.9444444444444444
# 1.0