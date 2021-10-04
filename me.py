import gi
import subprocess
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class Main:
    def __init__(self):
        gladeFile = "ss.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        
        self.builder.connect_signals(self)
        window = self.builder.get_object("Main")

        window.show()
    def file1Hand(self,widget):
        toPrint=self.builder.get_object("result")
        toPrint.set_text('Processing ....')
        fileChoosed = self.builder.get_object("file1")
        self.file1 = fileChoosed.get_filename()
        print(self.file1)
        fileChoosed = self.builder.get_object("file2")
        self.file2 = fileChoosed.get_filename()
        print(self.file2)
        self.file1=self.file1+'"'
        self.file1='"'+self.file1
        self.file2=self.file2+'"'
        self.file2='"'+self.file2
        self.output=self.output+'"'
        self.output='"'+self.output
        
        query = 'pdftk '+self.file1+' '+self.file2+' cat '+'output '+self.output
        os.system(query)
        p='File saved in '+self.output
        toPrint.set_text(p)
    def saveZenity(self,widget):
        list_files = subprocess.check_output(["kdialog", "--getsavefilename", "."])
        self.output=list_files.decode("utf-8")[:-1]
        print(self.output)
    
        #toPrint.set_text(textFile)
    def gtk_main_quit(self,widget,data=None):
        Gtk.main_quit()  


if __name__ =="__main__":
    main = Main()
    Gtk.main()
    

