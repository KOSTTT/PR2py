from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        filename : str = event.src_path.replace("E:\Колледж\Python\PR2", "").replace(".txt", "").lower()
        for char in filename:
            if char in "sdf":
                print(char)
            else:
                print(char.upper())
        print()


observer = Observer()
observer.schedule(Handler(), path="E:\Колледж\Python\PR2")
observer.start()
while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()
    print("Stop")
