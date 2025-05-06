import xmlrpc.client

server_url = "http://localhost:8000"
proxy = xmlrpc.client.ServerProxy(server_url)

# Input from user
num = int(input("Enter a number to calculate factorial: "))

# Calling remote function
result = proxy.factorial(num)
print(f"Factorial of {num} is: {result}")

# Checking server health
print("Health Check:", proxy.health())