import paramiko

# Server details
host = '159.89.42.243'  # Replace with your server's IP address
port = 22  # Default SSH port is 22
username = 'Yesha'  # Replace with your SSH username
password = 'Yesha@1496'  # Replace with your SSH password

try:
    # Create SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    ssh_client.connect(hostname=host, port=port, username=username, password=password)

    # Execute git pull command
    command = 'cd /home/Yesha/myfastapitest && /usr/bin/git pull origin main'

    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    
    # Print command output
    print(f"Command: {command}")
    if output:
        print(f"Output:\n{output}")
    if error:
        print(f"Error:\n{error}")

    # Close the SSH connection
    ssh_client.close()

except Exception as e:
    print(f"Error: {e}")
    # Handle exceptions as needed
