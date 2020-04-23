import json
from tkinter import *

with open('scene.json') as json_file:
    data = json.load(json_file)
    for scene in data['scenes']:
        print('Scene Name: ' + scene['scene_name'])
        print('created by: ' + scene['created_by'])
        for frame in scene['frames']:
            print('Frame Name: ' + frame['frame_name'])
            

root = Tk()

myLabel1 = Label(root, text="1")
myLabel2 = Label(root, text="2")


myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

root.mainloop()
