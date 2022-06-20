import json
import requests
import time
from hexbytes import HexBytes
from web3 import Web3

# in case i dont want to decode i can just use the "MethodID" for the calls:
# publishNewSubgraph: 0xe1329732
# upgradeSubgraph:
# publishAndSignal:

#w3 = Web3(Web3.HTTPProvider('http://geth-mainnet:8545'))
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
graph_proxy_address = '0xadca0dd4729c8ba3acf3e99f3a9f471ef37b6825'


def helper_remove_zeros(address):
    decimal = int(address, 16)
    hexa = HexBytes(decimal)
    return hexa.hex()


# https://eips.ethereum.org/EIPS/eip-1967#logic-contract-address
def get_contract_from_proxy(address):
    contract = w3.eth.get_storage_at(address, position='0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc')
    return helper_remove_zeros(contract.hex())


def handle_event(event):
    try:
        block = w3.eth.get_block(event.hex(), full_transactions=True)
        print(block['number'])
        for tx in block['transactions']:
            # print(tx['input'])
            if tx['to'] == graph_proxy_address:
                print("Transaction: /n")
                print(tx)
                print("Transaction Input: /n")
                print(tx['input'])
    except ValueError:
        print("Ooops, uncle or orphan?")
    # Print all transactions inside the new block
    # print(block['transactions'])


def log_loop(event_filter, poll_interval):
    while True:
        try:
            for event in event_filter.get_new_entries():
                handle_event(event)
            time.sleep(poll_interval)
        except ValueError:
            print("Couldn't get block with filter function")


def main():
    block_filter = w3.eth.filter('latest')
    log_loop(block_filter, 2)


if __name__ == '__main__':
    main()


# transaction = HexBytes('0x1e1154d2276161be6f9324452a685dfb9680c101381321516c368dd00bd14fd7')
# proxy_contract = '0xaDcA0dd4729c8BA3aCf3E99F3A9f471EF37b6825'
#
# abi = requests.get('http://api.etherscan.io/api?module=contract&action=getabi&address=' + get_contract_from_proxy(proxy_contract) + '&format=raw')
# json_abi = json.loads(abi.text)
# contract_abi = w3.eth.contract(w3.toChecksumAddress(get_contract_from_proxy(proxy_contract)), abi=json_abi)
#
# tx = w3.eth.get_transaction(transaction)
# print(contract_abi.decode_function_input(tx.input))
