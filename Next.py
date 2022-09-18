from PyQt5.QtWidgets import QApplication
from main import main
import sys






app=QApplication([])

kullanicilar=main()
kullanicilar.show()


app.exec_()



