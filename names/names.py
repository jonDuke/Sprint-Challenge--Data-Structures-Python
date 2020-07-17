from binary_search_tree import BSTNode
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# original file ran in 6.3 seconds on my machine
# original solution runs in 1.9 seconds after putting it in this function (interesting)
def original_brute_force():
    duplicates = []  # Return the list of duplicates in this data structure
    for name_1 in names_1:
        for name_2 in names_2:
            if name_1 == name_2:
                duplicates.append(name_1)
    return duplicates

# runtime on my machine: 0.09 seconds
def binary_search_tree_approach():
    duplicates = []
    
    # insert one of the lists into a binary search tree
    # uses the binary search tree class we built earlier this week
    bst = BSTNode(names_2[0])
    for name in names_2:
        bst.insert(name)

    # search bst for matching names
    for name in names_1:
        if bst.contains(name):
            duplicates.append(name)
        
    return duplicates

# runtime on my machine: 0.05 seconds
def stretch_using_set():
    # add both lists to a set, then get the intersection
    # convert back to a list and return
    return list(set(names_1) & set(names_2))

# choose which function runs here
# duplicates = binary_search_tree_approach()
duplicates = stretch_using_set()

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
