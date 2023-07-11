# IsraelBusinessIntel
Information regarding Israeli businesses and their owners

This repository contains a library and Maltego transforms to retreive information about buisnesses from the website https://datacheck.co.il.


Library Description
CompanyIntel.py:
    Class company_data:
        Input: Company name
        Output: Class object with the following details:
            Company ID
            Company Name
            English Name
            Incorporation Date
            Status
            Company Type
            Boolean is_governmental
            Boolean is_limited
            Latest Annual Report
            Company Purpose
            Address
            Company Discription
    Method get_companyID:
        Input: Company name
        Output: Company ID
OwnerIntel.py:
    Class companies_owned:
        Input: Name of person
        Output: companies_owned object with list of company_data objects owned by input
ShareholderIntel.py:
    Class shareholder_data:
        Input: Company ID
        Output: Two lists:
            Class object with a list of company_data objects that are shareholders of the input
            List of names of people that are shareholders of the input

Maltego Transforms Description
The Malto transforms are as follows:
    toCompanyDetails:
        Input Entity: maltego.company
        Output Entity: maltego.company:
            With added properties containing the company data from CompanyIntel.py
    entitiesToproperties:
        Input Entity: maltego.comapny:
            Meant to be run after running toCompanyDetails
        Output Entities:
            maltego.datetime x2:
                Incorporation Date
                Latest Annual Report
            maltego.address:
                Comapny address
    OwnedCompanies:
        Input Entity: maltego.person
        Output Entity: maltego.company
    toShareholders:
        Input Entity: maltego.company
        Output Entities:
            maltego.company
            maltego.person

Download
From command line, run:
    git clone https://github.com/HawkEyes-OSINT/IsraelBusinessIntel.git

Install transforms:
    After cloning the repository, from command line, run:
        cd <path to repository>/IsraelBusinessIntel
        pip install -r requirements.txt
        python project.py run
    From Maltego client, click on the 'Import/Export' tab on the top right of the client.
    Click on 'Import Config' and select '<path to repository>/IsraelBusinessIntel/IBItransforms.mtz'
