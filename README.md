## reeeplay


replay transactions from mainnet to rinkeby

Fill out .env_skel file and rename it to .env.

Then do:
```
docker-compose up -d
```

0x143298ca69a5ca3b5e5c4c69952952910d353d22608eaf6b53de16d64e05d39b

# MISC:

in case i dont want to decode i can just use the "MethodID" for the calls:
publishNewSubgraph: 0xe1329732
upgradeSubgraph:
publishAndSignal:

example get abi + decode, not working for multicalls.
```
transaction = HexBytes('0x1e1154d2276161be6f9324452a685dfb9680c101381321516c368dd00bd14fd7')
proxy_contract = '0xaDcA0dd4729c8BA3aCf3E99F3A9f471EF37b6825'
abi = requests.get('http://api.etherscan.io/api?module=contract&action=getabi&address=' + get_contract_from_proxy(proxy_contract) + '&format=raw')
json_abi = json.loads(abi.text)
contract_abi = w3.eth.contract(w3.toChecksumAddress(get_contract_from_proxy(proxy_contract)), abi=json_abi)
tx = w3.eth.get_transaction(transaction)
print(contract_abi.decode_function_input(tx.input))
```


get contract from proxy
```
# https://eips.ethereum.org/EIPS/eip-1967#logic-contract-address
def get_contract_from_proxy(address):
    contract = w3.eth.get_storage_at(address, position='0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc')
    return helper_remove_zeros(contract.hex())
```

remove zeroes from address:
```
def helper_remove_zeros(address):
    decimal = int(address, 16)
    hexa = HexBytes(decimal)
    return hexa.hex()
```