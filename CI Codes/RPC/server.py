from xmlrpc.server import SimpleXMLRPCServer

# Define factorial function
def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

# # Health check function
def health():
    return "Server is running"

# Create XML-RPC server on port 8001
server = SimpleXMLRPCServer(("localhost", 8000))
print("XML-RPC Server is running on port 8000...")

# Register functions
server.register_function(factorial, "factorial")
server.register_function(health, "health")

# Start the server
server.serve_forever()