# The script to check the date of expiration of the certificate.
# The script expects the domain name as an argument.
# Example: SSL-Expiration-Date.py 
# If the domain is not valid, the server name or inaccessibility will return "-100"

import socket
import ssl
import datetime
from sys import argv

hostname = argv[1]

context = ssl.create_default_context()
ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
today= datetime.datetime.now()

try:
    conn = context.wrap_socket(socket.socket(), server_hostname=hostname)
    conn.connect((hostname, 443))
    cert = conn.getpeercert()
    valid = cert['notAfter']
    expires = datetime.datetime.strptime(valid, ssl_date_fmt)
    difference = (expires - today).days
    print(difference)
except Exception:
    print(-100)
