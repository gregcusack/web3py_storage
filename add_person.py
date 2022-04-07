from base import *
from dotenv import load_dotenv
import sys

if len(sys.argv) < 3:
    print("please enter name and age to add to people map")
    sys.exit(-1)

inName = sys.argv[1]
inAge = int(sys.argv[2])

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("GANACHE_RPC_URL")))
chain_id = 1337

my_address = os.getenv("ACCOUNT_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")

#  Compiled bytecode of smart contract （ Data on the chain ）
bytecode = compiled_sol["contracts"]["Storage.sol"]["Storage"]["evm"]["bytecode"]["object"]

# ABI (Application Binary Interface), An interface for interacting with methods in a smart contract 
abi = json.loads(
    compiled_sol["contracts"]["Storage.sol"]["Storage"]["metadata"]
    )["output"]["abi"]

#  call deploy.py Will get contract_address
contract_address = os.getenv("CONTRACT_ADDRESS")

nonce = w3.eth.get_transaction_count(my_address)

#  Instantiate the contract object 
storage = w3.eth.contract(address=contract_address, abi=abi)

#  call addPerson Method 
transaction = storage.functions.addToPeopleMap(inName, inAge).buildTransaction({
    "gasPrice": w3.eth.gas_price,
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce
})
#  Signature 
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
#  Sending transaction 
tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
print('add new Person to contract...')
#  Waiting for the deal to complete 
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("person added")