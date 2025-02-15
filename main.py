from web3 import Web3
import json

# Arbitrum RPC URL (Replace with your own)
ARBITRUM_RPC_URL = "https://arb1.arbitrum.io/rpc"

# Connect to Arbitrum network
web3 = Web3(Web3.HTTPProvider(ARBITRUM_RPC_URL))

# Check connection
if not web3.is_connected():
    raise Exception("Failed to connect to Arbitrum network")

# Wallet details (Replace with your own)
PRIVATE_KEY = "your_private_key_here"
SENDER_ADDRESS = "your_wallet_address_here"
RECEIVER_ADDRESS = "receiver_wallet_address_here"

# ERC-20 Token Contract (Replace with the actual token contract)
TOKEN_ADDRESS = "0xTokenContractAddressHere"
TOKEN_ABI = json.loads('[{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]')

# Initialize token contract
token_contract = web3.eth.contract(address=TOKEN_ADDRESS, abi=TOKEN_ABI)

# Amount to send (Replace with your amount, considering decimals)
DECIMALS = 18  # Replace with token decimals
AMOUNT = 1  # Token amount to send
TOKEN_AMOUNT = int(AMOUNT * (10 ** DECIMALS))  # Convert to smallest unit

# Get nonce for sender account
nonce = web3.eth.get_transaction_count(SENDER_ADDRESS)

# Build transaction
tx = token_contract.functions.transfer(RECEIVER_ADDRESS, TOKEN_AMOUNT).build_transaction({
    'from': SENDER_ADDRESS,
    'nonce': nonce,
    'gas': 100000,  # Adjust based on network conditions
    'gasPrice': web3.eth.gas_price,
})

# Sign transaction
signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

# Send transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Get transaction hash
print(f"Transaction sent! TX Hash: {web3.to_hex(tx_hash)}")
