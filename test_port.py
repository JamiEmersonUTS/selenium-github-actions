import socket
import urllib.parse

def isOpen(url, port):
    # Parse the URL and extract the hostname
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    # Get the IP address of the hostname
    ip = socket.gethostbyname(hostname)
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Try to connect to the website on the specified port
        s.connect((ip, int(port)))
        s.shutdown(2)
        print(hostname)
        return True
    except:
        return False

# Test the website using the URL
url = 'https://project-cad-sandpit.sandpit.itu.uts.edu.au/cad/eoi'
port = 443
test_result = isOpen(url, port)
print(test_result)
