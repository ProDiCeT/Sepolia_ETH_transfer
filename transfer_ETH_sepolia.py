import streamlit as st
from web3 import Web3

st.set_page_config(page_title="ETH transfer sepolia testnet", layout="centered")

st.title("💸 ETH transfer - Sepolia Testnet")

private_key = st.text_input("🔑 private key", type="password")
destination = st.text_input("🎯 receiving address (0x...)")
amount_eth = st.number_input("💰 ETH amount", min_value=0.0001, value=0.01, step=0.001)
send_button = st.button("🚀 send")

if send_button:
    if not private_key.startswith("0x") or len(private_key) != 66:
        st.error("❌ invalid private key.")
    elif not Web3.is_address(destination):
        st.error("❌ invalid receiving address.")
    else:
        try:
            rpc_url = "https://sepolia.infura.io/v3/your_private_key" 
            w3 = Web3(Web3.HTTPProvider(rpc_url))

            if not w3.is_connected():
                st.error("❌ no sepolia testnet connection.")
            else:
                account = w3.eth.account.from_key(private_key)
                sender = account.address
                balance = w3.eth.get_balance(sender)
                balance_eth = w3.from_wei(balance, 'ether')

                st.write(f"📤 sender address : `{sender}`")
                st.write(f"💼 Sepolia balance : `{balance_eth:.4f} ETH`")

                value = w3.to_wei(amount_eth, 'ether')
                gas = 21000
                gas_price = w3.eth.gas_price
                fee = gas * gas_price

                if balance < (value + fee):
                    st.error("❌ insufficient amount.")
                else:
                    tx = {
                        'nonce': w3.eth.get_transaction_count(sender),
                        'to': destination,
                        'value': value,
                        'gas': gas,
                        'gasPrice': gas_price,
                        'chainId': 11155111
                    }

                    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
                    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

                    st.success("✅ Transaction successful !")
                    st.markdown(f"🔗 [See transaction](https://sepolia.etherscan.io/tx/0x{tx_hash.hex()})")
        except Exception as e:
            st.error(f"⚠️ Erreur : {e}")

