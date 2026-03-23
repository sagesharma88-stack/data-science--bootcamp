#Day 5 pratice
#Topic Numpy

"""Problem Statement
At AtliQ, a software service company, the HR team wants to analyze employee happiness and tenure to improve company policies and employee retention.The dataset is represented using NumPy arrays:
Employee Details Array: Stores Employee ID, Department, and Years of Experience at AtliQ.
Survey Results Array: Stores Employee ID and Happiness Score (on a scale of 1–10).
The objective of this task is to use NumPy operations to analyze employee happiness in relation to their experience and department."""
import numpy as np
# Employee Details: Employee ID, Department, Number of Years with AtliQ
employee_details = np.array([
    [101, 'Sales', 3],  
    [102, 'HR', 5],    
    [103, 'IT', 2],        
    [104, 'Sales', 8],    
    [105, 'IT', 6],      
    [106, 'HR', 4],           
    [107, 'IT', 7],    
    [108, 'Sales', 1], 
    [109, 'HR', 3]          
])
# Survey Results: Employee ID, Happiness Score (1-10)
survey_results = np.array([
    [101, 8],
    [102, 10],
    [103, 9],
    [104, 6],
    [105, 7],
    [106, 8],
    [107, 9],
    [108, 5],
    [109, 7]
])

#Task 1:Combine employee details and survey results using np.hstack().
merged_array = np.hstack((employee_details,survey_results))
print(merged_array)

#Task 2:Display all employee happiness scores from the merged array.
happiness_score = merged_array[:,-1]
print(happiness_score)

#Task 3:Sort and display employee happiness scores in ascending order.
sort_array = np.sort(happiness_score.astype(np.float64))
print(sort_array)

#Task 4:Print each employee's ID and department from the array.
for rows in merged_array:
    print(f"Employee_Id: {rows[0]}\tDepartment:{rows[1]}")

#Task 5:Print each employee’s ID with their happiness score from the merged array.
for rows in merged_array:
    print(f"Employee_Id: {rows[0]}\t Happiness_score:{rows[-1]}")

#Task 6:Convert all happiness scores to float type using astype(float).
print(merged_array[:,-1].astype(float))

#Task 7:Calculate and display the average happiness score of all employees.
print(np.mean(merged_array[:,-1].astype(float)))

#Task 8: Find and print all unique departments using np.unique().
print(merged_array[:,1])
print(np.unique(merged_array[:,1]))

#Task 9:Calculate and display the average happiness score for employees in the HR department.
hr_detais = merged_array[:,1]=="HR"
hr_array = merged_array[hr_detais]
print(hr_array)
print(np.mean(hr_array[:,-1].astype(float)))