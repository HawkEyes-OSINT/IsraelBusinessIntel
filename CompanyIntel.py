# This class is used to extract company data from the website: https://datacheck.co.il/company.a
import requests
from bs4 import BeautifulSoup

class company_data:
    """
    This class is used to extract company data from the website: https://datacheck.co.il/company.ai
    The class is used to extract the following data:
    - company name
    - english name
    - launch date
    - status
    - company type
    - is governmental
    - is limited
    - latest annual report
    - company purpose
    - address
    - company discription
    """
    def __init__(self, company_id):
        soup = self._extract_soup(company_id)

        self.company_id = company_id
        self.company_name = self._extract_data(soup, 'שם חברה')
        self.en_name = self._extract_data(soup, 'שם חברה באנגלית')
        self.incorporation_date = self._extract_data(soup, 'תאריך התאגדות')
        self.status = self._extract_data(soup, 'סטאטוס')
        self.company_type = self._extract_data(soup, 'סוג חברה')
        self.is_governmental = self._extract_data(soup, 'סוג חברה ממשלתית')
        self.is_limited = self._extract_data(soup, 'סוג מגבלות')
        self.latest_annual_report = self._extract_data(soup, 'דוח שנתי שהוגש')
        self.company_purpose = self._extract_data(soup, 'מטרות החברה')
        self.address = self._extract_data(soup, 'כתובת')
        self.company_discription = self._extract_data(soup, 'תיאור חברה')

    def _extract_soup(self, company_id):
        """
        This function is used to extract the data from the website
        :param company_id: the company id
        :return: the soup object
        """
        url = f"https://datacheck.co.il/company.ai?id={company_id}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def _extract_data(self, soup, search_text):
        """
        This function is used to extract the data from the website
        :param soup: the soup object
        :param search_text: the search text
        :return: the data from the website
        """
        company_discription = soup.find(text=search_text)
        company_discription = company_discription.parent.find_next_sibling()
        if company_discription:
            return company_discription.text.strip().replace('\xa0', '')
        else:
            return ''


def get_companyID(company_name):
    """
    This function is used to get the company id from the website
    :param company_name: the company name
    :return: the company id
    """
    # create soup
    company_name = company_name.replace(' ', '-').replace('"','')
    url = f"https://israeli-companies.com/hevra/מידע-על-{company_name}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
        
    # extract company id
    title_tag = soup.find('title')
    title_tag.text
    title_tag = title_tag.text.split(' ')
    company_id = title_tag[-7]
    
    return company_id

"""
Test Code
"""
# print(get_companyID('גוגל ישראל בע"מ'))
# test_company = company_data(get_companyID('גוגל ישראל בע"מ'))
# print(test_company.company_name)
# print(test_company.en_name)
# print(test_company.incorporation_date)
# print(test_company.status)
# print(test_company.company_type)
# print(test_company.is_governmental)
# print(test_company.is_limited)
# print(test_company.latest_annual_report)
# print(test_company.company_purpose)
# print(test_company.address)
# print(test_company.company_discription)
# print(test_company.company_id)
