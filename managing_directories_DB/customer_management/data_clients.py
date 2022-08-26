class ClientFL:
    id: int
    FIO: str
    residentialAddress: str
    numberPassport: str
    numberPhone: str

    def __init__(self, FIO, residentialAddress, numberPassport, numberPhone, id=None):
        self.id = id
        self.FIO = FIO
        self.residentialAddress = residentialAddress
        self.numberPassport = numberPassport
        self.numberPhone = numberPhone

class ClientL:
    id: int
    Name: str
    legalAddress: str
    OGRN: str
    numberPhone: str

    def __init__(self, Name, legalAddress, OGRN, numberPhone, id=None):
        self.id = id
        self.Name = Name
        self.legalAddress = legalAddress
        self.OGRN = OGRN
        self.numberPhone = numberPhone