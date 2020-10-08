import wallet
from tkinter import *

btc_wallet = wallet.Wallet()
filename = 'credentials.txt'

with open (filename, 'w') as f:
    f.write ('currency: ' + btc_wallet.coin + '\n')
    f.write ('private key: ' + btc_wallet.private_key + '\n')
    f.write ('public key: ' + btc_wallet.public_key + '\n')
    f.write ('address: ' + btc_wallet.address + '\n')
    f.write ('seed: ' + btc_wallet.seed + '\n')
f.close ()

root = Tk()

label_currency = Label(root, text='Currency: '+btc_wallet.coin)
label_currency.grid(row=0, sticky='w')

label_address = Label(root, text='Address: '+btc_wallet.address)
label_address.grid(row=1, sticky='w')

label_private_key = Label(root, text='Private Key: '+btc_wallet.private_key)
label_private_key.grid(row=2, sticky='w')

label_public_key = Label(root, text='Public Key: '+btc_wallet.public_key)
label_public_key.grid(row=3, sticky='w')

label_seed = Label(root, text='seed: '+btc_wallet.seed)
label_seed.grid(row=4, sticky='w')


running = True
while running: 
    root.mainloop()
    if root.quit:
        running = False
