import os
import sys
import time
import random
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source="C:/Users/Seema/Downloads"
dest="C:/Users/Seema/Downloads" # downloads/Image_Files/dogg.png

dir_tree={
    "Image_Files":['.jpg','.jpeg','.png','.gif'],
    "Video_Files":['.mpg','.mp2','.mpeg','.mpv','.mp4'],
    "Document_Files":['.ppt','.xls','.csv','.pdf','.txt'],
    "Setup_Files":['.exe','.bin','.cmd']
}


class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,ext=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                file_name=os.path.basename(event.src_path)
                print("Downloaded" + file_name)

                path1=source + '/' + file_name # downloads
                path2=dest + '/' + key  # downloads/Image_files
                path3=path2 + '/' + file_name # download/Image_Files/dog.png

                time.sleep(1)

                if os.path.exists(path2):
                    print("Moving "+file_name+"....")
                    shutil.move(path1,path3)
                else:
                    os.makedirs(path2)
                    print("Moving "+file_name+"....")
                    shutil.move(path1,path3)

event_handler=FileMovementHandler()
observer =Observer()
observer.schedule(event_handler,source,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
                    


