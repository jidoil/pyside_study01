from PySide2.QtWidgets import QWidget, QGroupBox, QCheckBox, QVBoxLayout, QButtonGroup, QRadioButton, QHBoxLayout


class CheckBoxWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBox and Radio Button")

        os = QGroupBox("Choose Operating System")
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)

        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(mac)
        os_layout.addWidget(linux)
        os.setLayout(os_layout)

        # exclusive checkboxes
        drinks = QGroupBox("Choose your drink")

        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True)

        exclusive_button_group = QButtonGroup(self)
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(coffee)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.setExclusive(True)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(coffee)
        drink_layout.addWidget(juice)
        drinks.setLayout(drink_layout)

        # Radio Buttons
        answers = QGroupBox("Choose Answer")
        answer_a =  QRadioButton("A")
        answer_b =  QRadioButton("B")
        answer_c =  QRadioButton("C")
        answer_a.setChecked(True)

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)
        answers.setLayout(answers_layout)


        # layout
        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answers)


        self.setLayout(v_layout)






    # func
    def windows_box_toggled(self, checked) :
        if checked :
            print("checked")
        else :
            print("not checked")

    def linux_box_toggled(self, checked) :
        if checked :
            print("checked")
        else :
            print("not checked")


    def mac_box_toggled(self, checked) :
        if checked :
            print("checked")
        else :
            print("not checked")