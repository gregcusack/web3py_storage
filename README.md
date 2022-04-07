Start by launching Ganache!


Setup python environment
```
python3.9 -m venv venv/
source venv/bin/activate
python -m pip install Web3 python-dotenv py-solc-x
```

Create `.env` file. For example:
```
GANACHE_RPC_URL=http://127.0.0.1:7545

ACCOUNT_ADDRESS=<public_address>
PRIVATE_KEY=<private_key>

ACCOUNT2_ADDRESS=<public_address>
ACCOUNT2_PRIVATE_KEY=<private_key>

CONTRACT_ADDRESS=<contract_address>
```

Compiling, Deploying, and interacting with smart contract
```
python base.py
python deploy.py

python add_person.py <name> <age>
python get_person.py <name> 
python delete_person.py <name>

python add_person_not_owner.py <name> <age> # will fail -> has onlyOwners modifier
python get_person_not_owner.py <name> # will succeed -> public function
```

If you want to interact with the `people` array structure, you can call:
```
python call_storage_list.py
```
