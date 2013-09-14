class Root(object):
	def __init__(self, request):
		pass

	def __getitem__(self, key):
		if key == 'map':
			return 'this is a map'
