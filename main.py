from search import *
from PyQt5.QtWidgets import *
from lxml import etree as et
import webbrowser
import sys


# основна форма. ствоерння іконок, віджетів і кнопок.
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self._menubar()
        self.tree = 'data.xml'
        self.tree_ = et.parse(self.tree)
        self.flag = None
        self.file = ''
        self.names = {''}
        self.surnames = {''}
        self.patronyms = {''}
        self.faculties = {''}
        self.departments = {''}
        self.educations = {''}
        self.places = {''}
        self.days_begin = {''}
        self.months_begin = {''}
        self.years_begin = {''}
        self.days_end = {''}
        self.months_end = {''}
        self.years_end = {''}

        self.resize(1600, 700)
        self.setWindowTitle('Welcome!')

        self.build_box(self.tree_)

        self.text = QTextEdit(self)
        self.text.resize(880, 630)
        self.text.move(700, 50)

        self.name_file = QLabel('Current file:', self)
        self.name_file.move(485, 40)

        self.show_file = QTextEdit(self)
        self.show_file.move(425, 70)
        self.show_file.resize(200, 30)
        self.show_file.setText(self.tree)

        self.btn_transform = QPushButton('Transform', self)
        self.btn_transform.move(475, 120)
        self.btn_transform.resize(100, 40)
        self.btn_transform.clicked.connect(self.transform)

        self.name = QCheckBox('Name', self)
        self.name.move(10, 40)
        self.cmbname = QComboBox(self)
        self.add_items(self.cmbname, self.names)
        self.cmbname.move(90, 40)

        self.surname = QCheckBox('Surname', self)
        self.surname.move(10, 90)
        self.cmbsurname = QComboBox(self)
        self.add_items(self.cmbsurname, self.surnames)
        self.cmbsurname.move(90, 90)

        self.patronym = QCheckBox('Patronym', self)
        self.patronym.move(10, 130)
        self.cmbpatronym = QComboBox(self)
        self.add_items(self.cmbpatronym, self.patronyms)
        self.cmbpatronym.move(100, 135)

        self.faculty = QCheckBox('Faculty', self)
        self.faculty.move(10, 175)
        self.cmbfaculty = QComboBox(self)
        self.add_items(self.cmbfaculty, self.faculties)
        self.cmbfaculty.move(100, 178)

        self.department = QCheckBox('Department', self)
        self.department.move(10, 220)
        self.cmbdepartment = QComboBox(self)
        self.add_items(self.cmbdepartment, self.departments)
        self.cmbdepartment.move(110, 220)

        self.education = QCheckBox('Education', self)
        self.education.move(10, 265)
        self.cmbeducation = QComboBox(self)
        self.add_items(self.cmbeducation, self.educations)
        self.cmbeducation.move(110, 265)

        self.place = QCheckBox('Place of education', self)
        self.place.move(10, 290)
        self.place.resize(150, 70)
        self.cmbplace = QComboBox(self)
        self.add_items(self.cmbplace, self.places)
        self.cmbplace.move(150, 310)

#
        self.date_begin = QCheckBox('Date of begining', self)
        self.date_begin.move(10, 350)
        self.date_begin.resize(140, 30)

        self.day_begin_text = QLabel('Day', self)
        self.day_begin_text.move(45, 380)

        self.day_begin = QComboBox(self)
        self.add_items(self.day_begin, self.days_begin)
        self.day_begin.move(10, 410)

        self.month_begin_text = QLabel('Month', self)
        self.month_begin_text.move(160, 380)

        self.month_begin = QComboBox(self)
        self.add_items(self.month_begin, self.months_begin)
        self.month_begin.move(130, 410)

        self.year_begin_text = QLabel('Year', self)
        self.year_begin_text.move(285, 380)
        self.year_begin = QComboBox(self)
        self.add_items(self.year_begin, self.years_begin)
        self.year_begin.move(250, 410)

#
        self.date_end = QCheckBox('Date of ending', self)
        self.date_end.move(10, 450)
        self.date_end.resize(120, 30)

        self.day_end_text = QLabel('Day', self)
        self.day_end_text.move(45, 480)

        self.day_end = QComboBox(self)
        self.add_items(self.day_end, self.days_end)
        self.day_end.move(10, 510)
#

        self.month_end_text = QLabel('Month', self)
        self.month_end_text.move(160, 480)
        self.month_end = QComboBox(self)
        self.add_items(self.month_end, self.months_end)
        self.month_end.move(130, 510)

#
        self.year_end_text = QLabel('Year', self)
        self.year_end_text.move(285, 480)
        self.year_end = QComboBox(self)
        self.add_items(self.year_end, self.years_end)
        self.year_end.move(250, 510)



        self.rbt_dom = QRadioButton('DOM', self)
        self.rbt_dom.move(10, 550)
        self.rbt_dom.clicked.connect(self.rbt_dom_clicked)

        self.rbt_sax = QRadioButton('SAX', self)
        self.rbt_sax.move(10, 600)
        self.rbt_sax.clicked.connect(self.rbt_sax_clicked)

        self.rbt_bs = QRadioButton('Beautiful\n \t Soup', self)
        self.rbt_bs.move(10, 640)
        self.rbt_bs.resize(100, 40)
        self.rbt_bs.clicked.connect(self.rbt_bs_clicked)

        self.rbt_group = QButtonGroup()
        self.rbt_group.addButton(self.rbt_dom)
        self.rbt_group.addButton(self.rbt_sax)
        self.rbt_group.addButton(self.rbt_bs)

        self.btn_search = QPushButton('Search', self)
        self.btn_search.move(110, 595)
        self.btn_search.resize(100, 40)
        self.btn_search.clicked.connect(self.btn_search_clicked)

        self.btn_clear = QPushButton('Clean', self)
        self.btn_clear.move(260, 595)
        self.btn_clear.resize(100, 40)
        self.btn_clear.clicked.connect(self.btn_clear_clicked)


    def _menubar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu('&File', self)
        menuBar.addMenu(fileMenu)

        self.openAction = QAction('Open..', self)
        fileMenu.addAction(self.openAction)
        self.openAction.triggered.connect(self.search_file)
        self.openAction.triggered.connect(self.show_)

        helpMenu = menuBar.addAction('&Help')
        helpMenu.triggered.connect(self.help)


# змінити файл хмл
    def search_file(self):
        try:
            res = QFileDialog.getOpenFileName(self, 'Open File', '/home/liza/PycharmProjects/lab_2', 'XML File (*.xml)')
            self.file = res[0][33:]
            self.tree = self.file
            tree = et.parse(self.tree)
            persons = self.read(tree)
            persons.clear()
            self.btn_clear_clicked()

# чистимо множину всіх елементів для нових
            self.names.clear()
            self.surnames.clear()
            self.patronyms.clear()
            self.faculties.clear()
            self.departments.clear()
            self.educations.clear()
            self.places.clear()
            self.days_begin.clear()
            self.months_begin.clear()
            self.years_begin.clear()
            self.days_end.clear()
            self.months_end.clear()
            self.years_end.clear()

# чистимо комбобокси для нових елементів
            self.cmbname.clear()
            self.cmbsurname.clear()
            self.cmbpatronym.clear()
            self.cmbfaculty.clear()
            self.cmbdepartment.clear()
            self.cmbeducation.clear()
            self.cmbplace.clear()
            self.day_begin.clear()
            self.month_begin.clear()
            self.year_begin.clear()
            self.day_end.clear()
            self.month_end.clear()
            self.year_end.clear()

# будуємо за новим файлом бокси
            self.build_box(tree)

            self.add_items(self.cmbname, self.names)
            self.add_items(self.cmbsurname, self.surnames)
            self.add_items(self.cmbpatronym, self.patronyms)
            self.add_items(self.cmbfaculty, self.faculties)
            self.add_items(self.cmbdepartment, self.departments)
            self.add_items(self.cmbeducation, self.educations)
            self.add_items(self.cmbplace, self.places)
            self.add_items(self.day_begin, self.days_begin)
            self.add_items(self.month_begin, self.months_begin)
            self.add_items(self.year_begin, self.years_begin)
            self.add_items(self.day_end, self.days_end)
            self.add_items(self.month_end, self.months_end)
            self.add_items(self.year_end, self.years_end)

            self.cmbname.addItem('')
            self.cmbname.setCurrentText('')
            self.cmbsurname.addItem('')
            self.cmbsurname.setCurrentText('')
            self.cmbpatronym.addItem('')
            self.cmbpatronym.setCurrentText('')
            self.cmbfaculty.addItem('')
            self.cmbfaculty.setCurrentText('')
            self.cmbdepartment.addItem('')
            self.cmbdepartment.setCurrentText('')
            self.cmbeducation.addItem('')
            self.cmbeducation.setCurrentText('')
            self.cmbplace.addItem('')
            self.cmbplace.setCurrentText('')
            self.day_begin.addItem('')
            self.day_begin.setCurrentText('')
            self.month_begin.addItem('')
            self.month_begin.setCurrentText('')
            self.year_begin.addItem('')
            self.year_begin.setCurrentText('')
            self.day_end.addItem('')
            self.day_end.setCurrentText('')
            self.month_end.addItem('')
            self.month_end.setCurrentText('')
            self.year_end.addItem('')
            self.year_end.setCurrentText('')
        except Exception:
            sh = QMessageBox.information(self, '', 'You don\'t choose file!')

# допоміжна ф-я: додати до комбобоксів множину вибору
    def add_items(self, x: QComboBox, item: List):
        x.addItems(item)

# вивід ім'я файлу
    def show_(self):
        self.show_file.setPlainText(self.tree)

# help
    def help(self):
        help_text = QMessageBox.warning(self, 'Help',
                                        '<font size = 3>'
                                        '<ul><li><b>Menu:</b></li>'
                                        '<ul>'
                                        '<li>For each item you can choose value of its, just click on drop-down list</li>'
                                        '<li>You can change it in any moment you want to</li>'
                                        '<li>WARNING! You have to tick the suitable item to include it in searching</li>'
                                        '<li>You don\'t need to tick all of items</li></ul>'
                                        '<li><b>File:</b></li>'
                                        '<ul>'
                                        '<li>Choose File to change current .xml file</li>'
                                        '<li>Choose Transform to transform .xml file into .html</li>'
                                        '<li>Then you can click Yes! and see web-page in your web-browser</li></ul>'
                                        '<li><b>Searching:</b></li>'
                                        '<ul>'
                                        '<li>Choose DOM for searching by DOM-method</li>'
                                        '<li>Choose SAX for searching by SAX-method</li>'
                                        '<li>Choose the last one for searching by BS-method</li></ul>'
                                        '<li><b>Output:</b><li>'
                                        '<ul>'
                                        '<li>At the field on the right you can see the result of searching</li>'
                                        '</ul></font>')

# кнопка очистити
    def btn_clear_clicked(self):
        self.text.clear()
        self.name.setChecked(False)
        self.surname.setChecked(False)
        self.patronym.setChecked(False)
        self.faculty.setChecked(False)
        self.department.setChecked(False)
        self.education.setChecked(False)
        self.place.setChecked(False)
        self.date_begin.setChecked(False)
        self.date_end.setChecked(False)
        self.rbt_group.setExclusive(False)
        self.rbt_dom.setChecked(False)
        self.rbt_sax.setChecked(False)
        self.rbt_bs.setChecked(False)
        self.rbt_group.setExclusive(True)
        self.cmbname.setCurrentText('')
        self.cmbsurname.setCurrentText('')
        self.cmbpatronym.setCurrentText('')
        self.cmbfaculty.setCurrentText('')
        self.cmbdepartment.setCurrentText('')
        self.cmbeducation.setCurrentText('')
        self.cmbplace.setCurrentText('')
        self.day_begin.setCurrentText('')
        self.month_begin.setCurrentText('')
        self.year_begin.setCurrentText('')
        self.day_end.setCurrentText('')
        self.month_end.setCurrentText('')
        self.year_end.setCurrentText('')

# читаємо дані з хмл файлу, щоб заповнити комбобокси
    def read(self, tree):
        root1 = tree.getroot()
        children = root1.getchildren()
        persons = []
        for child1 in children:
            person = {}
            root2 = child1.getchildren()
            for child2 in root2:
                person[child2.tag] = child2.text
                root3 = child2.getchildren()
                date = {}
                for child3 in root3:
                    date[child3.tag] = child3.text
                    person[child2.tag] = date
            persons.append(person)
        return persons

# заповнюємо комбобокси
    def build_box(self, tree):
        for item in self.read(tree):
            self.names.add(item['name'])
            self.surnames.add(item['surname'])
            self.patronyms.add(item['patronym'])
            self.faculties.add(item['faculty'])
            self.departments.add(item['department'])
            self.educations.add(item['education'])
            self.places.add(item['place_educ'])
            self.days_begin.add(item['date_begin']['number'])
            self.months_begin.add(item['date_begin']['month'])
            self.years_begin.add(item['date_begin']['year'])
            self.days_end.add(item['date_end']['number'])
            self.months_end.add(item['date_end']['month'])
            self.years_end.add(item['date_end']['year'])

# тут зберігається вибрана інформація
    def info(self):
        info = [[]]
        info.pop(0)
        info = self.ischeck(self.name, self.cmbname, info)
        info = self.ischeck(self.surname, self.cmbsurname, info)
        info = self.ischeck(self.patronym, self.cmbpatronym, info)
        info = self.ischeck(self.faculty, self.cmbfaculty, info)
        info = self.ischeck(self.department, self.cmbdepartment, info)
        info = self.ischeck(self.education, self.cmbeducation, info)
        info = self.ischeck(self.place, self.cmbplace, info)
        info = self.is_check(self.date_begin, [self.day_begin, self.month_begin, self.year_begin], info)
        info = self.is_check(self.date_end, [self.day_end, self.month_end, self.year_end], info)
        return info

# відмітка на чекбоксі
    def ischeck(self, check: QCheckBox, inputi: QComboBox, info):
        if check.isChecked():
            info.append(str(inputi.currentText()))
        else:
            info.append('')
        return info

# відмітка для дат
    def is_check(self, check: QCheckBox, list_: List[QComboBox], info):
        if check.isChecked():
            info.append([str(list_[0].currentText()), str(list_[1].currentText()), str(list_[2].currentText())])
        else:
            info.append(['', '', ''])
        return info

    def rbt_dom_clicked(self):
        self.flag = 1

    def rbt_sax_clicked(self):
        self.flag = 2

    def rbt_bs_clicked(self):
        self.flag = 3

# кнопка пошуку
    def btn_search_clicked(self):
        self.text.clear()
        info = self.info()
        x = Info()
        if self.flag == 1:
            x.set_strategy(DOM())    # создание обьекта стратегии дом
            li = x.search_(self.tree, info)
            self.output(li)
        elif self.flag == 2:
            x.set_strategy(SAX())
            li = x.search_(self.tree, info)
            self.output(li)
        elif self.flag == 3:
            x.set_strategy(BS())
            li = x.search_(self.tree, info)
            self.output(li)

    def output(self, li):
        i = 0
        for item in li:
            i += 1
            self.text.append(f'{i}.'
                             f'<table border = "2" bordercolor = "#E0BFA6">'
                             f'<tr>'
                             f'<th rowspan = "3" align = "center">Name</th>'
                             f'<th rowspan = "3" align = "center">Surname</th>'
                             f'<th rowspan = "3" align = "center">Patronym</th>'
                             f'<th rowspan = "3" align = "center">Faculty</th>'
                             f'<th rowspan = "3" align = "center">Department</th>'
                             f'<th rowspan = "3" align = "center">Education</th>'
                             f'<th rowspan = "3" align = "center">Place of education</th>'
                             f'<th align = "center">Day of beginning of education</th>'
						     f'<th align = "center">Day of ending of education</th>'
                             f'</tr>'
                             f'<tr>'
						     f'<th align = "center">Month of beginning of education</th>'
						     f'<th align = "center">Month of ending of education</th>'
					         f'</tr>'
					         f'<tr>'
						     f'<th align = "center">Year of beginning of education</th>'
						     f'<th align = "center">Year of ending of education</th>'
					         f'</tr>'
                             f'<tr><td rowspan = "3" align = "center">'
                             f'{item.name}</td>'
                             f'<td rowspan = "3" align = "center">'
                             f'{item.surname}</td>'
                             f'<td rowspan = "3" align = "center">'
                             f'{item.patronym}</td>'
                             f'<td rowspan = "3" align = "center">'
                             f'{item.faculty}</td>'
                             f'<td rowspan = "3" align = "center">'
                             f'{item.department}</td>'
                             f'<td rowspan = "3" align = "center">'
                             f'{item.education}</td>'
                             f'<td rowspan = "3" align = "center">'
                             f'{item.place}</td>'
                             f'<td align = "center">'
                             f'{item.date_begin[0]}</td>'
                             f'<td align = "center">'
                             f'{item.date_end[0]}</td>'
                             f'<tr><td align = "center">'
                             f'{item.date_begin[1]}</td>'
                             f'<td align = "center">'
                             f'{item.date_begin[2]}</td></tr>'
                             f'<tr><td align = "center">'
                             f'{item.date_end[1]}</td>'
                             f'<td align = "center">'
                             f'{item.date_end[2]}</td></tr></tr>'
                             f'</table>')

    def transform(self):
        if self.tree == '':
            window = QMessageBox.information(self, '', '<font color = red><b>Error</b></font>')
        else:
            dom = et.parse(self.tree)
            xslt = et.parse('data.xsl')
            transform = et.XSLT(xslt)
            new_dom = transform(dom)
            new_dom.write("output.html", pretty_print=True)

            res = QMessageBox.question(self, '', 'Transformation done! \nOpen file?')
            if res == QMessageBox.Yes:
                webbrowser.open('output.html')
            else:
                print('')

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(qApp.exec_())
