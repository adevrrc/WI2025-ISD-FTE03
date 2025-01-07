"""This module is used to demonstrate concepts from module 4."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

from user_interface.student_listing import StudentListing
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = StudentListing()
    mainWindow.show()
    sys.exit(app.exec())