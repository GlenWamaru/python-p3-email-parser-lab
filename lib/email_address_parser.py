# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        addresses = re.findall(pattern, self.email_addresses)
        
        # Remove duplicates and sort alphabetically
        unique_addresses = sorted(set(addresses))
        
        return unique_addresses
