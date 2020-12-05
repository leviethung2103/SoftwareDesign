from address import Address


class Person:
    def __init__(self, first, last, dob, phone, address) -> None:
        self.first_name = first
        self.last_name = last
        self.date_of_birth = dob
        self.phone = phone
        # address: one or many ? 
        self.addresses = []

        # check the instance belongs to Address
        if isinstance(address,Address):
            self.addresses.append(address)
        elif isinstance(address,list):
            for entry in address:
                if not isinstance(entry,Address):
                    raise Error("Invalid Address../")
            self.addresses = address
        else:
            raise Error("Invalid address...")

    def add_address(self,address):
        if not isinstance(address,Address):
            raise Error("Invalid address..")

        self.addresses.append(address)



Person(_,....,[Address(),Address()])
Person(_,..., Address(""))