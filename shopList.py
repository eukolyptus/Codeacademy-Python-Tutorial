shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

#helper method
def print_list(list):
    for item in list:
        item_name = item
        item_price = list[item]
        print ("[" + item_name + "]: %s" % item_price)
        


#print results
print_list(stock)
print_list(prices)


# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        total += food[item] * prices[item]
        #return total

    print (total)

compute_bill(stock)
        
        
        
        