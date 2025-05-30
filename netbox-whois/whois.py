import os
import pynetbox
from jinja2 import Template, Environment, FileSystemLoader

j2env = Environment(loader=FileSystemLoader("templates"))
TEMPLATE = j2env.get_template('whois.j2')

nb = pynetbox.api(os.environ.get("NETBOX_URL"), os.environ.get("NETBOX_TOKEN"))

print()

def get_content():
    asns = nb.ipam.asns.all()
    content = TEMPLATE.render({"ases": asns})
    print(content)

    return(content)
