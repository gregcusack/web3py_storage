from base import *
from dotenv import load_dotenv

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

#  Build smart contract objects 
storage = w3.eth.contract(abi=abi, bytecode=bytecode)
#  Of the last transaction in the current blockchain nonce
nonce = w3.eth.get_transaction_count(my_address)

#  Deploy smart contracts  -  Create transaction 
transaction = storage.constructor().buildTransaction({
    "gasPrice": w3.eth.gas_price,
    "chainId": chain_id, 
    "from": my_address, 
    "nonce": nonce
    }
)
#  Sign the current transaction  -  Prove that you initiated the transaction 
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")

#  Start deployment  -  Sending transaction 
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print('Waiting for deploy transaction to finish...')
#  Wait for smart contract deployment results , After deployment , Will get the address of the contract 
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print('Deployed Done!')
print(f'contract address: {tx_receipt.contractAddress}')