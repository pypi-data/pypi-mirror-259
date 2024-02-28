import re
from typing import List
import requests
import bs4 as bs
from mcv_api.models import Course
class BaseSession:
    def __init__(self):
        self.session = requests.session() # create a session
        self.URL = 'https://www.mycourseville.com/'
        self.cookies = self.session.cookies
        self.cookies['has_js'] = '1'

class ChulaLogin(BaseSession):
    def __init__(self, username: str, password: str):
        super().__init__()
        try:
            self.username = username
            self.password = password
            self.front = self.session.get(self.URL + '/api/chulalogin')
            self.csrf_token = re.search(r'name="_token" value="(.+?)"', self.front.text).group(1)
            self.payload = {
                'username': self.username,
                'password': self.password,
                '_token': self.csrf_token,
                'remember': 'on',
            }
            # authenticate to get session
            r = self.session.post(self.URL + '/api/chulalogin', data=self.payload)
            soup = bs.BeautifulSoup(r.text, 'html.parser')
            # find redirector of CU login
            table = soup.find('table')
            redirector = table.find_all('tr')[1].find_all('td')[-1].find('a')['href']
            self.session.get(redirector)
            self.__validate_login()
        except Exception as e:
            raise ValueError('Login failed Highly likely due to invalid username or password')
    
    def __validate_login(self) -> bool:
        # check if the session is valid
        r = self.session.get(self.URL)
        # if logout button is found, then the session is valid
        if not 'logout' in r.text:
            raise ValueError('Invalid username or password, Login failed')
        else:
            return True
        
    def get_joined_courses(self) -> List[Course.MyCourse]:
        # get the list of joined courses
        r = self.session.get(self.URL)
        soup = bs.BeautifulSoup(r.text, 'html.parser')
        # find class courseville-courseicongroup
        semester_soups = soup.find_all('section', class_='courseville-courseicongroup')
        my_courses = []
        for a_semester_soup in semester_soups:
            # courseville-header class
            semester = a_semester_soup.find('div', class_='courseville-header').text
            course_s = a_semester_soup.find_all('div', {'data-info': True})
            
            all_semester_courses = []
            for course in course_s:
                # data-part="courseno"
                courseno = course.find('div', {'data-part': 'courseno'}).text
                title = course.find('div', {'data-part': 'title'}).text
                all_semester_courses.append(Course.Course(courseno, title))

            my_courses.append(Course.MyCourse(semester, all_semester_courses))
        return my_courses
        
