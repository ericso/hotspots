from locu.api import VenueApiClient, MenuItemApiClient

class Root(object):
	def __init__(self, request):
		self.venue_client = VenueApiClient('359026ce8bb4a10f302211ddea87b2b5131fa041')

	def __getitem__(self, key):
		if key == 'map':
			venues = self.venue_client.search(locality = 'San Francisco')
			print(venues)

			return 'this is a map'
