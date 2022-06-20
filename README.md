## reeeplay


replay transactions from mainnet to rinkeby

Fill out .env_skel file and rename it to .env.

Then do:
```
docker-compose up -d
```



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
