import sys
import ctypes
from ui import Ui_mwWorkFlow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
        
class WorkflowApp(QMainWindow, Ui_mwWorkFlow):
    def __init__(self):
        super(WorkflowApp, self).__init__()
        
        self.setupUi(self)
        
    def resizeEvent(self, resizeEvent):
        print(resizeEvent)
 
        if self.dwTools.isFloating() == False:
            width = self.width() - self.dwTools.width()
            height = self.height() - 70                
            print(width, height)
            self.scrollArea.resize(width, height)
        else:
            self.scrollArea.resize(self.width() - 0, self.height() -70)        

                   
if __name__ == "__main__":
    # The following line is to make the venv work with PyQt5....
    QCoreApplication.setLibraryPaths(['C:/workspace/venv/illustrator-virt/Lib/site-packages/PyQt5/plugins'])
            
    myappid = 'Workflow App'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    app = QApplication(sys.argv)
    app.setStyle("plastique")
    
    wf = WorkflowApp()
    wf.show()
    
    sys.exit(app.exec_())