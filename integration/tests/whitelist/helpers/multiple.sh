
#!/bin/sh
# neon_revision = "cf20aac797114fc2741b92a5b0cac424637d68f5"
solana_rul = 
evm_loader_id = "eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU"
mint_authority_json_file = 
permission = "allow" # "deny"
grantee = "client" # "contract"
neon_eth_address = "53DfF883gyixYNXnM7s5xhdeyV8mVk9T4i2hGV9vG9io"
address_list_file = "external/addresses.txt"
# external/set_single_acct_permission.sh solana_url evm_loader_id mint_authority_json_file permission grantee neon_eth_address
external/set_many_accts_permission.sh solana_url evm_loader_id mint_authority_json_file permission grantee address_list_file
