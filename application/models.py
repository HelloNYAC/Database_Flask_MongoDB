# CST8333 - Programing Research Project
# Section: 350
# Semester: 22W
# Professor: Leanne Seaward
# Student name: Nicole Yue
# Student ID: 040991455
# Student Email: yue00015@algonquinlive.com
# Assignment 4

# this is the object constructor with all parameters needed to create one row of the table
# It included all rows listed as required, including:
class Record:
    def __init__(self, incident_num, incident_typ, report_date, nearest_centre, province, company, substance,
                 significant, category):
        '''
        :param incident_num:
        :param incident_typ:
        :param report_date:
        :param nearest_centre:
        :param province:
        :param company:
        :param substance:
        :param significant:
        :param category:
        '''
        super()
        self.incident_num = incident_num
        self.incident_typ = incident_typ
        self.report_date = report_date
        self.nearest_centre = nearest_centre
        self.province = province
        self.company = company
        self.substance = substance
        self.significant = significant
        self.category = category

    # getter of incident_num to return incident_num value
    def getincident_num(self):
        '''
        method: getincident_num
        :return: incident_num
        '''
        return self.incident_num

    # setter of incident_num to take incident_num as a parameter
    def setincident_num(self, incident_num):
        '''
        method: setincident_num
        :param incident_num:
        :return:
        '''
        self.incident_num = incident_num

    # getter of incident_typ to return incident_typ value
    def getincident_typ(self):
        '''
        method: getincident_typ
        :return: incident_typ
        '''
        return self.incident_typ

    # setter of incident_typ to take incident_typ as a parameter
    def setincident_typ(self, incident_typ):
        '''
        method: setincident_typ
        :param incident_typ:
        :return:
        '''
        self.incident_typ = incident_typ

    # getter of report_date to return report_date value
    def getreport_date(self):
        '''
        method: getreport_date
        :return: report_date
        '''
        return self.report_date

    # setter of report_date to take report_date as a parameter
    def setreport_date(self, report_date):
        '''
        method: setreport_date
        :param report_date:
        :return:
        '''
        self.report_date = report_date

    # getter of nearest_centre to return nearest_centre value
    def getnearest_centre(self):
        '''
        method: getnearest_centre
        :return: nearest_centre
        '''
        return self.nearest_centre

    # setter of nearest_centre to take nearest_centre as a parameter
    def setnearest_centre(self, nearest_centre):
        '''
        method: setnearest_centre
        :param nearest_centre:
        :return:
        '''
        self.nearest_centre = nearest_centre

    # getter of province to return province value
    def getprovince(self):
        '''
        method: getprovince
        :return: significant
        '''
        return self.province

    # setter of province to take province as a parameter
    def setprovince(self, province):
        '''
        method: setprovince
        :param province:
        :return:
        '''
        self.province = province

    # getter of company to return company value
    def getcompany(self):
        '''
        method: getcompany
        :return: significant
        '''
        return self.company

    # setter of company to take company as a parameter
    def setcompany(self, company):
        '''
        method: setcompany
        :param company:
        :return:
        '''
        self.company = company

    # getter of substance to return substance value
    def getsubstance(self):
        '''
        method: getsubstance
        :return: significant
        '''
        return self.substance

    # setter of substance to take substance as a parameter
    def setsubstance(self, substance):
        '''
        method: setsubstance
        :param substance:
        :return:
        '''
        self.substance = substance

    # getter of significant to return significant value
    def getsignificant(self):
        '''
        method: getsignificant
        :return: significant
        '''
        return self.significant

    # setter of significant to take significant as a parameter
    def setsignificant(self, significant):
        '''
        method: setsignificant
        :param significant:
        :return:
        '''
        self.significant = significant

        # getter of category to return category value

    def getcategory(self):
        '''
        method: getcategory
        :return: category
        '''
        return self.category

    # setter of category to take category as a parameter
    def setcategory(self, category):
        '''
        method: setcategory
        :param category:
        :return:
        '''
        self.category = category

    def obj_to_list(self):
        '''
        method object_to_list is to convert an Record object to a list with the object value
        this method is created for future use.
        '''
        obj_val = [self.getincident_num(), self.getincident_typ(), self.getreport_date(),
                   self.getnearest_centre(), self.getprovince(),
                   self.getcompany(), self.getsubstance(), self.getsignificant(),
                   self.getcategory()]
        return obj_val

    def asdict(self):
        return {"Incident Number": self.getincident_num(),
                "Incident Types": self.getincident_typ(),
                "Reported Date": self.getreport_date(),
                "Nearest Populated Centre": self.getnearest_centre(),
                "Province": self.getprovince(),
                "Company": self.getcompany(),
                "Substance": self.getsubstance(),
                "Significant": self.getsignificant(),
                "What happened category": self.getcategory()
                }

