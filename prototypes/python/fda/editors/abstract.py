from abc import abstractmethod
from typing import TypeVar
from tkinter import Frame
from tkinter import Misc
from tkinter import Button
from tkinter import Variable
from tkinter import Listbox
from tkinter import LEFT
from tkinter import Y
from tkinter import END
from tkinter import BOTH
from ..objects.abstract import AbstractObject
from ..forms.abstract import AbstractForm

O = TypeVar('O', bound=AbstractObject)
F = TypeVar('F', bound=AbstractForm)

class AbstractEditor(Frame):

    def __init__(self, master: Misc=None):
        Frame.__init__(self, master)

        self.objects: list[AbstractObject] = []

        # Container for left sidebar

        self.left = Frame(self)
        self.left.pack(side=LEFT, fill=Y)

        # Container for horizontal alignment of buttons

        self.buttons = Frame(self.left)
        self.buttons.pack()

        # Button for adding tools

        def handleButtonAddClick():
            # Create the new object
            object: O = self.createObject()
            # Remember the new object
            self.objects.insert(0, object)
            # List and select the new object
            self.listbox.insert(0, object.getName())
            self.listbox.selection_clear(0, END)
            self.listbox.selection_set(0)
            self.listbox.event_generate("<<ListboxSelect>>")

        self.buttonAdd = Button(self.buttons, text='Add', command=handleButtonAddClick)
        self.buttonAdd.pack(side=LEFT)

        # Button for removing tools
        
        def handleButtonRemoveClick():
            # Get selection index
            index = self.listbox.curselection()
            # Check selection index
            if index:
                # Get selected object
                object = self.objects[index[0]]
                # Delete the object
                self.objects.remove(object)
                # Unlist the object
                self.listbox.delete(index[0])
                # Unset the object
                self.right.setObject(None)

        self.buttonRemove = Button(self.buttons, text='Remove', command=handleButtonRemoveClick)
        self.buttonRemove.pack(side=LEFT)

        # List of tools
        
        def handleListboxSelect(event):
            # Get selection index
            index = self.listbox.curselection()
            # Check selection index
            if index:
                # Get selected object
                object = self.objects[index[0]]
                # Set selected object
                self.right.setObject(object)

        self.variable = Variable(value=())

        self.listbox = Listbox(self.left, listvariable=self.variable)
        self.listbox.pack(expand=True, fill=Y)
        self.listbox.bind('<<ListboxSelect>>', handleListboxSelect)

        # Right

        self.right: F = self.createForm()
        self.right.pack(expand=True, fill=BOTH)

    @abstractmethod
    def createObject(self) -> O:
        pass

    @abstractmethod
    def createForm(self) -> F:
        pass
