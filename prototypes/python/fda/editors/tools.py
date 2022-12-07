from tkinter import Misc
from .abstract import AbstractEditor
from ..objects.tool import ToolObject
from ..forms.tool import ToolForm

class ToolsEditor(AbstractEditor):

    def __init__(self, master: Misc=None):
        AbstractEditor.__init__(self, master)
    
    def createObject(self) -> ToolObject:
        return ToolObject(f'New tool type {len(self.objects) + 1}')
    
    def createForm(self) -> ToolForm:
        return ToolForm(self)
    