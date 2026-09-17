from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget
)

import database
import enrollment


class EnrollmentWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "SHS Enrollment System"
        )

        self.setMinimumSize(
            1100,
            750
        )

        self.create_ui()

        self.load_students()

    def create_ui(self):

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )

        main_layout = QVBoxLayout()

        central_widget.setLayout(
            main_layout
        )

        title = QLabel(
            "SHS ENROLLMENT SYSTEM"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        title.setStyleSheet("""
            QLabel {
                font-size: 26px;
                font-weight: bold;
                padding: 15px;
            }
        """)

        main_layout.addWidget(title)

        form = QFormLayout()

        self.student_id = QLineEdit()

        self.first_name = QLineEdit()

        self.middle_name = QLineEdit()

        self.last_name = QLineEdit()

        self.age = QLineEdit()


        self.gender = QComboBox()

        self.gender.addItems(
            enrollment.GENDERS
        )

        self.grade_level = QComboBox()

        self.grade_level.addItems(
            enrollment.GRADE_LEVELS
        )

        self.track = QComboBox()

        self.track.addItems(
            enrollment.TRACKS
        )

        self.track.currentTextChanged.connect(
            self.update_strands
        )

        self.strand = QComboBox()

        self.update_strands()

        self.contact = QLineEdit()

        self.address = QLineEdit()

        self.guardian = QLineEdit()


        form.addRow(
            "Student ID:",
            self.student_id
        )

        form.addRow(
            "First Name:",
            self.first_name
        )

        form.addRow(
            "Middle Name:",
            self.middle_name
        )

        form.addRow(
            "Last Name:",
            self.last_name
        )

        form.addRow(
            "Age:",
            self.age
        )

        form.addRow(
            "Gender:",
            self.gender
        )

        form.addRow(
            "Grade Level:",
            self.grade_level
        )

        form.addRow(
            "Track:",
            self.track
        )

        form.addRow(
            "Strand:",
            self.strand
        )

        form.addRow(
            "Contact Number:",
            self.contact
        )

        form.addRow(
            "Address:",
            self.address
        )

        form.addRow(
            "Guardian:",
            self.guardian
        )

        main_layout.addLayout(
            form
        )

        buttons = QHBoxLayout()


        enroll_button = QPushButton(
            "Enroll Student"
        )

        enroll_button.clicked.connect(
            self.enroll
        )

        clear_button = QPushButton(
            "Clear"
        )

        clear_button.clicked.connect(
            self.clear_form
        )

        update_button = QPushButton(
            "Update Selected"
        )

        update_button.clicked.connect(
            self.update_student
        )

        delete_button = QPushButton(
            "Delete Selected"
        )

        delete_button.clicked.connect(
            self.delete_student
        )

        buttons.addWidget(
            enroll_button
        )

        buttons.addWidget(
            clear_button
        )

        buttons.addWidget(
            update_button
        )

        buttons.addWidget(
            delete_button
        )

        main_layout.addLayout(
            buttons
        )

        label = QLabel(
            "ENROLLED STUDENTS"
        )

        label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                padding-top: 10px;
            }
        """)

        main_layout.addWidget(label)

        self.table = QTableWidget()

        self.table.setColumnCount(12)

        self.table.setHorizontalHeaderLabels([

            "Student ID",
            "First Name",
            "Middle Name",
            "Last Name",
            "Age",
            "Gender",
            "Grade Level",
            "Track",
            "Strand",
            "Contact",
            "Address",
            "Guardian"

        ])

        self.table.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        self.table.cellClicked.connect(
            self.select_student
        )


        main_layout.addWidget(
            self.table
        )

    def update_strands(self):

        self.strand.clear()

        if self.track.currentText() == "Academic":

            self.strand.addItems(
                enrollment.ACADEMIC_STRANDS
            )

        else:

            self.strand.addItems(
                enrollment.TVL_STRANDS
            )

    def get_form_data(self):

        student = {

            "student_id":
                self.student_id.text().strip(),

            "first_name":
                self.first_name.text().strip(),

            "middle_name":
                self.middle_name.text().strip(),

            "last_name":
                self.last_name.text().strip(),

            "age":
                self.age.text().strip(),

            "gender":
                self.gender.currentText(),

            "grade_level":
                self.grade_level.currentText(),

            "track":
                self.track.currentText(),

            "strand":
                self.strand.currentText(),

            "contact":
                self.contact.text().strip(),

            "address":
                self.address.text().strip(),

            "guardian":
                self.guardian.text().strip()

        }

        return student

    def enroll(self):
        student = self.get_form_data()

        success, message = (
            enrollment.enroll_student(
                student
            )
        )

        if success:

            QMessageBox.information(
                self,
                "Success",
                message
            )

            self.clear_form()
            self.load_students()

        else:

            QMessageBox.warning(
                self,
                "Enrollment Error",
                message
            )

    def load_students(self):

        students = database.get_students()

        self.table.setRowCount(
            len(students)
        )

        for row, student in enumerate(
            students
        ):

            values = [

                student["student_id"],
                student["first_name"],
                student["middle_name"],
                student["last_name"],
                student["age"],
                student["gender"],
                student["grade_level"],
                student["track"],
                student["strand"],
                student["contact"],
                student["address"],
                student["guardian"]

            ]

            for column, value in enumerate(
                values
            ):

                item = QTableWidgetItem(
                    str(value)
                )

                self.table.setItem(
                    row,
                    column,
                    item
                )

        self.table.resizeColumnsToContents()

    def select_student(
        self,
        row,
        column
    ):

        student_id_item = (
            self.table.item(row, 0)
        )

        if student_id_item is None:

            return

        student_id = (
            student_id_item.text()
        )

        student = database.get_student(
            student_id
        )

        if student is None:

            return

        self.student_id.setText(
            student["student_id"]
        )

        self.first_name.setText(
            student["first_name"]
        )

        self.middle_name.setText(
            student["middle_name"]
        )

        self.last_name.setText(
            student["last_name"]
        )

        self.age.setText(
            student["age"]
        )

        self.gender.setCurrentText(
            student["gender"]
        )

        self.grade_level.setCurrentText(
            student["grade_level"]
        )

        self.track.setCurrentText(
            student["track"]
        )

        self.strand.setCurrentText(
            student["strand"]
        )

        self.contact.setText(
            student["contact"]
        )

        self.address.setText(
            student["address"]
        )

        self.guardian.setText(
            student["guardian"]
        )

    def update_student(self):

        student_id = (
            self.student_id.text().strip()
        )

        if student_id == "":

            QMessageBox.warning(
                self,
                "Update Error",
                "Select a student first."
            )

            return

        student = self.get_form_data()

        valid, message = (
            enrollment.validate_student(
                student
            )
        )

        if not valid:

            QMessageBox.warning(
                self,
                "Update Error",
                message
            )

            return

        success, message = (
            database.update_student(
                student_id,
                student
            )
        )

        if success:

            QMessageBox.information(
                self,
                "Success",
                message
            )

            self.clear_form()
            self.load_students()

        else:

            QMessageBox.warning(
                self,
                "Update Error",
                message
            )

    def delete_student(self):
        row = self.table.currentRow()

        if row < 0:

            QMessageBox.warning(
                self,
                "Delete Error",
                "Select a student first."
            )

            return

        student_id = (
            self.table.item(
                row,
                0
            ).text()
        )

        answer = QMessageBox.question(

            self,
            "Confirm Delete",
            "Are you sure you want to delete this student?",

            QMessageBox.Yes |
            QMessageBox.No

        )

        if answer == QMessageBox.Yes:

            success, message = (
                database.delete_student(
                    student_id
                )
            )

            if success:
                QMessageBox.information(
                    self,
                    "Success",
                    message
                )

                self.clear_form()
                self.load_students()

            else:

                QMessageBox.warning(
                    self,
                    "Delete Error",
                    message
                )

    def clear_form(self):
        self.student_id.clear()
        self.first_name.clear()
        self.middle_name.clear()
        self.last_name.clear()
        self.age.clear()
        self.contact.clear()
        self.address.clear()
        self.guardian.clear()

        self.gender.setCurrentIndex(0)
        self.grade_level.setCurrentIndex(0)
        self.track.setCurrentIndex(0)
        self.update_strands()