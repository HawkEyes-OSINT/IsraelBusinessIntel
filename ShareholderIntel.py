import requests
from bs4 import BeautifulSoup

class shareholder_data:
    def __init__(self, company_id):
        """
        This function is used to extract the data from the website
        :param company_id: the company id
        This class is used to extract the following data:
        - companies
        - people
        :return: the data of the company and the people who hold the shares of the company.
        """
        soup = self._extract_soup(company_id)

        self.companies, self.people = self._extract_data(soup)

    def _extract_soup(self, company_id):
        """
        This function is used to extract the data from the website
        :param company_id: the company id
        :return: the soup object
        """
        url = f"https://datacheck.co.il/companyshareholders.ai?id={company_id}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    
    def _extract_data(self, soup):
        """
        This function is used to extract the data from the website
        :param soup: the soup object
        :return: the data of the company and the people who hold the shares of the company.
        """
        companies = []
        people = []
        
        # extract data from html
        table = soup.find(class_='table table-striped mb-0')
        links = table.select('a[href^="https://datacheck.co.il"]')

        # insert data to lists
        for link in links:
            if link['href'].split('/')[3].split('.')[0] == 'company':
                companies.append(link.text)
            else:
                people.append(link.text)

        return companies, people

"""
Test Code
"""
shareholders = shareholder_data(company_id=516648565)
print(shareholders.companies)
print(shareholders.people)
