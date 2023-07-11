from maltego_trx.transform import DiscoverableTransform
from maltego_trx.entities import Person, Company, Phrase
from extensions import registry, IBItransforms
from OwnerIntel import companies_owned

@registry.register_transform(display_name="OwnedCompanies [IBI]",
                             input_entity=Person,
                             description="Get the owned companies of a person",
                             output_entities=[Company],
                             transform_set=IBItransforms)
class OwnedCompanies(DiscoverableTransform):
    
    @classmethod
    def create_entities(cls, request, response):
        owner_name = request.Value

        companies_list = companies_owned(owner_name).companies   
        for company in companies_list:
            ent = response.addEntity(Company, company.company_name)
            for key, value in company.__dict__.items():
                if key != 'company_name':
                    display_name = key.replace('_', ' ').title()
                    ent.addProperty(key, display_name, '', value)

            # format entity
            ent.setLinkThickness(1)
            ent.setLinkLabel('Shareholder')
            ent.reverseLink()
