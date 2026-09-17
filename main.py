import sys

import database
from PyQt5.QtWidgets import QApplication

from gui import EnrollmentWindow

def main():
    database.initialize_database()

    app = QApplication(sys.argv)

    window = EnrollmentWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()