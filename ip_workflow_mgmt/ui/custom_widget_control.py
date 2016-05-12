#Custom widget functions

def resize_scrollArea(self, docked):
    #this resizes the stack widget when you remove or replace the dock widget

    #get the width of the dock widget 
    dockWidth = self.dwTools.width()
    #get the width of the stack widget
    saWidth = self.width() 
    # if the dock widget is already docked add its width to the stack widget
    # if being docked, subtract it's width from the stack widget                    
    if docked == True:
        width = saWidth - 10
    else:
        width = saWidth - dockWidth - 10
    
    #leaving height alone for now, maybe someday in the future.
    self.scrollArea.resize(width, self.height() - 70)

def toggle_toolbar(self, event):
    #simple function to show or hide the tool bar.
    if self.dwTools.isVisible():
        self.dwTools.hide()
    else:
        self.dwTools.show()

def leSku_changed(self, le_txt):
    #dirty hack to force line edit to upper case.
    self.leSkuEnter.setText(le_txt.upper())