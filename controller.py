from PyQt5.QtWidgets import *
from view_file import *
from calculator import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    A class containing the logic that allows the GUI
    to function correctly. Includes methods to program
    the submit and clear buttons along with a method to
    display the calculation results in the window and finally
    a method to manipulate the colors of the text entry boxes.
    """


    def __init__(self, *args, **kwargs):
        """
        Constructor that initializes the GUI
        and connects the submit and clear buttons
        to mouse clicks.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.submit_button.clicked.connect(lambda: self.submit())
        self.clear_button.clicked.connect(lambda: self.clear())



    def fetch_data(self, grade_percentage: float, letter_grade: str):
        """
        Method to check how the grade should be displayed
        and then display the final grade calculation.
        :param grade_percentage: The final calculated grade percentage.
        :param letter_grade: The final converted letter grade result.
        """
        if self.percent_button.isChecked() and grade_percentage > 0:
            self.output_box.setText('Your final grade would be ' + f'{grade_percentage:.2f}')
        elif self.letter_button.isChecked() and grade_percentage > 0:
            self.output_box.setText('Your final grade would be ' + f'{letter_grade}')


    def clear_color(self):
        """
        Method to reset the background colors of the
        line entry boxes back to white.
        """
        self.grade_1.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.grade_2.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.grade_3.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.grade_4.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.grade_5.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.grade_6.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.weight_1.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.weight_2.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.weight_3.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.weight_4.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.weight_5.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.weight_6.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.assign_1.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.assign_2.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.assign_3.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.assign_4.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.assign_5.setStyleSheet(f'background-color: rgb(255, 255, 255);')
        self.assign_6.setStyleSheet(f'background-color: rgb(255, 255, 255);')



    def submit(self):
        """
        Method that checks the data that has been entered
        and computes the final grade percentage and letter
        grade passing it then to self.fetch_data. Includes
        exception handling to validate the user input and
        display error messages if necessary.
        """
        grade_percentage = 0
        letter_grade = 'P'
        self.clear_color()
        try:
            if self.check_1.isChecked():
                first_category = self.assign_1.text()

                first_grade = float(self.grade_1.text())
                first_weight = float(self.weight_1.text())
                grade_percentage = compute1(first_weight, first_grade)

            if self.check_2.isChecked():
                second_category = self.assign_2.text()

                second_grade = float(self.grade_2.text())
                second_weight = float(self.weight_2.text())
                grade_percentage = compute2(first_weight, first_grade, second_weight, second_grade)


            if self.check_3.isChecked():
                third_category = self.assign_3.text()

                third_grade = float(self.grade_3.text())
                third_weight = float(self.weight_3.text())
                grade_percentage = compute3(first_weight, first_grade, second_weight, second_grade, third_weight, third_grade)


            if self.check_4.isChecked():
                fourth_category = self.assign_4.text()\

                fourth_grade = float(self.grade_4.text())
                fourth_weight = float(self.weight_4.text())
                grade_percentage = compute4(first_weight, first_grade, second_weight, second_grade, third_weight, third_grade, fourth_weight, fourth_grade)




            if self.check_5.isChecked():
                fifth_category = self.assign_5.text()

                fifth_grade = float(self.grade_5.text())
                fifth_weight = float(self.weight_5.text())
                grade_percentage = compute5(first_weight, first_grade, second_weight, second_grade, third_weight, third_grade, fourth_weight, fourth_grade, fifth_weight, fifth_grade)


            if self.check_6.isChecked():
                sixth_category = self.assign_6.text()

                sixth_grade = float(self.grade_6.text())
                sixth_weight = float(self.weight_6.text())
                grade_percentage = compute6(first_weight, first_grade, second_weight, second_grade, third_weight, third_grade, fourth_weight, fourth_grade, fifth_weight, fifth_grade, sixth_weight, sixth_grade)



            if grade_percentage == 0:
                self.output_box.setText('You must enter data in at least one row and check the box in order to calculate.\n\n' + 'Also, grade and weight boxes must contain numeric values between\n0 and 100, no letters.')



            if 96.5 <= grade_percentage <= 100:
                letter_grade = 'A+'
            elif 92.5 <= grade_percentage < 96.5:
                letter_grade = 'A'
            elif 89.5 <= grade_percentage < 92.5:
                letter_grade = 'A-'
            elif 86.5 <= grade_percentage < 89.5:
                letter_grade = 'B+'
            elif 82.5 <= grade_percentage < 86.5:
                letter_grade = 'B'
            elif 79.5 <= grade_percentage < 82.5:
                letter_grade = 'B-'
            elif 76.5 <= grade_percentage < 79.5:
                letter_grade = 'C+'
            elif 72.5 <= grade_percentage < 76.5:
                letter_grade = 'C'
            elif 69.5 <= grade_percentage < 72.5:
                letter_grade = 'C-'
            elif 66.5 <= grade_percentage < 69.5:
                letter_grade = 'D+'
            elif 62.5 <= grade_percentage < 66.5:
                letter_grade = 'D'
            elif 59.5 <= grade_percentage < 62.5:
                letter_grade = 'D-'
            elif grade_percentage < 59.5:
                letter_grade = 'F'


            self.fetch_data(grade_percentage, letter_grade)



        except ValueError:
            self.output_box.setText('Grade and weight boxes must contain numeric values\nbetween 0 and 100, no letters.')
            self.grade_1.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.grade_2.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.grade_3.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.grade_4.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.grade_5.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.grade_6.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_1.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_2.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_3.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_4.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_5.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_6.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_1.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_2.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_3.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_4.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_5.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_6.setStyleSheet(f'background-color: rgb(255, 100, 100);')

        except UnboundLocalError:
            self.output_box.setText('Every previous row from the last one you enter data in must have\ndata entered and the box checked.')
            self.grade_1.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.grade_2.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.grade_3.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.grade_4.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.grade_5.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.grade_6.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_1.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_2.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_3.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_4.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_5.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.weight_6.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_1.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_2.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_3.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_4.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_5.setStyleSheet(f'background-color: rgb(255, 100, 100);')
            self.assign_6.setStyleSheet(f'background-color: rgb(255, 100, 100);')






    def clear(self):
        """
        Method to clear all currently entered data
        from the application including all checked boxes
        and resets the grade display radio buttons to
        the default value. Also clears the text from
        the window and calls self.clear_color.
        """
        self.assign_1.clear()
        self.assign_2.clear()
        self.assign_3.clear()
        self.assign_4.clear()
        self.assign_5.clear()
        self.assign_6.clear()
        self.grade_1.clear()
        self.grade_2.clear()
        self.grade_3.clear()
        self.grade_4.clear()
        self.grade_5.clear()
        self.grade_6.clear()
        self.weight_1.clear()
        self.weight_2.clear()
        self.weight_3.clear()
        self.weight_4.clear()
        self.weight_5.clear()
        self.weight_6.clear()

        if self.letter_button.isChecked():
            self.percent_button.setChecked(True)

        if self.check_1.isChecked():
            self.check_1.setChecked(False)
        if self.check_2.isChecked():
            self.check_2.setChecked(False)
        if self.check_3.isChecked():
            self.check_3.setChecked(False)
        if self.check_4.isChecked():
            self.check_4.setChecked(False)
        if self.check_5.isChecked():
            self.check_5.setChecked(False)
        if self.check_6.isChecked():
            self.check_6.setChecked(False)

        self.clear_color()
        self.output_box.clear()




