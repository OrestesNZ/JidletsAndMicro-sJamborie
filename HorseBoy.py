#suck horse cum

# git add filyname.py - stage the file for commit, add the file to the staging area, ready to be committed
# git commit -m "Initial commit"
# git push

# branching - create wokring on a safe copy 
# parellel 
# git checkout -b feature-test 

# check which branch you are on 
# git branch

#go back to main
# git checkout main

# updating 
# pull the changes down - make a change on the github (friend changes), local code will be out of date, need to pull down the changes to update local code
# git pull origin main 

# collaborating 
# grant them permission
# they clone, they edit, they push, sync

# merge conflicts - when two people edit the same line of code, git doesn't know which one to keep, need to resolve the conflict manually

# Fetch updates without merging them into your code
#git fetch origin

# See the difference between your local code and the remote code
#git diff main origin/main

inventory = {
    "food": {"apples": 50, "bread": 2, "milk": 1},
    "alcohol": {"wine": 12, "beer": 5, "whiskey": 2}
}

def find_stock(item_name, inventory_data):
    for category, items in inventory_data.items():
        if item_name in items:
            # 'items' is the sub-dictionary (e.g., {"apples": 50, "bread": 2, ...})
            # So just use items[item_name]
            quantity = items[item_name]
            print(f"Found {item_name} in {category}. Quantity: {quantity}")

            if quantity < 10:
                order_function(item_name, quantity, inventory_data, category)
                
            return quantity
    print(f"{item_name} not found in inventory.")

def order_function(item, current_qty, inventory_data, category):
    print(f"--ALERT: {item} is low ({current_qty}). Placing Order for 20 more!")
    # update dictionary: category then item accessed
    inventory_data[category][item] += 20

    print(f"New stock for {item}: {inventory_data[category][item]}")

stock_update = find_stock("bread", inventory)