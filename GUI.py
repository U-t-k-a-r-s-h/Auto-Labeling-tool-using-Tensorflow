import PySimpleGUI as sg
import cv2
import os
from PIL import Image
import TensorflowScript as API
size = 300,300
directory = 'C:/'  #random image which is loaded as default image
#im = Image.open(directory)
#im.thumbnail(size, Image.ANTIALIAS)
#im2 = im.save('Photo.png')
#directory = 'Photo.png'             #PysimpleGUI cant display jpeg images properly so converted that same image to png format
index=0
def Next_Image(path,index,dirn,window):   # this function shows the next image of the directory
    index=index+1
    window.close()
    directories = cvt_image(dirn+'/'+path[index])
    gui(directories,size,path,dirn,index)
def cvt_image(directory):          #this function converts the jpg images to png for displaying only
    im = Image.open(directory)
    im.thumbnail(size, Image.ANTIALIAS)
    im2 = im.save('Photo.png')      # a copy of the original image is taken to be displayed
    directory = 'Photo.png'         
    return directory

def Previous_Image(path,index,dirn,window): #this function if called for displaying the previous image in the same directory
    if index!=0:
        index=index-1
    window.close()
    directories = cvt_image(dirn+'/'+path[index])
    gui(directories,size,path,dirn,index)

def call_detector(window2,Threshold,model):   # this function calls the object detector script
    API.Detector('Photo.png',float(Threshold),model)
    window2.Close()
    directory = 'Temp.jpg'
    im = Image.open(directory)
    im.thumbnail(size, Image.ANTIALIAS)
    im2 = im.save('Photo2.png')
    directory = 'Photo2.png'
    gui(directory,size,path,dirn,index)

def gui(directory,size,path,dirn,index):  #this function creates the GUI 
    layout = [[sg.Text('Threshold', size=(8, 1)), sg.InputText('0.3')],[sg.Input(key='_FILEBROWSE_', enable_events=True, visible=False)],
            [sg.OK()],[sg.FileBrowse(target='_FILEBROWSE_')],
            [sg.Image(filename=directory)],[sg.Button('Next Image'), sg.Button('Previous Image'), sg.Button('Detect'),
            sg.Exit()], [sg.Listbox(values=('FRCNN.pb', 'Mobilenet.pb','SSD.pb'), size=(30, 3))]  ]

    window = sg.Window('ORIGINAL').Layout(layout)
    
    while True:             # Event Loop
        event, values = window.Read()
        if event in (None, 'Exit'):
            exit()
            break
        if event == 'Next Image':
            Next_Image(path,index,dirn,window)
        elif event == 'Detect':
            Threshold = values[0]
            if len(str(values.get(2)))<=2:
                model = 'FRCNN.pb'
            else :
                model = str(values.get(2)[0])
            call_detector(window,Threshold,model)
        elif event == 'Previous Image':
            Previous_Image(path,index,dirn,window)
        elif event == 'OK':
            print(values.get(2))
        elif event == '_FILEBROWSE_':
            directory=values.get('Browse')
            dirn = os.path.dirname(directory)
            path = dirn
            path = os.listdir(path)
            window.Close()
            directory = cvt_image(directory)
            gui(directory,size,path,dirn,index)         
    window.close()
def gui_init(directory,size,path,dirn,index):  #this function creates the GUI 
    layout = [[sg.Input(key='_FILEBROWSE_', enable_events=True, visible=False)],
            [sg.OK()],[sg.FileBrowse(target='_FILEBROWSE_')],
            [sg.Exit()]  ]

    window = sg.Window('ORIGINAL').Layout(layout)
    
    while True:             # Event Loop
        event, values = window.Read()
        if event in (None, 'Exit'):
            exit()
            break
        elif event == '_FILEBROWSE_':
            directory=values.get('Browse')
            dirn = os.path.dirname(directory)
            path = dirn
            path = os.listdir(path)
            window.Close()
            directory = cvt_image(directory)
            gui(directory,size,path,dirn,index)         
    window.close()
       
path = os.getcwd()
dirn = os.getcwd()
gui_init(directory,size,path,dirn,index)
if os.path.exists('Photo.png')=='True':   # to delete those temporary images
    os.remove('Photo.png')
if os.path.exists('Photo2.png')=='True':
    os.remove('Photo2.png')
    
    
