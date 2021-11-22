from abc import ABC, abstractmethod
from typing import List
from lxml import etree as et
import xml.sax
from bs4 import BeautifulSoup



class IStrategy(ABC):
    @abstractmethod
    def search(self, path, info):
        pass

#DOM
class DOM(IStrategy):
    def search(self, path, info):
        road = et.parse(path)
        root1 = road.getroot()
        children = root1.getchildren()
        res = []
        for child1 in children:
            inf = Info()
            flag = True
            root2 = child1.getchildren()
            if info[0] == '' or root2[0].text == info[0]:
                inf.name = root2[0].text
            else:
                flag = False

            if info[1] == '' or root2[1].text == info[1]:
                inf.surname = root2[1].text
            else:
                flag = False

            if info[2] == '' or root2[2].text == info[2]:
                inf.patronym = root2[2].text
            else:
                flag = False

            if info[3] == '' or root2[3].text == info[3]:
                inf.faculty = root2[3].text
            else:
                flag = False

            if info[4] == '' or root2[4].text == info[4]:
                inf.department = root2[4].text
            else:
                flag = False

            if info[5] == '' or root2[5].text == info[5]:
                inf.education = root2[5].text
            else:
                flag = False

            if info[6] == '' or root2[6].text == info[6]:
                inf.place = root2[6].text
            else:
                flag = False
            if info[7][0] == '' or root2[7][0].text == info[7][0]:
                inf.date_begin.append(root2[7][0].text)
            else:
                flag = False
            if info[7][1] == '' or root2[7][1].text == info[7][1]:
                inf.date_begin.append(root2[7][1].text)
            else:
                flag = False

            if info[7][2] == '' or root2[7][2].text == info[7][2]:
                inf.date_begin.append(root2[7][2].text)
            else:
                flag = False


            if info[8][0] == '' or root2[8][0].text == info[8][0]:
                inf.date_end.append(root2[8][0].text)
            else:
                flag = False

            if info[8][1] == '' or root2[8][1].text == info[8][1]:
                inf.date_end.append(root2[8][1].text)
            else:
                flag = False

            if info[8][2] == '' or root2[8][2].text == info[8][2]:
                inf.date_end.append(root2[8][2].text)
            else:
                flag = False


            if flag:
                res.append(inf)
        return res

# SAX
class SAX(IStrategy):
    def search(self, path, info):
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        handler = InfoHandler(info)
        parser.setContentHandler(handler)
        parser.parse(path)
        return handler.res


class InfoHandler(xml.sax.ContentHandler):
    def __init__(self, info):
        self.info = info   # инфа в виде списка того, что мы выбрали
        self.res = []
        self.current = ''
        self.name = ''
        self.surname = ''
        self.patronym = ''
        self.faculty = ''
        self.department = ''
        self.education = ''
        self.place = ''
        self.date_begin = ['', '', '']
        self.date_end = ['', '', '']
        self.inf = object
        self.flag = True
        self.flag1 = True
        self.flag2 = True
        self.flagg = True

    def startElement(self, tag, attrs):
        self.current = tag

    def endElement(self, tag):
        if tag == 'name':
            infi = Info()
            self.flag = True
            self.inf = infi
        if self.current == 'name' and (self.info[0] == '' or self.info[0] == self.name):
            self.inf.name = self.name
        elif self.current == 'name':
            self.flag = False

        if self.current == 'surname' and (self.info[1] == '' or self.info[1] == self.surname):
            self.inf.surname = self.surname
        elif self.current == 'surname':
            self.flag = False

        if self.current == 'patronym' and (self.info[2] == '' or self.info[2] == self.patronym):
            self.inf.patronym = self.patronym
        elif self.current == 'patronym':
            self.flag = False

        if self.current == 'faculty' and (self.info[3] == '' or self.info[3] == self.faculty):
            self.inf.faculty = self.faculty
        elif self.current == 'faculty':
            self.flag = False

        if self.current == 'department' and (self.info[4] == '' or self.info[4] == self.department):
            self.inf.department = self.department
        elif self.current == 'department':
            self.flag = False

        if self.current == 'education' and (self.info[5] == '' or self.info[5] == self.education):
            self.inf.education = self.education
        elif self.current == 'education':
            self.flag = False

        if self.current == 'place_educ' and (self.info[6] == '' or self.info[6] == self.place):
            self.inf.place = self.place
            self.flag1 = False
            self.flag2 = False
        elif self.current == 'place_educ':
            self.flag = False

        if self.current == 'number' and (self.info[7][0] == '' or self.info[7][0] == self.date_begin[0])\
                and not self.flag1:
            self.inf.date_begin.append(self.date_begin[0])
        elif self.current == 'number' and not self.flag1:
            self.flag = False

        if self.current == 'month' and (self.info[7][1] == '' or self.info[7][1] == self.date_begin[1])\
                and not self.flag1:
            self.inf.date_begin.append(self.date_begin[1])
        elif self.current == 'month' and not self.flag1:
            self.flag = False

        if self.current == 'year' and (self.info[7][2] == '' or self.info[7][2] == self.date_begin[2])\
                and not self.flag1 and not self.flag2:
            self.inf.date_begin.append(self.date_begin[2])
            self.flag1 = True
        elif self.current == 'year' and not self.flag1 and not self.flag2:
            self.flag = False

        if self.current == 'number' and (self.info[8][0] == '' or self.info[8][0] == self.date_end[0])\
                and self.flag1:
            self.inf.date_end.append(self.date_end[0])
        elif self.current == 'number' and self.flag1:
            self.flag = False

        if self.current == 'month' and (self.info[8][1] == '' or self.info[8][1] == self.date_end[1]) \
                and self.flag1:
            self.inf.date_end.append(self.date_end[1])
            self.flag2 = True
        elif self.current == 'month' and self.flag1:
            self.flag = False

        if self.current == 'year' and (self.info[8][2] == '' or self.info[8][2] == self.date_end[2])\
                and self.flag1 and self.flag2:
            self.inf.date_end.append(self.date_end[2])
            if self.flag:
                self.res.append(self.inf)
        elif self.current == 'year' and self.flag1 and self.flag2:
            self.flag = False

        self.current = ""

    def characters(self, content):
        if self.current == 'name':
            self.name = content
        elif self.current == 'surname':
            self.surname = content
        elif self.current == 'patronym':
            self.patronym = content
        elif self.current == 'faculty':
            self.faculty = content
        elif self.current == 'department':
            self.department = content
        elif self.current == 'education':
            self.education = content
        elif self.current == 'place_educ':
            self.place = content
        elif self.current == 'date_begin':
            self.flagg = False
        elif self.current == 'number' and not self.flagg:
            self.date_begin[0] = content
        elif self.current == 'month' and not self.flagg:
            self.date_begin[1] = content
        elif self.current == 'year' and not self.flagg:
            self.date_begin[2] = content
            self.flagg = True
        elif self.current == 'number' and self.flagg:
            self.date_end[0] = content
        elif self.current == 'month' and self.flagg:
            self.date_end[1] = content
        elif self.current == 'year' and self.flagg:
            self.date_end[2] = content


#Bs
class BS(IStrategy):
    def search(self, path, info):
        with open(path, "r") as file:
            content = file.readlines()
            content = "".join(content)
            soup = BeautifulSoup(content, 'lxml')
            res = []
            name = soup.find_all('name')
            surname = soup.find_all('surname')
            patronym = soup.find_all('patronym')
            faculty = soup.find_all('faculty')
            department = soup.find_all('department')
            education = soup.find_all('education')
            place = soup.find_all('place_educ')

            days = soup.find_all('number')
            months = soup.find_all('month')
            years = soup.find_all('year')
            i = 0

            for n, item in enumerate(name):
                inf = Info()
                flag = True
                if info[0] == item.text or info[0] == '':
                    inf.name = item.text
                else:
                    flag = False
                if info[1] == surname[n].text or info[1] == '':
                    inf.surname = surname[n].text
                else:
                    flag = False
                if info[2] == patronym[n].text or info[2] == '':
                    inf.patronym = patronym[n].text
                else:
                    flag = False
                if info[3] == faculty[n].text or info[3] == '':
                    inf.faculty = faculty[n].text
                else:
                    flag = False
                if info[4] == department[n].text or info[4] == '':
                    inf.department = department[n].text
                else:
                    flag = False
                if info[5] == education[n].text or info[5] == '':
                    inf.education = education[n].text
                else:
                    flag = False
                if info[6] == place[n].text or info[6] == '':
                    inf.place = place[n].text
                else:
                    flag = False

                if info[7][0] == days[n + i].text or \
                        info[7][0] == '':
                    inf.date_begin.append(days[n + i].text)
                else:
                    flag = False

                if info[7][1] == months[n + i].text or \
                        info[7][1] == '':
                    inf.date_begin.append(months[n + i].text)
                else:
                    flag = False

                if info[7][2] == years[n + i].text or \
                        info[7][2] == '':
                    inf.date_begin.append(years[n + i].text)
                else:
                    flag = False

                if info[8][0] == days[n + 1 + i].text or \
                        info[8][0] == '':
                    inf.date_end.append(days[n + 1 + i].text)
                else:
                    flag = False

                if info[8][1] == months[n + 1 + i].text or \
                        info[8][1] == '':
                    inf.date_end.append(months[n + 1 + i].text)
                else:
                    flag = False

                if info[8][2] == years[n + 1 + i].text or \
                        info[8][2] == '':
                    inf.date_end.append(years[n + 1 + i].text)
                else:
                    flag = False
                i += 1
                if flag:
                    res.append(inf)
            return res

# контекст
class Info:
    name: str
    surname: str
    patronym: str
    faculty: str
    department: str
    education: str
    place: str
    date_begin: list
    date_end: list
    strategy: IStrategy

    def __init__(self):
        self.name = ''
        self.surname = ''
        self.patronym = ''
        self.faculty = ''
        self.department = ''
        self.education = ''
        self.place = ''
        self.date_begin = []
        self.date_end = []

    def set_strategy(self, strategy: IStrategy):
        self.strategy = strategy

    def search_(self, path, info) -> List:
        return self.strategy.search(path, info)
