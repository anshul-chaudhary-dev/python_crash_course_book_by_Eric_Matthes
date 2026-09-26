#example:1
for page in range(1,11):
    print(page)
    
# for better :

for page in range(1, 11):
    print(f"page {page}")
    
# example :2
# automated retry mechanisum (Network Request)
# Scenario: When an app tries to connect to a server , the network might flicker insted of failling immediately,production code ussually retries the connection up to 3 times before giving up.
#TASK: Use range() to simulate a loop that attempts a network connection up to times .

for Attempt in range (1, 4):
    print(f" Attempt {Attempt}: connecting to server ...")
    
print(" failled to cnnect after 3 aatempt.")

# Example:3: Batch Data Processing(skipping steps)
for index in range(0, 51, 5):
    print(f"Processing record at index:{index}")

