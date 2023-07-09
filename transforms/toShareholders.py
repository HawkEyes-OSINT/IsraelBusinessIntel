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
