# ERC-20 Token Transfer on Arbitrum

This Python script allows you to transfer ERC-20 tokens on the Arbitrum network using Web3.py.

## Prerequisites

1. **Python Installation**: Ensure you have Python 3 installed.
2. **Install Dependencies**:
   ```sh
   pip install web3
   ```
3. **Arbitrum RPC URL**: Get an RPC URL from providers like Alchemy, Infura, or the official Arbitrum RPC.
4. **Wallet Details**:
   - Private key of the sender wallet (Keep it secure!).
   - Wallet addresses of the sender and receiver.
5. **Token Contract Address**: Find the ERC-20 token contract address on Arbitrum.

## Usage

1. Clone this repository or save the script.
2. Update the script with:
   - Your **private key**
   - **Sender and receiver wallet addresses**
   - **ERC-20 token contract address**
   - **Token decimals** (to calculate the correct transfer amount)
3. Run the script:
   ```sh
   python transfer_erc20.py
   ```
4. The script will sign and send the transaction, displaying the transaction hash upon success.

## Configuration

Modify these variables in `transfer_erc20.py`:
```python
ARBITRUM_RPC_URL = "https://arb1.arbitrum.io/rpc"
PRIVATE_KEY = "your_private_key_here"
SENDER_ADDRESS = "your_wallet_address_here"
RECEIVER_ADDRESS = "receiver_wallet_address_here"
TOKEN_ADDRESS = "0xTokenContractAddressHere"
DECIMALS = 18  # Replace with actual token decimals
AMOUNT = 1  # Token amount to send
```

## Notes
- Ensure your wallet has enough ETH to cover gas fees on Arbitrum.
- Do not share your private key.
- Adjust gas limits if needed for faster transactions.

## License
This project is licensed under the MIT License.

