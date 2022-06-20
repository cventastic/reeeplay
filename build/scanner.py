import replay
import time
from hexbytes import HexBytes
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://geth-mainnet:8545'))
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
                payload = tx['input']
                replay.sent_rinkeby(payload)
    except ValueError:
        print("Ooops, uncle or orphan?")


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
