from .grid import Grid
from .hash import generate_private_key, generate_public_key, gen_access_key, check_access_key

class Network:
    def __init__(self, name, grid: Grid):
        """
        Initializes the object with the given name and grid.

        Parameters:
            name: str - the name of the object
            grid: Grid - the grid object to be associated with the object

        Returns:
            None
        """
        self.grid = grid
        self.name = name
        self._check()

    def _check(self):
        if self.grid.get()[0, 0, 0] is None:
            self.grid.genesis()
        if self.grid.get()[0, 0, 1] is None:
            self.grid.cache()
    def get_accounts(self):
        return self.grid.get()[0, 0, 1]["accounts"]
    def import_account(self, account: 'Account'):
        """
        Import account into the network.
        """
        public_key, private_key, access_key = account.export()
        self.grid.import_pair(access_key, private_key, public_key)

class Account:
    def __init__(self, access_key=None, public=None, private=None):
        """
        Initializes the object with the provided access key, public key, and private key.
        
        Parameters:
            access_key (None): The access key for the object.
            public (None): The public key for the object.
            private (None): The private key for the object.
            
        Returns:
            None
        """ 
        if access_key is None and public is None and private is None:
            self.private_key = generate_private_key()
            self.access_key = gen_access_key(self.private_key)
            self.public_key = generate_public_key(self.private_key, self.access_key)
            if not check_access_key(self.access_key, self.public_key, self.private_key):
                raise ValueError("Access key is wrong.")
        else:
            self.import_pair(access_key, public, private)

            

    def export(self):
        return self.public_key, self.private_key, self.access_key
    
    def import_pair(self, access_key, public, private):
        if check_access_key(public_key=public, private_key=private, encoded_key=access_key):
            self.public_key = public
            self.private_key = private
            print("Successfully imported")
        else: 
            print("Could not import")
    
    def get(self):
        return {"access_key": self.access_key, "public_key": self.public_key, "private_key": self.private_key}
