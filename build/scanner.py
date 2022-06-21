import replay
import time
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://geth-mainnet:8545'))
graph_proxy_address = '0xadca0dd4729c8ba3acf3e99f3a9f471ef37b6825'


def handle_event(event):
    try:
        block = w3.eth.get_block(event.hex(), full_transactions=True)
        print(block['number'])
        for tx in block['transactions']:
            # print(tx['input'])
            if tx['to'].lower() == graph_proxy_address.lower():
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
