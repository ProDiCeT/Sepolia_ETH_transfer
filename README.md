# ETH_transfer-Sepolia testnet
python script to transfert ETH from sepolia testnet

# 💸 ETH Transfer - Sepolia Testnet

A simple **Streamlit** web app to send Ether on **Sepolia testnet**.  
Designed for developers and learners experimenting with Ethereum transactions in a safe test environment.

## 🚀 Features
- Minimal and secure interface (no keys are stored).
- Automatic validation of private key and destination address.
- Direct connection to Sepolia via **Infura** (or any RPC endpoint).
- Displays sender balance, estimated gas fee, and Etherscan transaction link.

## 🧩 Installation
Clone this repository and install the required dependencies:
```bash
git clone https://github.com/<your_username>/eth-transfer-sepolia.git
cd eth-transfer-sepolia
pip install streamlit web3

▶️ Run the app

Start the Streamlit interface:

streamlit run ETH_sepolia_transfer.py

Then open the local link shown in your terminal (usually http://localhost:8501).
⚙️ Configuration

The script connects to the Sepolia testnet using an Infura RPC endpoint:

rpc_url = "https://sepolia.infura.io/v3/<your_infura_project_id>"

👉 Replace <your_infura_project_id> with your own to avoid rate limits.
🧠 Notes

    This app is for educational and testing purposes only.

    Never use private keys containing real funds.

    You can obtain free Sepolia test ETH from public faucets like Google Cloud, Chainlink or QuickNode.

🪙 Author

Created with ❤️ by dnapog

