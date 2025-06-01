import os
import pynetbox
from jinja2 import Environment, FileSystemLoader

j2env = Environment(loader=FileSystemLoader("templates"))
TEMPLATE = j2env.get_template('whois.j2')

nb = pynetbox.api(os.environ.get("NETBOX_URL"), os.environ.get("NETBOX_TOKEN"))

def get_all_asns():
    asns = nb.ipam.asns.all()
    content = TEMPLATE.render({"ases": asns})

    return(content)


def get_asn(asn: int):
    nb_asn = nb.ipam.asns.get(asn=str(asn))

    if nb_asn is None:
        return None

    content = TEMPLATE.render({"ases": [nb_asn]})

    return(content)
