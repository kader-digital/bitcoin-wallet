import wallet

btc_wallet = wallet.Wallet()
filename = 'credentials.txt'

with open (filename, 'w') as f:
    f.write ('currency: ' + btc_wallet.coin + '\n')
    f.write ('private key: ' + btc_wallet.private_key + '\n')
    f.write ('public key: ' + btc_wallet.public_key + '\n')
    f.write ('address: ' + btc_wallet.address + '\n')
    f.write ('seed: ' + btc_wallet.seed + '\n')
f.close ()

