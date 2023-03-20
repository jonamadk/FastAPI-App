

def line_of_business_entity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "code": item["code"],
        "carrierCode": item["carrierCode"],
        "broadLineBusinessCode": item["broadLineBusinessCode"],
        "carrierName": item["carrierName"],
        "carrierWebsite": item["carrierWebsite"],
        "enabled": item["enabled"],
        "_class": item["_class"],
        "carrierLogo": item["carrierLogo"],
        "jurisdictions": item["jurisdictions"],
        "integrationType": item["integrationType"],
        "stateOrProvinceCode": item["stateOrProvinceCode"],
        "stateOrProvinceName": item["stateOrProvinceName"],
    }
    

def line_of_business_entities(entities) -> list:
    return[line_of_business_entity(item) for item in entities]
