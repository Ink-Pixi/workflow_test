import sys
import ctypes
import getpass
from ui import Ui_mwWorkFlow
from create_web_art import CreateWebArt
from design_info import DesignInfo
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout, QLineEdit,\
    QCheckBox, QHBoxLayout, QFrame
from PyQt5.QtCore import QCoreApplication, Qt
#Your biological and technological distinctiveness will be added to our own. Resistance is futile.
        
class WorkflowApp(QMainWindow, Ui_mwWorkFlow):
    designInfo = DesignInfo()
    
    def __init__(self):
        super(WorkflowApp, self).__init__()
        
        self.setupUi(self)
        
        #Connect widgets to functions (signals and slots).
        #Buttons
        self.btnRunAll.clicked.connect(self.run_all)
        self.btnShowRunAll.clicked.connect(self.change_stack_widget)
        self.btnHome.clicked.connect(self.change_stack_widget)
        self.btnShowSku.clicked.connect(self.change_stack_widget)
        self.btnLoadSku.clicked.connect(self.btnLoadSku_Clicked)
        #line edit
        self.leSkuEnter.textChanged.connect(self.leSku_changed)
        #Tool bar dock widget
        self.dwTools.topLevelChanged.connect(self.resize_scrollArea)
        #Connect menu actions to slots...
        self.actionQuit.triggered.connect(QApplication.quit)
        self.actionTools.triggered.connect(self.toggle_toolbar)
        
        #get user name, in case we need it for any reason
        self.uName = getpass.getuser()
        #as a safety in case the .ui file is saved on a stack other than "home"
        self.stackWorkFlow.setCurrentIndex(0)
        #set title for first stack widget.
        self.lblWelcome.setText('Welcome, ' + self.uName[:-1].title() + '.')        
        
    def run_all(self):
        #get's all the active queues
        skus = self.designInfo.get_skus()
        print(skus)
        
        toRun = []
        if self.chkAllStatic.isChecked():
            toRun.append('static')
        if self.chkAllPng.isChecked():
            toRun.append('png')
        if not self.chkAllStatic.isChecked() and not self.chkAllPng.isChecked():
            QMessageBox.information(self, 'Hey Copernicus...', 'Hey Copernicus...Check at least one of the boxes.', QMessageBox.Ok)
        
        if toRun:
            self.setEnabled(False)            
            for sku in skus:
                for run in toRun:
                    try:
                        CreateWebArt(run, sku)
                    except BaseException as e:
                        error = str(e).split(',')
                        print('shit be broke for design: ' + sku + ' man, and here\'s why: \n', error[4] )
            self.setEnabled(True)

    def btnLoadSku_Clicked(self):
        names = self.designInfo.get_art_name_types()
        self.cbNameTypes.setEnabled(True)   
        self.gbGarments.setEnabled(True)
        #self.label.setEnabled(True)
        self.cbNameTypes.addItems(names)
        garms = self.designInfo.get_invetories_names(self.leSkuEnter.text())
        self.add_garm_widgets(garms)
    
    def add_garm_widgets(self, garms):
        hbGarms = QHBoxLayout()
        
        vbGarms = {}
        lblGarm = {}
        hbGarmRow = {}
        leGarm = {}
        chkGarm = {}
        
        for i in range(0,1):
            #beginning of var loop should go here.
            vbGarms[i] = QVBoxLayout()
            for garm in garms:
                lblGarm[garm[0]] = QLabel(garm[0])
                #lblGarm[garm[0]].setAlignment(Qt.AlignRight)
                lblGarm[garm[0]].setObjectName(garm[0].replace(' ', '').replace("'", "").replace("-", "").lower())
                leGarm[garm[0]] = QLineEdit()
                leGarm[garm[0]].setMaximumWidth(150)
                leGarm[garm[0]].setMinimumWidth(150)
                #leGarm[garm[0]].setAlignment(Qt.AlignRight)
                chkGarm[garm[0]] = QCheckBox()
                
                hbGarmRow = QHBoxLayout()
                hbGarmRow.addWidget(lblGarm[garm[0]])
                hbGarmRow.setAlignment(lblGarm[garm[0]], Qt.AlignRight)
                hbGarmRow.addWidget(leGarm[garm[0]])
                hbGarmRow.setAlignment(leGarm[garm[0]], Qt.AlignRight)
                hbGarmRow.addWidget(chkGarm[garm[0]])
                hbGarmRow.setAlignment(chkGarm[garm[0]], Qt.AlignRight)
                #hbGarmRow.addStretch(1)
                
                vbGarms[i].addLayout(hbGarmRow)
                #vbGarms[i].setAlignment(Qt.AlignRight)
                #vbGarms[i].setAlignment(hbGarmRow, Qt.AlignRight)  
                #vbGarms[i].addStretch(1)                                 
                print(lblGarm[garm[0]].objectName())
            
            hbGarms.addLayout(vbGarms[i])
            #hbGarms.setAlignment(Qt.AlignRight)
        shit = QFrame()
        shit.setLayout(hbGarms)
        self.scrollGarms.setWidget(shit)
        fuck = QHBoxLayout()
        fuck.addWidget(self.scrollGarms)
        self.gbGarments.setLayout(fuck)
                    
    def resize_scrollArea(self, docked):
        #this resizes the scroll area when you remove or replace the dock widget

        #get the width of the dock widget 
        dockWidth = self.dwTools.width()
        #get the width of the stack widget
        saWidth = self.width() 
        # if the dock widget is already docked add its width to the stack widget
        # if being docked, subtract it's width from the stack widget                    
        if docked == True:
            width = saWidth -3
        else:
            width = saWidth - dockWidth -3
        
        #leaving height alone for now, maybe someday in the future.
        self.scrollArea.resize(width, self.height() -20)
       
    def resizeEvent(self, resizeEvent):

        if self.dwTools.isFloating() == False:
            width = self.width() - self.dwTools.width() -3
            height = self.height() -20                
        else:
            width = self.width() -3
            height = self.height() -20
        
        self.scrollArea.resize(width, height)
        
    def toggle_toolbar(self, event):
        #simple function to show or hide the tool bar.
        if self.dwTools.isVisible():
            self.dwTools.hide()
        else:
            self.dwTools.show()
    
    def leSku_changed(self, le_txt):
        #dirty hack to force line edit to upper case.
        self.leSkuEnter.setText(le_txt.upper())
        
    def change_stack_widget(self):
        btn = self.sender().objectName()
        
        if btn == 'btnHome':
            self.stackWorkFlow.setCurrentIndex(0)
            #add a welcome message and the users name
            self.lblWelcome.setText('Welcome, ' + self.uName[:-1].title() + '.')            
        elif btn == 'btnShowRunAll':
            self.stackWorkFlow.setCurrentIndex(1)
            #self.lblTitle.setText('Run All Designs')
        elif btn == 'btnShowSku':
            self.stackWorkFlow.setCurrentIndex(2)
            self.leSkuEnter.setFocus()
            self.leSkuEnter.returnPressed.connect(self.btnLoadSku_Clicked)        

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