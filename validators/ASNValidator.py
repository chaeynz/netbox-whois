import re

def validate_asn(asn):
    this_type = "asn"
    if re.search(r"^AS(\d+)$", asn, re.IGNORECASE) and int(asn[2:]) < 2**32-1:
        return {"value": int(asn[2:]), "type": this_type}
    else:
        return None
