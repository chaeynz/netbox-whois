from ipaddress import ip_address, ip_network

def validate_ip_address(ip_address):
    this_type = "ip_address"
    try:
        return  {"value": ip_address(ip_address), "type": this_type}
    except ValueError:
        return None
