from bitcoinrpc.authproxy import AuthServiceProxy

# Set up RPC connection
rpc_user = "your_rpc_user"
rpc_password = "your_rpc_password"
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:8332")

# Generate a new SegWit address
segwit_address = rpc_connection.getnewaddress("", "bech32")

# Print and save the address
print("Generated SegWit Address:", segwit_address)
