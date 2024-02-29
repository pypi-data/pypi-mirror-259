import requests

class Jettonapi:
    def __init__(self, testnet=False):
        self.base_url = 'https://tonapi.io/v2'
        if testnet == True:
            self.base_url = 'https://testnet.tonapi.io/v2'
        self.headers = {"Accept": "application/json"}

    def get_status(self):
        response = requests.get(f"{self.base_url}/status", headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            return data['rest_online']
        else:
            result = f"Error: {response.status_code}"
            return result

    def get_price(self, tokens, currencies):
        response = requests.get(f'{self.base_url}/rates?tokens={tokens}&currencies={currencies}', headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            return data['rates'][f'{tokens}']['prices'][f'{currencies}']
        else:
            result = f'Error: {response.status_code}'
            return result

    def get_diff(self, tokens, diff, currencies):
        response = requests.get(f'{self.base_url}/rates?tokens={tokens}&currencies={currencies}', headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            return data['rates'][f'{tokens}'][f'diff_{diff}'][f'{currencies}']
        else:
            result = f'Error: {response.status_code}'
            return result
        
    