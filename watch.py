import os
import logging
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import paramiko

# Set up logging
logging.basicConfig(filename='/tmp/watchfolder_debug.log', level=logging.INFO)

# Define Git commands function
def run_git_commands(repo_dir):
    print(f"Running git commands in {repo_dir}")
    os.chdir(repo_dir)
    os.system('git status > /tmp/git_status.log')
    with open('/tmp/git_status.log', 'r') as f:
        status_output = f.read()
    if 'nothing to commit' not in status_output:
        os.system('git add . && git commit -m "Updated watch.py to automatically push changes to GitHub" && git push origin main')
        return True
    else:
        logging.info('No changes to commit')
        return False

# Define SSH function to pull changes
def pull_changes_via_ssh():
    print("Executing SSH command to pull changes from GitHub to server")
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='159.89.42.243',port=22, username='Yesha', password='Yesha@1496')
        print("SSH connection established gksuccessfully")
        command='cd /home/Yesha/myfastapitest && /usr/bin/git pull origin main'
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        logging.info('Changes pulled from GitHub 1to server successfully')
        print(f"Command: {command}")
        if output:
            print(f"Output:\n{output}")
        if error:
            print(f"Error:\n{error}")
        ssh_client.close()
    except Exception as e:
        print(f"Error: {e}")


# Define event handler class
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f'File modified: {event.src_path}')
            if run_git_commands("/Users/bhargav/Desktop/python/vscode/bhargavnufolder"):
                pull_changes_via_ssh()

    def on_created(self, event):
        if not event.is_directory:
            logging.info(f'File created: {event.src_path}')
            if run_git_commands("/Users/bhargav/Desktop/python/vscode/bhargavnufolder"):
                pull_changes_via_ssh()

if __name__ == "__main__":
    path = "/Users/bhargav/Desktop/python/vscode/bhargavnufolder"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    logging.info('Watcher started')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
