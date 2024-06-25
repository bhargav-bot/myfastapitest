import paramiko

# Server details
host = '159.89.42.243'  # Replace with your server's IP address
port = 22  # Default SSH port is 22
username = 'Yesha'  # Replace with your SSH username
password = 'Yesha@1496'  # Replace with your SSH password

# SSH session setup
try:
    # Create SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    ssh_client.connect(hostname=host, port=port, username=username, password=password)

    # Example command to execute on the server
    command = 'ls -l /home/Yesha/myfastapitest'  # Replace with your desired command

    # Execute the command
    stdin, stdout, stderr = ssh_client.exec_command(command)

    # Read the output from the command
    output = stdout.read().decode('utf-8')

    # Print the output
    print(f"Command output:\n{output}")

    # Close the SSH connection
    ssh_client.close()

except Exception as e:
    print(f"Error: {e}")
    # Handle exceptions as needed
