import requests
import string
import urllib.parse
from bs4 import BeautifulSoup
from CompanyIntel import company_data


class companies_owned:
    def __init__(self, owner_name):
        """
        This class is used to extract the data from the website
        :param company_id: the company id
        """
        soup = self._extract_soup(owner_name)
        self.companies = self._extract_data(soup)

    def _extract_soup(self, owner_name):
        """
        This function is used to extract the data from the website
        :param company_id: the company id
        :return: the soup object
        """
        # check input language
        if not all(char in string.ascii_letters for char in owner_name):
            # encode the owner_name
            owner_name = urllib.parse.quote(owner_name, encoding='ISO-8859-8')
        else:
            owner_name = owner_name.replace(' ', '+')

        # get soup via url
        url = f'https://datacheck.co.il/CompaniesOwner.ai?name={owner_name}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def _extract_data(self, soup):
        """
        This function is used to extract the data from the website
        :param soup: the soup object
        :return: the company objects
        """
        # get company ids from soup
        company_links = soup.select('a[href^="https://datacheck.co.il/company.ai?id="]')
        companies = [link['href'].split('=')[1] for link in company_links]

        # create company objects from ids
        company_objects = [company_data(company) for company in companies]
        return company_objects
    
"""
Test Code
"""
# owner_name = 'WALKER BUURMA NANCY MABLE'
# companies = companies_owned(owner_name).companies
# for test_company in companies:
#     print(test_company.company_name)
#     print(test_company.en_name)
#     print(test_company.incorporation_date)
#     print(test_company.status)
#     print(test_company.company_type)
#     print(test_company.is_governmental)
#     print(test_company.is_limited)
#     print(test_company.latest_annual_report)
#     print(test_company.company_purpose)
#     print(test_company.address)
#     print(test_company.company_discription)
#     print(test_company.company_id)
    