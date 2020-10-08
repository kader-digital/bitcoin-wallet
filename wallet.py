class Wallet ():
    def __init__(self):
        from pywallet import wallet as w

        self.coin = ''
        self.private_key = ''
        self.public_key = ''
        self.address = ''

        self.seed = w.generate_mnemonic()
        self.wallet = w.create_wallet(network='BTC',seed=self.seed, children=0)
        self.parse_response()

    def parse_response(self):
        for line in list(self.wallet):
            if 'coin' in line:
                self.coin = self.wallet[line]
            elif 'private_key' in line:
                self.private_key = self.wallet[line]
            elif 'public_key' in line:
                self.public_key = self.wallet[line]
            elif 'address' in line:
                self.address = self.wallet[line]
