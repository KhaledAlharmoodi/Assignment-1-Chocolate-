#Task one
class Chocolates: #chocolate class
    def __init__(self, weight, price, types, ID): #attrbuites of the class
        self.weight = weight
        self.price = price
        self.types = types
        self.ID = ID

def iterativeChocDist(chocolates, students):# the first way of distrbuting the chocolates for the students
    distributed_chocolates = [] #chocolate list
    for i in range(len(students)): #for loop
        if i < len(chocolates): #if statment
            distributed_chocolates.append((students[i], chocolates[i]))
        else:
            break #stop the for loop
    return distributed_chocolates

def distribute_chocolates_recursive(chocolates, students, index=0): # the second way of distrbuting the chocolates for the stduents
    if index >= len(students) or index >= len(chocolates): #if statment
        return []
    else:
        return [(students[index], chocolates[index])] + distribute_chocolates_recursive(chocolates, students, index + 1)

# Test cases
chocolates = [Chocolates(3, 1, "Milk Chocolate", "001"),
    Chocolates(4, 2, "Carmel Chocolate", "002"),
    Chocolates(1, 4, "Dark Chocolate", "003"),
    Chocolates(2, 3, "White Chocolate", "004"),
    Chocolates(5, 9, "Hazelnut Chocolate", "005"),
    Chocolates(6, 7, "Pumpkin Chocolate", "006"),
    Chocolates(7, 10, "Mint Chocolate", "007"),
    Chocolates(9, 6, "Almond Chocolate", "008"),
    Chocolates(3, 7, "Pistachio Chocolate", "009"),
    Chocolates(8, 8, "Bubbld Chocolate", "010"),]

students = ["Khaled", "Mohammed", "Hamad", "Rashed", "Saif", "Sultan", "Fares", "Abdulla", "Ahmed", "Saeed"]


iterative_dist = iterativeChocDist(chocolates, students)# checking which chocolate is going to which student by using itertive disttrbution
print("Iterative Distribution:")
for student, chocolate in iterative_dist:#for loop
    print(f"{student} gets {chocolate.types}")

# Test recursive function
recursive_distribution = distribute_chocolates_recursive(chocolates, students) # checking which chocolate is going to which student by using recursive disttrbution
print("\nRecursive Distribution:")
for student, chocolate in recursive_distribution: #for loop
    print(f"{student} gets {chocolate.types}")

# Complexity Analysis
# Time Complexity: The time complexity of the recursive and iterative functions is O(min(n, m)), where n and m are the number of students and chocolates, respectively This is because the best-case, average-case, and worst-case possibilities are the same when we cycle through the students list or the chocolates list until we exhaust the smaller list.
# Space Complexity: Since both functions just store the dispersed chocolates in a list, their space complexity is O(min(n, m)).   The number of distributed chocolates, which is constrained by the smaller of the two input lists, determines the spatial complexity.

# Task two
def sort_chocolates_by_weight(chocolates): #sorting the chocolate by weight
    return sorted(chocolates, key=lambda x: x.weight)

def sort_chocolates_by_price(chocolates): #sorting the chocolate by price
    return sorted(chocolates, key=lambda x: x.price)

# Test cases
sorted_by_weight = sort_chocolates_by_weight(chocolates)
sorted_by_price = sort_chocolates_by_price(chocolates)

print("Chocolates sorted by weight:")
for chocolate in sorted_by_weight: #for loop
    print(f"Type: {chocolate.types}, Weight: {chocolate.weight}")

print("\nChocolates sorted by price:")
for chocolate in sorted_by_price: #foor loop
    print(f"Type: {chocolate.types}, Price: {chocolate.price}")

# Justification for sorting algorithm choice: We have chosen Python's built-in sorted() function which uses Timsort, a hybrid sorting algorithm derived from merge sort and insertion sort.Timsort is a very effective method for sorting a lot of chocolates since it has a time complexity of O(n log n) in both average and worst-case situations.

# Efficiency discussion: # Timsort's efficiency stays optimal with a time complexity of O(n log n) even if the number of chocolates and pupils increases dramatically. This is due to the fact that Timsort works well with partially sorted arrays, which can happen while giving students chocolates. As a result, even with a big input size, the method is still efficient.

# Complexity analysis: Sorting chocolates by price and weight has a time complexity of O(n log n) since the time complexity of Timesort (used in Python's sorted() function) is O(n log n) on average and worst-case situations.Since more space is needed to keep the sorted lists, the space complexity for both sorting processes is O(n), where n is the number of chocolates.


#Task three
def chocolate_price_search(chocolates, price):  #searching chocolate by price
    for student, chocolate in chocolates: #for loop
        if chocolate.price == price: #if statment
            return student
    return None

def chocolate_weight_search(chocolates, weight):  #searching chocolate by weight
    for student, chocolate in chocolates: #for loop
        if chocolate.weight == weight: # if statement
            return student
    return None

# Test cases
price = 4  # Use the same price variable as in Task one
StudentSpecifiedPrice = chocolate_price_search(iterative_dist, price)
if StudentSpecifiedPrice:
    print(f"The student who is holding a chocolate with price {price} is: {StudentSpecifiedPrice}")
else:
    print(f"No student is found holding a chocolate with price {price}")

weight = 7 # Use the same weight variable as in Task one
StudentSpecifiedWeight = chocolate_weight_search(iterative_dist, weight)
if StudentSpecifiedWeight:
    print(f"The student who is holding a chocolate with weight {weight} is: {StudentSpecifiedWeight}")
else:
    print(f"No student is found holding a chocolate with weight {weight}")

# Distribution Algorithms:The time and space complexities of recursive and iterative distributions are comparable. They take the same amount of time, m, depending on which is smaller—the number of students or the number of chocolates (n). They also require a space that is proportionate to the smaller of n or m.

# Sorting Algorithms:Timsort, an extremely effective sorting algorithm, is used for pricing and weight-based sorting. For both the best and average situations, the time required is proportional to n (the number of chocolates) multiplied by the logarithm of n (O (n log n)). The amount of additional memory needed is O(n) times the number of chocolates.

# Searching Algorithms: Searching by price and weight simply goes through the list of chocolates once. In both the best and worst situations, the amount of time required is equal to the number of chocolates (n). Its space complexity is constant O (1) since it doesn't need any more memory beyond what is needed to store the input data.

