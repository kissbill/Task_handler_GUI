#PyQt, check multiple check boxes
#Please follow any one of the below line. I hope you can achieve your result. 

#1. Find the all QCheckBox in UI.
#OR
#2. Put all QCheckBox to one QGroupBox(QCheckBox become child of this QGroupBox), then find the QCheckBox Childern of QGroupBox. 
#OR
#3. Put all QCheckBox to any layouts like QHBoxLayout, QVBoxLayout, QGridLayout (QCheckBox become child of particular Layout), 
# then find the QCheckBox Childern of particular Layout.

#If your are not expecting this answer, sorry.
#Thanks, Subin


class MainUi(QtGui.QMainWindow):


  def __init__(self):       
    super(MainUi, self).__init__()
    self.ui = Ui.Ui_MainWindow()
    self.ui.setupUi(self)
    self.xmon = xmon2.MainUi()
    self.xmon.show()
    self.timer = XTimer(1)


    #Selection of generation to run
    self.connect(self.ui.checkBoxGen2, QtCore.SIGNAL("clicked()"), self.gen2Selected)
    self.connect(self.timer, QtCore.SIGNAL("tick"), self.onEventTick)
    self.connect(self.ui.checkBoxGen3, QtCore.SIGNAL("clicked()"), self.gen3Selected)

    #Select RS232 or CAN
    self.connect(self.ui.checkBoxCAN, QtCore.SIGNAL("clicked()"), self.canSelected)
    self.connect(self.ui.checkBoxRS232, QtCore.SIGNAL("clicked()"), self.rs232Selected)

    #Select single test or continuous test
    self.connect(self.ui.checkBoxConTest, QtCore.SIGNAL("clicked()"), self.conTestSelected)
    self.connect(self.ui.checkBoxSingTest, QtCore.SIGNAL("clicked()"), self.singTestSelected)

    #The RUN button is pressed
    self.connect(self.ui.pushButtonRun, QtCore.SIGNAL("clicked()"), self.runButtonPushed)

    self.connect(self.ui.pushButtonRunGen3, QtCore.SIGNAL("clicked()"), self.runButtonGen3Pressed)

    self.timer.start()




    #1. This case it will affect all the check box in your UI
    checkBoxList = self.ui.findChildern (QtGui.QCheckBox)
    for loop in range (len(checkBoxList)) :
      if checkBoxList[loop].ischecked() :
        Unit1 = create_unit(self, loop+1 , self.ui.lineEditComUnit1Gen2.text() 


    #2. Put all QCheckBox to one QGroupBox
    checkBoxList = self.ui.myGroup.findChildern (QtGui.QCheckBox)
    for loop in range (len(checkBoxList)) :
      if checkBoxList[loop].ischecked() :
        Unit1 = create_unit(self, loop+1 , self.ui.lineEditComUnit1Gen2.text() 


    #3. Put all QCheckBox to any layouts (QHBoxLayout, QVBoxLayout, QGridLayout)
    checkLoop  = 1
    for loop in range (self.ui.layouts.count ()) :
      currentWidget  = self.ui.layouts.itemAt(loop).widget()
      if type(currentWidget)==QtGui.QCheckBox :
         if checkBoxList[loop].ischecked() :
            Unit1 = create_unit(self, checkLoop, self.ui.lineEditComUnit1Gen2.text() 
            checkLoop+=1



    '''
    if self.ui.checkBoxUnit1Gen2.ischecked():
      Unit1 = create_unit(self, 1 , self.ui.lineEditComUnit1Gen2.text() 

    if self.ui.checkBoxUnit2Gen2.ischecked():
      Unit2 = create_unit(self, 2 , self.ui.lineEditComUnit2Gen2.text() 

    if self.ui.checkBoxUnit3Gen2.ischecked():
      Unit3 = create_unit(self, 3 , self.ui.lineEditComUnit3Gen2.text() 

    if self.ui.checkBoxUnit4Gen2.ischecked():
      Unit4 = create_unit(self, 4 , self.ui.lineEditComUnit4Gen2.text() 
    '''