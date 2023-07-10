from maltego_trx.transform import DiscoverableTransform
from maltego_trx.entities import Person, Company, Phrase
from extensions import registry, IBItransforms
from ShareholderIntel import shareholder_data
from CompanyIntel import get_companyID, company_data


@registry.register_transform(display_name="toShareholders [IBI]",
                             input_entity=Company,
                             description="Get shareholders of company",
                             output_entities=[Person],
                             transform_set=IBItransforms)
class toShareholders(DiscoverableTransform):
    
    @classmethod
    def create_entities(cls, request, response):
        company_id = 0
        
        try: # try to get company_id from company property
            company_id = request.getProperty('company_id')
        except: # if not found, send error  message instructing to run toCompanyDetails
            response.addUIMessage("Please run toCompanyDetails first.", "FatalError")
            return
        
        # get shareholders
        shareholders = shareholder_data(company_id)
        companies = shareholders.companies
        people = shareholders.people    

        # create company entities
        response.addEntity(Phrase, companies[0])
        for company in companies:
            try: # try to get company data from company name
                company = company_data(get_companyID(company))
                ent = response.addEntity(Company, company.company_name)
                for key, value in company.__dict__.items():
                    if key != 'company_name':
                        display_name = key.replace('_', ' ').title()
                        ent.addProperty(key, display_name, '', value)
            except: # if not found, create entity with company name only and company_id propertyy
                ent = response.addEntity(Company, company)
                ent.addProperty('company_id', 'Company ID', '', '')

            # format entity
            ent.setLinkThickness(1)
            ent.setLinkLabel('Shareholder')
            ent.reverseLink()

        # create person entities
        for person in people:
            ent = response.addEntity(Person, person)
            ent.setLinkThickness(1)
            ent.setLinkLabel('Shareholder')
            ent.reverseLink()
