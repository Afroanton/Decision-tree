import dtree as tree
import monkdata as m

monk1a1 = tree.averageGain(m.monk1, m.attributes[0])
monk1a2 = tree.averageGain(m.monk1, m.attributes[1])
monk1a3 = tree.averageGain(m.monk1, m.attributes[2])
monk1a4 = tree.averageGain(m.monk1, m.attributes[3])
monk1a5 = tree.averageGain(m.monk1, m.attributes[4])
monk1a6 = tree.averageGain(m.monk1, m.attributes[5])

print(monk1a1)
print(monk1a2)
print(monk1a3)
print(monk1a4)
print(monk1a5)
print(monk1a6)

#Results 1:
#0.07527255560831925
#0.005838429962909286
#0.00470756661729721
#0.02631169650768228
#0.28703074971578435
#0.0007578557158638421


monk1 = tree.averageGain(m.monk2, m.attributes[0])
monk2 = tree.averageGain(m.monk2, m.attributes[1])
monk3 = tree.averageGain(m.monk2, m.attributes[2])
monk4 = tree.averageGain(m.monk2, m.attributes[3])
monk5 = tree.averageGain(m.monk2, m.attributes[4])
monk6 = tree.averageGain(m.monk2, m.attributes[5])

print(monk1)
print(monk2)
print(monk3)
print(monk4)
print(monk5)
print(monk6)

#Results 2 :
#0.0037561773775118823
#0.0024584986660830532
#0.0010561477158920196
#0.015664247292643818
#0.01727717693791797
#0.006247622236881467


monk1 = tree.averageGain(m.monk3, m.attributes[0])
monk2 = tree.averageGain(m.monk3, m.attributes[1])
monk3 = tree.averageGain(m.monk3, m.attributes[2])
monk4 = tree.averageGain(m.monk3, m.attributes[3])
monk5 = tree.averageGain(m.monk3, m.attributes[4])
monk6 = tree.averageGain(m.monk3, m.attributes[5])

print(monk1)
print(monk2)
print(monk3)
print(monk4)
print(monk5)
print(monk6)

#Results 3 :
0.007120868396071844
0.29373617350838865
0.0008311140445336207
0.002891817288654397
0.25591172461972755
0.007077026074097326
