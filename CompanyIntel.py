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
        self.company_name = ''
        self.en_name = ''
        self.incorporation_date = ''
        self.status = 'Active'
        self.company_type = ''
        self.is_governmental = False
        self.is_limited = False
        self.latest_annual_report = ''
        self.company_purpose = ''
        self.address = ''
        self.company_discription = ''

        self._extract_data(soup)

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

    def _extract_data(self, soup):
        """
        This function is used to extract the data from the soup object
        :param soup: the soup object
        :return: None
        """

        # get company name
        company_name = soup.find(text='שם חברה')
        company_name = company_name.parent.find_next_sibling()
        self.company_name = company_name.text

        # get english name
        en_name = soup.find(text='שם חברה באנגלית')
        en_name = en_name.parent.find_next_sibling()
        self.en_name = en_name.text

        # get launch date
        incorporation_date = soup.find(text='תאריך התאגדות')
        incorporation_date = incorporation_date.parent.find_next_sibling()
        self.incorporation_date = incorporation_date.text

        # get company status
        status = soup.find(text='סטאטוס')
        status = status.parent.find_next_sibling()
        self.status = status.text

        # get company type
        company_type = soup.find(text='סוג חברה')
        company_type = company_type.parent.find_next_sibling()
        self.company_type = company_type.text

        # get is governmental
        is_governmental = soup.find(text='סוג חברה ממשלתית')
        is_governmental = is_governmental.parent.find_next_sibling()
        self.is_governmental = is_governmental.text

        # get is limited
        is_limited = soup.find(text='סוג מגבלות')
        is_limited = is_limited.parent.find_next_sibling()
        self.is_limited = is_limited.text

        # get latest annual report
        latest_annual_report = soup.find(text='דוח שנתי שהוגש')
        latest_annual_report = latest_annual_report.parent.find_next_sibling()
        self.latest_annual_report = latest_annual_report.text

        # get company purpose
        company_purpose = soup.find(text='מטרות החברה')
        company_purpose = company_purpose.parent.find_next_sibling()
        self.company_purpose = company_purpose.text

        # get company address
        address = soup.find(text='כתובת')
        address = address.parent.find_next_sibling()
        self.address = address.text.strip().replace('\xa0', '')

        # get company discription
        company_discription = soup.find(text='תיאור חברה')
        company_discription = company_discription.parent.find_next_sibling()
        self.company_discription = company_discription.text

def get_companyID(company_name):
    """
    This function is used to get the company id from the website
    :param company_name: the company name
    :return: the company id
    """
    # create soup
    company_name = 'גוגל ישראל בע"מ'
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
