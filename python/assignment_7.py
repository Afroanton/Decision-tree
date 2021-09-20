import monkdata as m
import dtree as d
import random
import sys
import statistics
import matplotlib.pyplot as plt



## first one is parameter tuning. 

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]
   
   
def pruning(dataset, frac):
    monktrain, monkval = partition(dataset, frac)
    build_tree = d.buildTree(monktrain, m.attributes)
    
    ## error rate
    tree_score = 1 - d.check(build_tree, monkval)
    best_error_value = float('-inf')
    least_error_value = tree_score
    least = least_error_value

    ## monk1
    while best_error_value < least_error_value:
        least_error_value = least
        pruned = d.allPruned(build_tree)
        best = build_tree
        for tree in pruned:
            a = 1 - d.check(tree, monkval)
            if a < least:
                least = 1 - d.check(tree, monkval)
                best = tree
        best_error_value = least
        build_tree = best
    return best_error_value 

frac = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

monk1_results_1 = []
monk1_results_2 = []
monk1_results_3 = []
monk1_results_4 = []
monk1_results_5 = []
monk1_results_6 = []

monk3_results_1 = []
monk3_results_2 = []
monk3_results_3 = []
monk3_results_4 = []
monk3_results_5 = []
monk3_results_6 = []

for i in range(100):
    monk1_results_1.append(pruning(m.monk1, frac[0]))
    monk3_results_1.append(pruning(m.monk3, frac[0]))
    
for i in range(100):
    monk1_results_2.append(pruning(m.monk1, frac[1]))
    monk3_results_2.append(pruning(m.monk3, frac[1]))
    
for i in range(100):
    monk1_results_3.append(pruning(m.monk1, frac[2]))
    monk3_results_3.append(pruning(m.monk3, frac[2]))
    
for i in range(100):
    monk1_results_4.append(pruning(m.monk1, frac[3]))
    monk3_results_4.append(pruning(m.monk3, frac[3]))
    
for i in range(100):
    monk1_results_5.append(pruning(m.monk1, frac[4]))
    monk3_results_5.append(pruning(m.monk3, frac[4]))
    
for i in range(100):
    monk1_results_6.append(pruning(m.monk1, frac[5]))
    monk3_results_6.append(pruning(m.monk3, frac[5]))

## frac 0
monk1_mean_1 = statistics.mean(monk1_results_1)
monk1_std_1 = statistics.stdev(monk1_results_1)
monk3_mean_1 = statistics.mean(monk3_results_1)
monk3_std_1 = statistics.stdev(monk3_results_1)
print("monk1 frac[0] | mean: ", monk1_mean_1, " stdev: ", monk1_std_1)
print("monk3 frac[0] | mean: ", monk3_mean_1, " stdev: ", monk3_std_1)

## frac 1
monk1_mean_2 = statistics.mean(monk1_results_2)
monk1_std_2 = statistics.stdev(monk1_results_2)
monk3_mean_2 = statistics.mean(monk3_results_2)
monk3_std_2 = statistics.stdev(monk3_results_2)
print("monk1 frac[1] | mean: ", monk1_mean_2, " stdev: ", monk1_std_2)
print("monk3 frac[1] | mean: ", monk3_mean_2, " stdev: ", monk3_std_2)

## frac 0
monk1_mean_3 = statistics.mean(monk1_results_3)
monk1_std_3 = statistics.stdev(monk1_results_3)
monk3_mean_3 = statistics.mean(monk3_results_3)
monk3_std_3 = statistics.stdev(monk3_results_3)
print("monk1 frac[2] | mean: ", monk1_mean_3, " stdev: ", monk1_std_3)
print("monk3 frac[2] | mean: ", monk3_mean_3, " stdev: ", monk3_std_3)

## frac 0
monk1_mean_4 = statistics.mean(monk1_results_4)
monk1_std_4 = statistics.stdev(monk1_results_4)
monk3_mean_4 = statistics.mean(monk3_results_4)
monk3_std_4 = statistics.stdev(monk3_results_4)
print("monk1 frac[3] | mean: ", monk1_mean_4, " stdev: ", monk1_std_4)
print("monk3 frac[3] | mean: ", monk3_mean_4, " stdev: ", monk3_std_4)

## frac 0
monk1_mean_5 = statistics.mean(monk1_results_5)
monk1_std_5 = statistics.stdev(monk1_results_5)
monk3_mean_5 = statistics.mean(monk3_results_5)
monk3_std_5 = statistics.stdev(monk3_results_5)
print("monk1 frac[4] | mean: ", monk1_mean_5, " stdev: ", monk1_std_5)
print("monk3 frac[4] | mean: ", monk3_mean_5, " stdev: ", monk3_std_5)

## frac 0
monk1_mean_6 = statistics.mean(monk1_results_6)
monk1_std_6 = statistics.stdev(monk1_results_6)
monk3_mean_6 = statistics.mean(monk3_results_6)
monk3_std_6 = statistics.stdev(monk3_results_6)
print("monk1 frac[5] | mean: ", monk1_mean_6, " stdev: ", monk1_std_6)
print("monk3 frac[5] | mean: ", monk3_mean_6, " stdev: ", monk3_std_6)

ylabel_monk1 = []
ylabel_monk3 = []

ylabel_monk1.append(monk1_mean_1)
ylabel_monk1.append(monk1_mean_2)
ylabel_monk1.append(monk1_mean_3)
ylabel_monk1.append(monk1_mean_4)
ylabel_monk1.append(monk1_mean_5)
ylabel_monk1.append(monk1_mean_6)

ylabel_monk3.append(monk3_mean_1)
ylabel_monk3.append(monk3_mean_2)
ylabel_monk3.append(monk3_mean_3)
ylabel_monk3.append(monk3_mean_4)
ylabel_monk3.append(monk3_mean_5)
ylabel_monk3.append(monk3_mean_6)

xlabel = frac

ylabel_monk1_std = []
ylabel_monk3_std = []

ylabel_monk1_std.append(monk1_std_1)
ylabel_monk1_std.append(monk1_std_2)
ylabel_monk1_std.append(monk1_std_2)
ylabel_monk1_std.append(monk1_std_4)
ylabel_monk1_std.append(monk1_std_5)
ylabel_monk1_std.append(monk1_std_6)

ylabel_monk3_std.append(monk3_std_1)
ylabel_monk3_std.append(monk3_std_2)
ylabel_monk3_std.append(monk3_std_3)
ylabel_monk3_std.append(monk3_std_4)
ylabel_monk3_std.append(monk3_std_5)
ylabel_monk3_std.append(monk3_std_6)


# print(ylabel_monk1)
# print(ylabel_monk3)
# print(ylabel_monk1_std)
# print(ylabel_monk3_std)

fig, ax = plt.subplots()
ax.plot(xlabel, ylabel_monk1)

ax.set(xlabel='fractions', ylabel='errors',
       title='error rate MONK1')
ax.grid()

#fig.savefig("test.png")
plt.show()
    
    
fig, bx = plt.subplots()
bx.plot(xlabel, ylabel_monk3)

bx.set(xlabel='fractions', ylabel='errors',
       title='error rate MONK3')
bx.grid()

#fig.savefig("test.png")
plt.show()
    

    
    
    
    
    
    
    
    
    
    
    

