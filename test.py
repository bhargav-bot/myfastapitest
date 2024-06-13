from dotenv import load_dotenv
import os

load_dotenv()

# Print loaded environment variables
print(os.getenv("database_hostname"))
print(os.getenv("database_port"))
# Add other variables as needed
