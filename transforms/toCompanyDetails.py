from maltego_trx.transform import DiscoverableTransform
from maltego_trx.entities import Company
from extensions import registry, IBItransforms
from CompanyIntel import get_companyID, company_data
import re

@registry.register_transform(display_name="CompanyDetails [IBI]",
                             input_entity=Company,
                             description="Get company details from IBI",
                             output_entities=[Company],
                             transform_set=IBItransforms)
class toCompanyDetails(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request, response):
        company_name = request.Value
        hebrew_chars = re.compile(r'[^א-ת\s]')
        company_name = hebrew_chars.sub('', company_name)

        try: # try to get company details
            company_id = request.getProperty('company_id')
            if company_id:
                company = company_data(company_id)
            else:
                company = company_data(get_companyID(company_name))

        except: # request company id via new company entity with id property
            ent = response.addEntity(Company, company_name)
            ent.addProperty('company_id', 'Company ID', '', '')
            response.addUIMessage("Error: Could not find company, try adding the company ID to the entity properties", "FatalError")
            return
        
        ent = response.addEntity(Company, company.company_name)
        for key, value in company.__dict__.items():
            if key != 'company_name':
                display_name = key.replace('_', ' ').title()
                ent.addProperty(key, display_name, '', value)
        