

class MyTestCls(object):
	def __init__(self, **kwargs):
		for k, v in kwargs.items():
			setattr(self, k, v)

	def __repr__(self):
		return 'A<{0:}>'.format(', '.join('{0:s}={1:}'.format(k, v) for k, v in self.__dict__.items()))


class CustomEncodeCls(MyTestCls):
	def __init__(self, **kwargs):
		super(CustomEncodeCls, self).__init__(**kwargs)
		self.relevant = 42
		self.irrelevant = 37

	def __json_encode__(self):
		return {'relevant': self.relevant}

	def __json_decode__(self, **attrs):
		self.relevant = attrs['relevant']
		self.irrelevant = 12


