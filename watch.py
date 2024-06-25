import os
import logging
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import paramiko

# Set up logging
logging.basicConfig(filename='/tmp/watchfolder_debug.log', level=logging.INFO)

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f'File modified: {event.src_path}')
            # Change directory and check git status
            os.system('cd /Users/bhargav/Desktop/python/vscode/bhargavnufolder && git status > /tmp/git_status.log')
            with open('/tmp/git_status.log', 'r') as f:
                status_output = f.read()
            if 'nothing to commit' not in status_output:
                # If changes exist, add, commit, and push
                os.system('git add . && git commit -m "Updated watch.py to automatically push changes to GitHub" && git push origin main')
                # Clone changes to server via SSH using Paramiko
                try:
                    ssh_client = paramiko.SSHClient()
                    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh_client.connect('159.89.42.243', username='Yesha', password='Yesha@1496')
                    ssh_client.exec_command('cd /home/Yesha/myfastapitest && git pull origin main')
                    logging.info('Changes pulled from GitHub to server successfully')
                except Exception as e:
                    logging.error(f'Error executing SSH command: {str(e)}')
                finally:
                    ssh_client.close()
            else:
                logging.info('No changes to commit')

    def on_created(self, event):
        if not event.is_directory:
            logging.info(f'File created: {event.src_path}')
            # Change directory and check git status
            os.system('cd /Users/bhargav/Desktop/python/vscode/bhargavnufolder && git status > /tmp/git_status.log')
            with open('/tmp/git_status.log', 'r') as f:
                status_output = f.read()
            if 'nothing to commit' not in status_output:
                # If changes exist, add, commit, and push
                os.system('git add . && git commit -m "Updated watch.py to automatically push changes to GitHub" && git push origin main')
                # Clone changes to server via SSH using Paramiko
                try:
                    ssh_client = paramiko.SSHClient()
                    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh_client.connect('159.89.42.243', username='Yesha', password='Yesha@1496')
                    ssh_client.exec_command('cd /home/Yesha/myfastapitest && /usr/bin/git pull origin main')
                    logging.info('Changes pulled from GitHub to server successfully')
                except Exception as e:
                    logging.error(f'Error executing SSH command: {str(e)}')
                finally:
                    ssh_client.close()
            else:
                logging.info('No changes to commit')

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
