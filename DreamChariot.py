# New file push, 
#new files
#git add DreamChartiot.py
#git commit -m "Initial commit of DreamChariot.py"
#git push origin main

#update file
# git add DreamChartiot.py 
# git commit -m "Updated logic in DreamCharitot.py"
# git push origin main


"""
Prompt - Gemini
Awesome lets more onto another practical python puzzle, 
lets do something to find the shortest path,
lets think of it as a car salesman, we have 3 sites, 
and customers at certain sites, these customers want certain cars that are not availabe at there closest site, 
the carsalesman are willing to move cars to other sites, and the customers are willing to drive to other sites to pick up their new cars,
how can we discover which is most efficient path, 
the customer moving to the site, or the carsalesman moving a car to another site.

Response - Gemini
This is a fantastic real-world scenario! It’s a classic optimization problem that involves balancing multiple moving parts to find the "path of least resistance." 🚗

To solve this, we'll need to look at Weighted Graphs. In this model:

Nodes (Vertices) 📍: Represent the 3 sites.

Edges (Lines) 🛣️: Represent the roads between them.

Weights (Costs) 💸: Represent the "cost" of moving (fuel, time, or driver wages).

I'll help guide you through building this logic block by block. Before we write any code, we need to define how we measure "efficiency." Usually, the cost of a salesman moving a car is different from a customer driving their own car.

Block 1: The Cost Matrix
First, we need to establish the distances between our three sites: Site A, Site B, and Site C.

Let's assume these distances (or costs) are:

A to B: 10 miles

B to C: 15 miles

A to C: 20 miles

If a car salesman moves a car, it might cost $2.00 per mile (including their time and gas). If a customer drives, it might only cost them $0.50 per mile (just gas).

Let's start our first block of logic: 🧠
If a customer is at Site A and their dream car is at Site C, what are the two specific paths we need to compare to see which is cheaper?
"""

#Basic logic formating of variables to be used in the code,
# We can represent the sites and distances as a graph using an adjacency matrix or list.    
#weighted Graphs
    # nodes (vertices): Represent 3 sites
    # Edges (lines): Represent the roads between them
    # Weights (costs): represent the cost of moving (fuel, time, driver wages)

# Block 1 
    #Establish distances between sites A, B, C 
    # A to B = 10 miles
    # B to C = 15 miles
    # C to A = 20 miles

# If a car salesman moves a car, it might cost $2.00 per mile (gas and time), 
# If a customer dirves, it might only cost them $0.50 per mile 

# Logic
    # if a customer is at site A and their dream car is site C, what are paths we need to compare to see which is cheaper? 

# %% 
# BLock One: The Data Structure 
# define distances between the sites and the cost constants for both the salesman and the customer 

#the "Map": Distances between the site in miles 
distances = {
    'Site A': {'Site B': 17, 'Site C':50},
    'Site B': {'Site A': 55, 'Site C': 75},
    'Site C': {'Site A': 20, 'Site B': 15}
}

# %%
# The "Weights": Costs per mile
SALESMAN_SERVICE_FEE = 5 # flat fee for the service of moving a car
SALESMAN_COST_PER_MILE = 0.75
CUSTOMER_COST_PER_MILE = 0.85

# %%
#print(distances['Site A'])
#print(distances['Site B']['Site A'])
# iterate through nested distances dict 
for site, connections in distances.items():
        print(f"{site}:")
        for destination, distance in connections.items():
            print(f" {destination}: {distance}")

# Transportation Problem
# weighted graph, edge weights
# Scenario 
# The Car: Located at Site C
# The Customer: Locaed at Site A

# %%
#Option 1: Saelsman moves the car from Site C to Site A
salesman_cost_ac = (distances['Site C']['Site A'] * SALESMAN_COST_PER_MILE) + SALESMAN_SERVICE_FEE 
customer_cost_ac = distances['Site A']['Site C'] * CUSTOMER_COST_PER_MILE

# %%
def find_cheapest_mover(start, end):
      # we need to get the distance from our dictionary
      dist = distances[start][end]
      salesman_cost = (dist * SALESMAN_COST_PER_MILE) + SALESMAN_SERVICE_FEE
      customer_cost = dist * CUSTOMER_COST_PER_MILE
      if salesman_cost < customer_cost:
            print(f"Cheaper for the salesman to move the car from {start} to {end}. Cost: ${salesman_cost:.2f}")
      elif customer_cost < salesman_cost:
            print(f"Cheaper for the customer to drive from {start} to {end}. Cost: ${customer_cost:.2f}")

# %%
find_cheapest_mover('Site A', 'Site B')


# %%
