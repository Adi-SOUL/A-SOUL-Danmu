from PyQt5.QtWidgets import QApplication
import sys
from ui import Window
import asyncio

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())