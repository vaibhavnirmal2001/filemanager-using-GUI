from tkinter import *
from PIL import ImageTk, Image
import shutil
import os
import easygui
import pygame


from tkinter import filedialog
from tkinter import messagebox as mb


def open_window():
    read = easygui.fileopenbox()
    return read

def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")

def copy_file():
    source1 = open_window()
    destination1 = filedialog.askdirectory()
    shutil.copy(source1, destination1)
    mb.showinfo('confirmation', "File Copied !")


def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
        mb.showinfo('confirmation', "File Deleted !")
    else:
        mb.showinfo('confirmation', "File not found !")


def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension = os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName = input()
    path = os.path.join(path1, newName + extension)
    print(path)
    os.rename(chosenFile, path)
    mb.showinfo('confirmation', "File Renamed !")


def move_file():
    source = open_window()
    destination = filedialog.askdirectory()
    if (source == destination):
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', "File Moved !")


def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of new folder")
    newFolder = input()
    path = os.path.join(newFolderPath, newFolder)
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")


def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)

    mb.showinfo('confirmation', "Folder Deleted !")


def list_files():
    folderList = filedialog.askdirectory()
    sortlist = sorted(os.listdir(folderList))
    i = 0
    print("Files in ", folderList, "folder are:")
    while (i < len(sortlist)):
        print(sortlist[i] + '\n')
        i += 1

print("\n \t<<\tWELCOME TO AVA FILE EXPLORER MENU\t>>\n \t>>>This mini project is created by :")

class Queue:
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enQueue(self, x):
		self.s1.append(x)

	def deQueue(self):

		if len(self.s1) == 0 and len(self.s2) == 0:
			print("Q is Empty")
			return

		elif len(self.s2) == 0 and len(self.s1) > 0:
			while len(self.s1):
				temp = self.s1.pop()
				self.s2.append(temp)
			return self.s2.pop()

		else:
			return self.s2.pop()

if __name__ == '__main__':
	q = Queue()
	q.enQueue('\t>>> Vaibhav Nirmal \tID:(19007058)')
# 	q.enQueue('\t>>> Aditi Nimkar  \tID:(19007062)')
# 	q.enQueue('\t>>> Anusha Sahi  \tID:(19007053)')

	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())

root = Tk()
root.geometry("495x700")
root.maxsize(495,700);root.minsize(400,600);
root.title("My Group Project using GUI")
root.configure(background="darkorchid3")
Label(root, text="Created by Vaibhav, Anusha ,Aditi", font=("Helvetica 10 bold"), fg="black", padx="100", pady="15", bg="gray39"
      , relief=RAISED
      , borderwidth="5").grid(row=95, column=2)

Label(root, text="  AVA File Explorer Menu     ", font=("Helvetica 16 bold"), fg="black", padx="100", pady="30", bg="gray"
      , relief=RAISED, borderwidth="10").grid(row=5, column=2)

Button(root, text="Open a File", command=open_file, padx="20", pady="5", borderwidth="10", bg="black", fg="white",
       font=("Helvetica 16 bold")).grid(row=15, column=2)

Button(root, text="Copy a File", command=copy_file, padx="20", pady="5", borderwidth="10", bg="black", fg="white",
       font=("Helvetica 16 bold")).grid(row=25, column=2)

Button(root, text="Delete a File", command=delete_file, padx="20", pady="5", borderwidth="10", bg="black", fg="white",
       font=("Helvetica 16 bold")).grid(row=35, column=2)

Button(root, text="Rename a File", command=rename_file, padx="20", pady="5", borderwidth="10", bg="black", fg="white",
       font=("Helvetica 16 bold")).grid(row=45, column=2)

Button(root, text="Move a File", command=move_file, padx="20", pady="5", borderwidth="10", bg="black", fg="white",
       font=("Helvetica 16 bold")).grid(row=55, column=2)

Button(root, text="Make a Folder", command=make_folder, padx="20", pady="5", borderwidth="10", bg="black", fg="white",
       font=("Helvetica 16 bold")).grid(row=75, column=2)

Button(root, text="Remove a Folder", command=remove_folder, padx="20", pady="5", borderwidth="10", bg="black",
       fg="white", font=("Helvetica 16 bold")).grid(row=65, column=2)

Button(root, text="List all Files in Directory", command=list_files, padx="20", pady="5", borderwidth="10", bg="black",
       fg="white", font=("Helvetica 16 bold")).grid(row=85, column=2)
root.mainloop()



