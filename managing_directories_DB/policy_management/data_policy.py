class Policy:
    policyNumber: int
    idTypeObject: int
    idFL: int
    idL: int
    idObjects: int
    startDate: str
    stopDate: str
    insuranceAmount: int


    def __init__(self, idTypeObject, idObjects, startDate, stopDate, insuranceAmount, idFL=None, idL=None, policyNumber=None):
        self.policyNumber = policyNumber
        self.idTypeObject = idTypeObject
        self.idFL = idFL
        self.idL = idL
        self.idObjects = idObjects
        self.startDate = startDate
        self.stopDate = stopDate
        self.insuranceAmount = insuranceAmount

class SellPolicy:
    policyNumber: int
    status: str

    def __init__(self, policyNumber, status):
        self.policyNumber = policyNumber
        self.status = status