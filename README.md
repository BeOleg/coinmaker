# Coinmaker

Coinmaker is a python program for generating new alternative cryptocurrencies (altcoins).  It does so by modifying the sourc of a base coin.

# Usage

python coinmaker.py [options]

optional arguments:
  -h, --help            show this help message and exit
  -n Bitcoin, --coin-name Bitcoin
                        Name for coin
  -s BTC, --coin-code BTC
                        3-letter code for coin
  -u UUID, --coin-uuid UUID
                        UUID for coin
  -i INITIAL_SUBSIDY, --initial-subsidy INITIAL_SUBSIDY
                        First reward for miners
  -l HALVING_INTERVAL, --halving-interval HALVING_INTERVAL
                        Reward cuts in half after this many blocks
  -g BLOCK1_VALUE, --block1-value BLOCK1_VALUE
                        Value of block 1
  -t BLOCK_TIME, --block-time BLOCK_TIME
                        Time in seconds to generate blocks
  -r RETARGET_NUM, --retarget-num RETARGET_NUM
                        Retarget the difficulty after this long
  -m MAX_MONEY, --max-money MAX_MONEY
                        Maximum money for the network
  -p PORT, --port PORT  Port to connect to other full nodes
  --port-testing PORT_TESTING
                        Port to connect to other nodes on testnet
  --rpcport RPCPORT     Port for RPC connections
  --rpcport-testing RPCPORT_TESTING
                        Port for RPC connections on testnet
  -w WEBSITE, --website WEBSITE
                        Website host
  -a ADDRESS_VERSION, --address-version ADDRESS_VERSION
                        Version number for regular addresses, see
                        https://en.bitcoin.it/wiki/List_of_address_prefixes
  --address-version-testing ADDRESS_VERSION_TESTING
                        Version number for testnet addresses
  --timestamp TIMESTAMP
                        The headline that proves the unix time is valid
  --time TIME           The unix timecode of the genesis block
  --pubkey PUBKEY       The pubkey that the genesis coins are sent to
  --nonce NONCE         The winning nonce for the mined genesis block
  --merkle_hash MERKLE_HASH
                        The merkle hash of the genesis block
  --genesis_hash GENESIS_HASH
                        The hash of the genesis block
  --splash_image SPLASH_IMAGE
                        Splash image
  --icon_ico ICON_ICO   Icon ico format
  --icon_png ICON_PNG   Icon png format

