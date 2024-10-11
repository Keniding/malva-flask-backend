from flask import request, abort
import ipaddress

ALLOWED_IPS = ['192.168.8.0/24', '127.0.0.1']

def ip_in_subnet(ip, subnet):
    return ipaddress.ip_address(ip) in ipaddress.ip_network(subnet)

def ip_restrictor(app):
    @app.before_request
    def restrict_ip_address():
        client_ip = request.remote_addr
        if not any(ip_in_subnet(client_ip, subnet) for subnet in ALLOWED_IPS):
            abort(403)
