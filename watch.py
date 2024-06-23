import os
import logging
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set up logging
logging.basicConfig(filename='/tmp/watchfolder_debug.log', level=logging.INFO)

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f'File modified: {event.src_path}')
            # Change directory and perform git add, commit, and push
            os.system('cd /Users/bhargav/Desktop/python/vscode/bhargavnufolder && git add . && git commit -m "Updated watch.py to automatically push changes to GitHub" && git push origin main')

    def on_created(self, event):
        if not event.is_directory:
            logging.info(f'File created: {event.src_path}')
            # Change directory and perform git add, commit, and push
            os.system('cd /Users/bhargav/Desktop/python/vscode/bhargavnufolder && git add . && git commit -m "Updated watch.py to automatically push changes to GitHub" && git push origin main')

if __name__ == "__main__":
    path = "/Users/bhargav/Desktop/python/vscode/bhargavnufolder"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    logging.info('Watcher started')

    try:
        while True:
            time.sleep(20)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
