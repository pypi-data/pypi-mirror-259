
import shelve


class CachingAlgod:
    def __init__(self, algod, name, round=None) -> None:
        self.algod = algod
        self.cache = shelve.open(f'cache_{name}')

    def close(self):
        self.cache.close()

    def asset_info(self, asset_id):
        key = str(asset_id)
        if key not in self.cache:
            print(f"Fetching asset info {asset_id}")
            self.cache[key] = self.algod.asset_info(asset_id)
        return self.cache[key]
    
    def account_info(self, address):
        key = str(address)
        if key not in self.cache:
            print(f"Fetching account info {address}")
            self.cache[key] = self.algod.account_info(address)
        return self.cache[key]
    
    def application_info(self, app_id):
        key = str(app_id)
        if key not in self.cache:
            print(f"Fetching app info {app_id}")
            self.cache[key] = self.algod.application_info(app_id)
        return self.cache[key]
