from typing import Dict, List

class Onion:
    o1:int
    
    def __init__(self, h ):
        self.o1=h
        
    def __repr__( self ):
        return f"Onion(o1={ga( self, 'o1' )})" 

class Toast:
    t1: Dict[object, object]
    t2: List[Onion]
    
    
    def __init__( self, g ):
        self.t1 = { "value": g }
        self.t2 = [Onion(n) for n in range(3)]
    
    
    def __repr__( self ):
        return f"Toast(t1={ga(self, 't1')}, t2={ga(self, 't2')})"


class Beans:
    b1: object
    b2: object
    b3: Toast
    
    
    def __init__( self, e, f, g ):
        self.b1 = e
        self.b2 = f
        self.b3 = Toast( g )
    
    
    def __repr__( self ):
        return f"Beans(b1={ga( self, 'b1' )}, b2={ga( self, 'b2' )}, b3={ga( self, 'b3' )})"


class Spam:
    s1: object
    s2: Beans
    
    
    def __init__( self, d, e, f, g ):
        self.s1 = d
        self.s2 = Beans( e, f, g )
    
    
    def __repr__( self ):
        return f"Spam(s1={ga( self, 's1' )}, s2={ga( self, 's2' )})"


class Eggs( Spam ):
    e1: object
    e2: object
    e3: object
    
    
    def __init__( self, a, b, c, d, e, f, g ):
        super().__init__( d, e, f, g )
        self.e1 = a
        self.e2 = b
        self.e3 = c
    
    
    def __repr__( self ):
        return f"Eggs(e1={ga( self, 'e1' )}, e2={ga( self, 'e2' )}, e3={ga( self, 'e3' )}, base={super().__repr__()})"


sentinel = object()


def ga( x, y ):
    v = getattr( x, y, sentinel )
    if v is sentinel:
        return "?"
    return v.__repr__()


from mhelper import json_helper


original = Eggs( True, 2, 3.0, "four", 5, 6, 7 )
json_dict = json_helper.to_json( original )
round_trip = json_helper.from_json( json_dict, Eggs )
print( f"ORIGINAL   = {original}" )
print( f"JSON       = {json_dict}" )
print( f"ROUND-TRIP = {round_trip}" )
assert repr( original ) == repr( round_trip )


Toast.__annotations__["t2"]= list

try:
    round_trip = json_helper.from_json( json_dict, Eggs )
    raise RuntimeError("Expected a JsonDeserialiseError.")
except json_helper.JsonDeserialiseError as ex:
    print(str(ex))