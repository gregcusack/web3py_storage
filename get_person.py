from base import *
from dotenv import load_dotenv
import sys

if len(sys.argv) < 2:
    print("please enter a name to get from people map")
    sys.exit(-1)

inName = sys.argv[1]

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("GANACHE_RPC_URL")))
chain_id = 1337

my_address = os.getenv("ACCOUNT_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")

# ABI (Application Binary Interface), An interface for interacting with methods in a smart contract 
abi = json.loads(
    compiled_sol["contracts"]["Storage.sol"]["Storage"]["metadata"]
    )["output"]["abi"]

#  call deploy.py Will get contract_address
contract_address = os.getenv("CONTRACT_ADDRESS")

nonce = w3.eth.get_transaction_count(my_address)

#  Instantiate the contract object 
storage = w3.eth.contract(address=contract_address, abi=abi)

print("get person named " + inName + " from people map")
name, age = storage.functions.getFromPeopleMap(inName).call()

if name == "none" and int(age) == 0:
    print("no person exists with name: " + inName)
else:
    print("received back name: " + name + ", age: " + str(age))

