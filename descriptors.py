from datetime import datetime


class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)
        
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


def installments(cls):
    super_set = cls.__set__
    def __set__(self, instance, value):
        try:
            _, _ = [int(val) for val in value.split('/')]
            super_set(self, instance, value)
        except:
            msg = f"installments '{value}' does not match format 'paid_out/total'"
            raise ValueError(msg)
    cls.__set__ = __set__ 
    return cls 


def date(cls):
    super_set = cls.__set__
    def __set__(self, instance, value):
        datetime.strptime(value, '%d/%m/%Y')
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls

        
def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)
    super_set = cls.__set__
    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError('expected ' + str(expected_type))
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls 

def Unsigned(cls):
    super_set = cls.__set__
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls 

def MaxSized(cls):
    super_init = cls.__init__
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super_init(self, name, **opts)
    cls.__init__ = __init__

    super_set = cls.__set__
    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls 


@Typed(int)
class Integer(Descriptor):
    pass 


@Unsigned
class UnsignedInteger(Integer):
    pass 


@Typed(float)
class Float(Descriptor):
    pass 


@Unsigned
class UnsignedFloat(Float):
    pass 


@Typed(str)
class String(Descriptor):
    pass 


@MaxSized
class SizedString(String):
    pass


@date
class Date(Descriptor):
    pass

@installments
class Installments(Descriptor):
    pass 