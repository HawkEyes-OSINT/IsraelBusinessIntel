from maltego_trx.transform import DiscoverableTransform
from maltego_trx.entities import Location, Company
from extensions import registry, IBItransforms

@registry.register_transform(display_name="entityTOproperties [IBI]",
                             input_entity=Company,
                             description="Turn date and location properties to entities",
                             output_entities=[Location, "maltego.DateTime"],
                             transform_set=IBItransforms)
class entitiesTOproperties(DiscoverableTransform):
    
    @classmethod
    def create_entities(cls, request, response):
        company = request.Value

        # incorporation_date
        incorporation_date = request.getProperty('incorporation_date')
        if incorporation_date:
            ent = response.addEntity('maltego.DateTime', incorporation_date)
            ent.setLinkLabel('Incorporation Date')
            ent.setLinkThickness(1)

        # latest_annual_report
        latest_annual_report = request.getProperty('latest_annual_report')  
        if latest_annual_report:
            ent = response.addEntity('maltego.DateTime', latest_annual_report)
            ent.setLinkLabel('Latest Annual Report')
            ent.setLinkThickness(1)

        # address
        address = request.getProperty('address')
        if address:
            ent = response.addEntity(Location, address)
            ent.setLinkLabel('Address')
            ent.setLinkThickness(1)
            