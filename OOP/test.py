class AttributeInitType(object):

   def __init__(self,**kwargs):
       for name, value in kwargs.items():
          setattr(self, name, value)

class Car(AttributeInitType):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    @property
    def description(self):
       return "%s %s %s %s" % (self.color, self.year, self.make, self.model)

c = Car(make='Toyota', model='Prius', year=2005, color='green')
print (c.description)