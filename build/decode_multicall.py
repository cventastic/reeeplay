import json
import requests
import time
from hexbytes import HexBytes
from web3 import Web3


# block with a multicall
block = 14944300
# tx multicall
tx = HexBytes('0xc3dc898b11e1734e2966c0a8587139244d93189391db4e0e32d0304b515cbcfe')


# init
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

tx = w3.eth.get_transaction(tx)
print(tx['input'])
