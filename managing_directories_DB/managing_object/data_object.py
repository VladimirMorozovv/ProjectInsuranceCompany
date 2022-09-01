class Object:
    idObjects: int
    Name: str
    numberPassport: str
    idTypeObject: int

    def __init__(self,  Name, numberPassport, idTypeObject, idObjects=None):
        self.idObjects = idObjects
        self.Name = Name
        self.numberPassport = numberPassport
        self.idTypeObject = idTypeObject