# IsraelBusinessIntel
Information regarding Israeli businesses and their owners

This repository contains a library and Maltego transforms to retrieve information about businesses from the website https://datacheck.co.il.


# Library Description
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
            Company Description
    Method get_companyID:
        Input: Company name
        Output: Company ID
    OwnerIntel.py:
        Class companies_owned:
            Input: Name of person
            Output: companies_owned object with a list of company_data objects owned by the input
    ShareholderIntel.py:
        Class shareholder_data:
            Input: Company ID
            Output: Two lists:
                Class object with a list of company_data objects that are shareholders of the input
                List of names of people that are shareholders of the input

# Maltego Transforms Description
The Maltego transforms are as follows:

    toCompanyDetails:
        Input Entity: maltego.company
        Output Entity: maltego.company
            With added properties containing the company data from CompanyIntel.py
    entitiesToProperties:
        Input Entity: maltego.company
            Meant to be run after running toCompanyDetails
        Output Entities:
            maltego.datetime x2:
                Incorporation Date
                Latest Annual Report
            maltego.address:
                Company address
    OwnedCompanies:
        Input Entity: maltego.person
        Output Entity: maltego.company
    toShareholders:
        Input Entity: maltego.company
        Output Entities:
            maltego.company
            maltego.person

# Download and Installation
From the command line, run:

    git clone https://github.com/HawkEyes-OSINT/IsraelBusinessIntel.git

Install transforms:
After cloning the repository, from the command line, run:

    cd <path to repository>/IsraelBusinessIntel
    pip install -r requirements.txt
    python project.py run

From the Maltego client, click on the 'Import/Export' tab on the top right of the client.
Click on 'Import Config' and select '<path to repository>/IsraelBusinessIntel/IBItransforms.mtz'
