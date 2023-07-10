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
            day, month, year = incorporation_date.split('/')
            ent = response.addEntity('maltego.DateTime', incorporation_date)
            ent.addProperty('day', 'Day', '', day)
            ent.addProperty('month', 'Month', '', month)
            ent.addProperty('year', 'Year', '', year)
            ent.setLinkLabel('Incorporation Date')
            ent.setLinkThickness(1)

        # latest_annual_report
        latest_annual_report = request.getProperty('latest_annual_report')  
        if latest_annual_report:
            ent = response.addEntity('maltego.DateTime', latest_annual_report)
            ent.addProperty('year', 'Year', '', latest_annual_report)
            ent.setLinkLabel('Latest Annual Report')
            ent.setLinkThickness(1)

        # address
        address = request.getProperty('address')
        if address:
            # create address properties
            street, city, area = '', '', ''
            addr_indx = 0
            addr = address.split(' ')
            for word in addr:
                if any(char.isdigit() for char in word):
                    addr_indx = addr.index(word)+1
                    street = ' '.join(addr[:addr_indx])
                    addr_indx += 1
                    break
            for word in addr[addr_indx:]:
                if word ==  '':
                    addr_indx += addr.index(word) + 2
                    break
                else:
                    city += word + ' '
            for word in addr[addr_indx:]:
                area += word + ' '

            # add entity
            ent = response.addEntity(Location, address)
            ent.setLinkLabel('Address')
            ent.setLinkThickness(1)

            # add properties
            ent.addProperty('country', 'Country', '', 'ישראל')
            ent.addProperty('city', 'City', '', city)
            ent.addProperty('streetaddress', 'Street Address', '', street)
            ent.addProperty('location.area', 'Area', '',  area)
            ent.addProperty('countrycode', 'Country Code', '', 'IL')
            