from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QPushButton, QLineEdit, QComboBox, QTableWidget,
    QTableWidgetItem, QMessageBox, QStackedWidget, QFrame,
    QHeaderView, QSpinBox, QDialog, QDialogButtonBox
)

import database
import enrollment


class EnrollmentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SHS Enrollment System")
        self.setMinimumSize(1100, 700)
        self.setStyleSheet("""
            QMainWindow, QWidget { background: #f5f7fb; color: #202938; font-family: Segoe UI; }
            #sidebar { background: #172033; }
            #brand { color: white; font-size: 22px; font-weight: bold; }
            #sidebarSubtitle { color: #aeb8c9; font-size: 12px; }
            QPushButton#navButton { color: #dce3ee; background: transparent; border: none; text-align: left; padding: 13px 18px; border-radius: 8px; font-size: 14px; }
            QPushButton#navButton:hover { background: #26334c; }
            QPushButton#primaryButton { background: #2563eb; color: white; border: none; padding: 11px 20px; border-radius: 7px; font-weight: bold; }
            QPushButton#primaryButton:hover { background: #1d4ed8; }
            QPushButton#dangerButton { background: #dc2626; color: white; border: none; padding: 9px 16px; border-radius: 7px; }
            QPushButton#secondaryButton { background: white; border: 1px solid #d6dce6; padding: 9px 16px; border-radius: 7px; }
            QLineEdit, QComboBox, QSpinBox { background: white; border: 1px solid #d5dbe5; border-radius: 6px; padding: 9px; min-height: 18px; }
            QLineEdit:focus, QComboBox:focus, QSpinBox:focus { border: 1px solid #2563eb; }
            QTableWidget { background: white; border: 1px solid #e0e5ec; border-radius: 8px; gridline-color: #edf0f4; }
            QHeaderView::section { background: #f1f4f8; padding: 10px; border: none; font-weight: bold; }
            #card { background: white; border: 1px solid #e3e7ee; border-radius: 10px; }
            #pageTitle { font-size: 26px; font-weight: bold; }
            #muted { color: #6b7280; }
            #statValue { font-size: 28px; font-weight: bold; }
        """)
        self.pages = QStackedWidget()
        self.setup_window()
        self.refresh_dashboard()
        self.refresh_students()

    def setup_window(self):
        central = QWidget()
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(220)
        side_layout = QVBoxLayout(sidebar)
        side_layout.setContentsMargins(18, 25, 18, 18)

        brand = QLabel("SHS Enrollment")
        brand.setObjectName("brand")
        subtitle = QLabel("Management System")
        subtitle.setObjectName("sidebarSubtitle")
        side_layout.addWidget(brand)
        side_layout.addWidget(subtitle)
        side_layout.addSpacing(35)

        for text, function in [
            ("Dashboard", self.show_dashboard),
            ("Enroll Student", self.show_enrollment),
            ("Enrolled Students", self.show_students),
            ("Settings", self.show_settings)
        ]:
            button = QPushButton(text)
            button.setObjectName("navButton")
            button.clicked.connect(function)
            side_layout.addWidget(button)

        side_layout.addStretch()
        exit_button = QPushButton("Exit")
        exit_button.setObjectName("navButton")
        exit_button.clicked.connect(self.close)
        side_layout.addWidget(exit_button)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.pages)
        self.setCentralWidget(central)

        self.dashboard_page = self.create_dashboard_page()
        self.enrollment_page = self.create_enrollment_page()
        self.students_page = self.create_students_page()
        self.settings_page = self.create_settings_page()

        for page in [self.dashboard_page, self.enrollment_page, self.students_page, self.settings_page]:
            self.pages.addWidget(page)

    def page_header(self, title, description):
        layout = QVBoxLayout()
        title_label = QLabel(title)
        title_label.setObjectName("pageTitle")
        description_label = QLabel(description)
        description_label.setObjectName("muted")
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        return layout

    def create_dashboard_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(35, 30, 35, 30)
        layout.addLayout(self.page_header("Dashboard", "Overview of the SHS enrollment system."))
        layout.addSpacing(20)

        cards = QHBoxLayout()
        self.total_value = QLabel("0")
        self.total_value.setObjectName("statValue")
        self.status_value = QLabel("OPEN")
        self.status_value.setObjectName("statValue")
        self.year_value = QLabel("2026-2027")
        self.year_value.setObjectName("statValue")
        cards.addWidget(self.create_stat_card("Total Students", self.total_value))
        cards.addWidget(self.create_stat_card("Enrollment Status", self.status_value))
        cards.addWidget(self.create_stat_card("School Year", self.year_value))
        layout.addLayout(cards)
        layout.addSpacing(25)

        card = QFrame()
        card.setObjectName("card")
        info_layout = QVBoxLayout(card)
        title = QLabel("System Overview")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        info = QLabel("The system manages SHS student enrollment, student records, track and strand selection, validation, and enrollment settings.")
        info.setWordWrap(True)
        info.setObjectName("muted")
        info_layout.addWidget(title)
        info_layout.addWidget(info)
        layout.addWidget(card)
        layout.addStretch()
        return page

    def create_stat_card(self, title, value_label):
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumHeight(125)
        layout = QVBoxLayout(card)
        label = QLabel(title)
        label.setObjectName("muted")
        layout.addWidget(label)
        layout.addWidget(value_label)
        return card

    def create_enrollment_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(35, 30, 35, 30)
        layout.addLayout(self.page_header("Student Enrollment", "Enter the student's information to create an enrollment record."))
        layout.addSpacing(15)

        card = QFrame()
        card.setObjectName("card")
        form = QFormLayout(card)
        form.setContentsMargins(25, 25, 25, 25)
        form.setVerticalSpacing(12)
        form.setHorizontalSpacing(25)

        self.student_id = QLineEdit()
        self.first_name = QLineEdit()
        self.middle_name = QLineEdit()
        self.last_name = QLineEdit()
        self.age = QSpinBox(); self.age.setRange(10, 100); self.age.setValue(16)
        self.gender = QComboBox(); self.gender.addItems(enrollment.GENDERS)
        self.grade_level = QComboBox(); self.grade_level.addItems(enrollment.GRADE_LEVELS)
        self.track = QComboBox(); self.track.addItems(enrollment.TRACKS); self.track.currentTextChanged.connect(self.update_strands)
        self.strand = QComboBox(); self.update_strands()
        self.contact = QLineEdit()
        self.address = QLineEdit()
        self.guardian = QLineEdit()

        for label, widget in [
            ("Student ID *", self.student_id), ("First Name *", self.first_name), ("Middle Name", self.middle_name),
            ("Last Name *", self.last_name), ("Age *", self.age), ("Gender *", self.gender),
            ("Grade Level *", self.grade_level), ("Track *", self.track), ("Strand *", self.strand),
            ("Contact Number *", self.contact), ("Address *", self.address), ("Guardian *", self.guardian)
        ]:
            form.addRow(label, widget)

        layout.addWidget(card)
        buttons = QHBoxLayout(); buttons.addStretch()
        clear_button = QPushButton("Clear"); clear_button.setObjectName("secondaryButton"); clear_button.clicked.connect(self.clear_form)
        enroll_button = QPushButton("Enroll Student"); enroll_button.setObjectName("primaryButton"); enroll_button.clicked.connect(self.submit_enrollment)
        buttons.addWidget(clear_button); buttons.addWidget(enroll_button)
        layout.addLayout(buttons); layout.addStretch()
        return page

    def update_strands(self):
        self.strand.clear()
        if self.track.currentText() == "Academic":
            self.strand.addItems(enrollment.ACADEMIC_STRANDS)
        else:
            self.strand.addItems(enrollment.TVL_STRANDS)

    def collect_student(self):
        return {
            "student_id": self.student_id.text().strip(), "first_name": self.first_name.text().strip(),
            "middle_name": self.middle_name.text().strip(), "last_name": self.last_name.text().strip(),
            "age": str(self.age.value()), "gender": self.gender.currentText(),
            "grade_level": self.grade_level.currentText(), "track": self.track.currentText(),
            "strand": self.strand.currentText(), "contact": self.contact.text().strip(),
            "address": self.address.text().strip(), "guardian": self.guardian.text().strip()
        }

    def submit_enrollment(self):
        student = self.collect_student()
        valid, message = enrollment.validate_student(student)
        if not valid:
            QMessageBox.warning(self, "Invalid Information", message)
            return
        success, message = enrollment.enroll_student(student)
        if success:
            QMessageBox.information(self, "Enrollment Successful", message)
            self.clear_form(); self.refresh_students(); self.refresh_dashboard()
        else:
            QMessageBox.warning(self, "Enrollment Failed", message)

    def clear_form(self):
        self.student_id.clear(); self.first_name.clear(); self.middle_name.clear(); self.last_name.clear()
        self.age.setValue(16); self.gender.setCurrentIndex(0); self.grade_level.setCurrentIndex(0)
        self.track.setCurrentIndex(0); self.update_strands(); self.contact.clear(); self.address.clear(); self.guardian.clear()

    def create_students_page(self):
        page = QWidget(); layout = QVBoxLayout(page); layout.setContentsMargins(35, 30, 35, 30)
        layout.addLayout(self.page_header("Enrolled Students", "Search, view, update, and delete enrollment records.")); layout.addSpacing(15)
        search_layout = QHBoxLayout()
        self.search = QLineEdit(); self.search.setPlaceholderText("Search by Student ID or name..."); self.search.textChanged.connect(self.refresh_students)
        refresh_button = QPushButton("Refresh"); refresh_button.setObjectName("secondaryButton"); refresh_button.clicked.connect(self.refresh_students)
        search_layout.addWidget(self.search); search_layout.addWidget(refresh_button); layout.addLayout(search_layout); layout.addSpacing(12)
        self.table = QTableWidget(); self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["Student ID", "Name", "Grade", "Track", "Strand", "Gender", "Contact", "Status"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers); self.table.setSelectionBehavior(QTableWidget.SelectRows); self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)
        actions = QHBoxLayout(); actions.addStretch()
        edit_button = QPushButton("Edit Selected"); edit_button.setObjectName("secondaryButton"); edit_button.clicked.connect(self.edit_selected)
        delete_button = QPushButton("Delete Selected"); delete_button.setObjectName("dangerButton"); delete_button.clicked.connect(self.delete_selected)
        actions.addWidget(edit_button); actions.addWidget(delete_button); layout.addLayout(actions)
        return page

    def refresh_students(self):
        if not hasattr(self, "table"): return
        students = database.get_students(self.search.text())
        self.table.setRowCount(len(students))
        for row, student in enumerate(students):
            values = [student["student_id"], student["first_name"] + " " + student["last_name"], student["grade_level"], student["track"], student["strand"], student["gender"], student["contact"], student["status"]]
            for column, value in enumerate(values):
                self.table.setItem(row, column, QTableWidgetItem(str(value)))

    def selected_student_id(self):
        row = self.table.currentRow()
        return self.table.item(row, 0).text() if row >= 0 else ""

    def edit_selected(self):
        student_id = self.selected_student_id()
        if not student_id:
            QMessageBox.warning(self, "No Selection", "Please select a student first."); return
        student = database.get_student(student_id)
        if student:
            dialog = EditStudentDialog(self, student)
            if dialog.exec_() == QDialog.Accepted:
                updated = dialog.get_student()
                valid, message = enrollment.validate_student({**updated, "student_id": student_id})
                if not valid:
                    QMessageBox.warning(self, "Invalid Information", message); return
                database.update_student(student_id, updated); self.refresh_students(); self.refresh_dashboard()

    def delete_selected(self):
        student_id = self.selected_student_id()
        if not student_id:
            QMessageBox.warning(self, "No Selection", "Please select a student first."); return
        answer = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this student record?", QMessageBox.Yes | QMessageBox.No)
        if answer == QMessageBox.Yes:
            database.delete_student(student_id); self.refresh_students(); self.refresh_dashboard()

    def create_settings_page(self):
        page = QWidget(); layout = QVBoxLayout(page); layout.setContentsMargins(35, 30, 35, 30)
        layout.addLayout(self.page_header("System Settings", "Manage school and enrollment configuration.")); layout.addSpacing(15)
        card = QFrame(); card.setObjectName("card"); form = QFormLayout(card); form.setContentsMargins(25, 25, 25, 25); form.setVerticalSpacing(15)
        self.school_name = QLineEdit(database.get_setting("school_name"))
        self.school_year = QLineEdit(database.get_setting("school_year"))
        self.enrollment_status = QComboBox(); self.enrollment_status.addItems(["OPEN", "CLOSED"]); self.enrollment_status.setCurrentText(database.get_setting("enrollment_status"))
        form.addRow("School Name", self.school_name); form.addRow("School Year", self.school_year); form.addRow("Enrollment Status", self.enrollment_status)
        layout.addWidget(card)
        buttons = QHBoxLayout(); buttons.addStretch(); save = QPushButton("Save Settings"); save.setObjectName("primaryButton"); save.clicked.connect(self.save_settings); buttons.addWidget(save); layout.addLayout(buttons); layout.addStretch()
        return page

    def save_settings(self):
        school_name = self.school_name.text().strip(); school_year = self.school_year.text().strip()
        if not school_name or not school_year:
            QMessageBox.warning(self, "Invalid Settings", "School name and school year are required."); return
        database.update_setting("school_name", school_name); database.update_setting("school_year", school_year); database.update_setting("enrollment_status", self.enrollment_status.currentText())
        self.refresh_dashboard(); QMessageBox.information(self, "Settings Saved", "System settings have been updated.")

    def refresh_dashboard(self):
        if not hasattr(self, "total_value"): return
        self.total_value.setText(str(database.get_student_count())); self.status_value.setText(database.get_setting("enrollment_status")); self.year_value.setText(database.get_setting("school_year"))

    def show_dashboard(self): self.refresh_dashboard(); self.pages.setCurrentWidget(self.dashboard_page)
    def show_enrollment(self): self.pages.setCurrentWidget(self.enrollment_page)
    def show_students(self): self.refresh_students(); self.pages.setCurrentWidget(self.students_page)
    def show_settings(self): self.pages.setCurrentWidget(self.settings_page)

    def closeEvent(self, event):
        answer = QMessageBox.question(self, "Exit Application", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No)
        event.accept() if answer == QMessageBox.Yes else event.ignore()


class EditStudentDialog(QDialog):
    def __init__(self, parent, student):
        super().__init__(parent); self.setWindowTitle("Edit Student"); self.setMinimumWidth(500)
        layout = QVBoxLayout(self); form = QFormLayout()
        self.first_name = QLineEdit(student["first_name"]); self.middle_name = QLineEdit(student["middle_name"] or ""); self.last_name = QLineEdit(student["last_name"])
        self.age = QSpinBox(); self.age.setRange(10, 100); self.age.setValue(student["age"])
        self.gender = QComboBox(); self.gender.addItems(enrollment.GENDERS); self.gender.setCurrentText(student["gender"])
        self.grade_level = QComboBox(); self.grade_level.addItems(enrollment.GRADE_LEVELS); self.grade_level.setCurrentText(student["grade_level"])
        self.track = QComboBox(); self.track.addItems(enrollment.TRACKS); self.track.setCurrentText(student["track"]); self.track.currentTextChanged.connect(self.update_strands)
        self.strand = QComboBox(); self.update_strands(); self.strand.setCurrentText(student["strand"])
        self.contact = QLineEdit(student["contact"]); self.address = QLineEdit(student["address"]); self.guardian = QLineEdit(student["guardian"])
        for label, widget in [("First Name *", self.first_name), ("Middle Name", self.middle_name), ("Last Name *", self.last_name), ("Age *", self.age), ("Gender *", self.gender), ("Grade Level *", self.grade_level), ("Track *", self.track), ("Strand *", self.strand), ("Contact *", self.contact), ("Address *", self.address), ("Guardian *", self.guardian)]: form.addRow(label, widget)
        layout.addLayout(form)
        buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel); buttons.accepted.connect(self.accept); buttons.rejected.connect(self.reject); layout.addWidget(buttons)

    def update_strands(self):
        self.strand.clear(); self.strand.addItems(enrollment.ACADEMIC_STRANDS if self.track.currentText() == "Academic" else enrollment.TVL_STRANDS)

    def get_student(self):
        return {"first_name": self.first_name.text().strip(), "middle_name": self.middle_name.text().strip(), "last_name": self.last_name.text().strip(), "age": str(self.age.value()), "gender": self.gender.currentText(), "grade_level": self.grade_level.currentText(), "track": self.track.currentText(), "strand": self.strand.currentText(), "contact": self.contact.text().strip(), "address": self.address.text().strip(), "guardian": self.guardian.text().strip()}
