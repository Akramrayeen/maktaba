from ajax_select import LookupChannel
from geonamescache import GeonamesCache

gc = GeonamesCache()

class CountryLookup(LookupChannel):
    model = gc.get_countries()
    def get_query(self, q, request):
        return self.model.filter(name__icontains=q).values_list('name', flat=True)[:10]

class StateLookup(LookupChannel):
    def get_query(self, q, request):
        return gc.get_us_states(q)[:10]

class CityLookup(LookupChannel):
    def get_query(self, q, request):
        return gc.get_cities_by_name(q)[:10]
