#Day2 Pracice

#Task 1. Count numbers of items from a list
avengers = ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']
print(len(avengers))

#Task 2. Adding a new element to the list
avengers = ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']
avengers.append("Spiderman")
print(avengers)

#Task 3. To remove an element using pop() method and changing the position of an element
avengers = ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']
removed_avenger = avengers.pop(1)
avengers.insert(0,removed_avenger)
print(avengers)

#Task 4. Find the value of element from a list(indexing and slicing method)
scores = [92, 85, 76, 58, 89, 91, 73, 84]
print(scores[0])            #score of first student
print(scores[-1])           #score of last student
print(scores[:3])           #score of first three students
print(scores[2:5])          # scores of roll #3, 4 and 5

#Task 5. Append the score to the scores list
scores = [92, 85, 76, 58, 89, 91, 73, 84]
scores.append(83)
print(scores)

#Task 6. Categorizing the scores into grades
a = b = c = d= f= 0                    #Intializing the counters for each grade
for score in scores:
    if score >= 90:                    #Condition for grade A
        a += 1
    elif score >=80 and score < 90:    #Condition for grade B
        b += 1
    elif score >=70 and score < 80:    #Condition for grade C
        c += 1
    elif score >= 60 and score < 70:   #Condition for grade D
        d += 1
    else:
        f += 1                         #Condition for grade F
print("Grade Summary:")
print(f"-A: {a} students")
print(f"-B: {b} students")
print(f"-C: {c} students")
print(f"-D: {d} students")
print(f"-F: {f} students")

#Task 7. Checking an inventory for items to reorder
# Lists to store product names and stock levels
product_names = ["Apples", "Bananas", "Oranges", "Pears", "Grapes"]
stock_levels = [20, 50, 15, 5, 8]

minimum_stock = 10  # Minimum stock before reordering
reorder_list = []
for products in range(len(product_names)):
    if stock_levels[products] < 10:
        reorder_list.append(product_names[products])
print("Items to reorder-")
for product in reorder_list:
    print(f"-{product}")

