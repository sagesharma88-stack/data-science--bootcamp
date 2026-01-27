#Day 3 Practice 
#Topic : Functions, Dictionary, Tuples, File handling

#Task 1. Reading a file and building a dictionary
#Reading a file(customers.txt) to save the data in a dictionary
customer_record = {}                                     #Creating an empty dictionary

with open("customers.txt","r") as f:                     #Reading the customers.txt file
    for record_lines in f:
        customer_name, purchase_amount = record_lines.split(",")
        customer_record[customer_name]=int(purchase_amount.strip())       #Adding the key&value pair to the dictionary
print(customer_record)

#Task 2. Calculating rewards for the customers by accesing the customer_record dictinoary
#Function to calculate the reward
def calculate_rewards(customer_record):
    for customer_name,total_purchases in customer_record.items():
        if total_purchases>= 500:
            print(f"{customer_name}. Your total purchase is {total_purchases},You win Gold!")
        elif total_purchases>=200:
            print(f"{customer_name}. Your total purchase is {total_purchases}, You win Silver!")
        else:
            print(f"{customer_name}. Your total purchase is {total_purchases},You win Bronze!")
calculate_rewards(customer_record)

#Task 3. Making a new dictionary with customer's name, purchase amount and their dicitonary
customers_summary_dict = {}
for customer_name,purchase_amount in customer_record.items():
    if purchase_amount>= 500:
         reward = "Gold"
    elif purchase_amount >= 200:
         reward = "Silver"
    else:
         reward = "Bronze"
    customers_summary_dict[customer_name] = (purchase_amount,reward)
print(customers_summary_dict)

#Task  4. Combinig all the above task to make a function that takes a file as input and gives customer_summary dictionary
def process_customer_data(filename):
    customers_summary_dict = {} 

    #Reading the file                                   
    with open(filename,"r") as f:                     
        for record_lines in f:
            customer_name, purchase_amount = record_lines.split(",")
            total_purchase_amount =int(purchase_amount.strip())       
        
            #Deciding the reward 
            if total_purchase_amount >= 500:
                reward = "Gold"
            elif total_purchase_amount >= 200:
                reward = "Silver"
            else:
                reward = "Bronze"
            customers_summary_dict[customer_name] = (total_purchase_amount,reward)
    return customers_summary_dict
 #Calling the function
print(process_customer_data("customers.txt"))

    
