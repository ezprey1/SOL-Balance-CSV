# SOL-Balance-CSV
- Python file records SOL address's balances to a CSV named SOLBalance
- Records current date and hour to the CSV
- Change public keys in .env file to record desired wallet balance
- Change RPC_ENDPOINT to ``https://api.devnet.solana.com`` for Devnet in .env
- Change RPC_ENDPOINT to ``https://api.mainnet-beta.solana.com`` for Mainnet in .env
- To record 1 wallet balance rather than 2, replace line 42 w/ ``csvwriter(wallet, file_csv)``
