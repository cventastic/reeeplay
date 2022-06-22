import os
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://geth-rinkeby:8545'))

private_key = os.environ['PRIVATE_KEY']
from_address = os.environ['SENDER_ADDRESS']
to_address = '0x4beb7299221807Cd47C2fa118c597C51Cc2fEC99'

nonce = w3.eth.getTransactionCount(from_address)
gasPrice = w3.toWei('50', 'gwei')
value = w3.toWei(0, 'ether')


def sent_rinkeby(input):
    tx = {
        'chainid': 4,
        'nonce': nonce,
        'to': to_address,
        'value': value,
        'gas': 2000000,
        'data': input,
        'gasPrice': gasPrice
    }
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Transaction  Hash: ")
    print(tx_hash)
