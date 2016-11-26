from gui import *
from my_mqtt import *
import thread
import sys
import time

def link2(self):
    server_name=self.Mqtt_server.text()
    Username=self.username.text()
    Password=self.password.text()
    Port=self.port.text()
    topic=self.lineEdit.text()
    client_id=self.client.text()

    print "server_name " + server_name + " \nUsername " + Username + " \nPassword " + Password + "\nPort " + Port + "\ntopic " + topic + "\nclient_id " + client_id
    update(server_name,Username,Password,Port,topic,client_id)
    tx("a")


    

if __name__ == "__main__":
    thread.start_new_thread(loop,())
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    print "sala bloack ho gaya"
    sys.exit(app.exec_())
    print "sala bloack ho gaya"
    

def loop():
    print "naya thread to start ho gaya"
    mqttc.loop_forever()
    
def guiloop(a):

    print a
    
    print "khjuk"
    
