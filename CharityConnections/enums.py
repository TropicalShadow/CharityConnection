from enum import Enum,auto

class ShadowEnum(Enum):
    def toTuple(self):
        return (self.value,self.name)


class CharityCatagory(ShadowEnum):
    PERSON = auto()
    HEALTH = auto()
    ANIMALS = auto()
    ENVIRONMENT = auto()
    EDUCATION = auto()



class CharityAction(ShadowEnum):
    COOK = auto()
    CLEAN = auto()
    TEACH = auto()
    PARTY = auto()