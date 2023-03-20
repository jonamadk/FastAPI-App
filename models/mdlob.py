from lib2to3.pytree import Base
from pydantic import BaseModel


class LineOfBusiness(BaseModel):
    _id:str
    code:str
    carrierCode:str
    broadLineBusinessCode:str
    carrierName:str
    carrierWebsite:str
    enabled:str
    _class:str
    carrierLogo:str
    jurisdictions:str
    integrationType:str
    stateOrProvinceCode:str
    stateOrProvinceName:str
    integrationType:str
    stateOrProvinceCode:str
    stateOrProvinceName:str

    