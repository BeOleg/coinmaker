#!/usr/bin/python
"""
This script produces new altcoins with specified parameters.
"""
from .utils import copy_anything, replace, rename
from .settings import SETTINGS
import os
import uuid
import shutil
import argparse

__author__ = "Spencer Dupre"
__copyright__ = "Copyright 2015"
__credits__ = ["Spencer Dupre", "The Bitcoin Developers"]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Spencer Dupre"
__email__ = "spencer.dupre@gmail.com"
__status__ = "Alpha"


DEFAULT_TIMESTAMP = "The Times web front page 22-Jul-2011 Europe" \
                    " hails 'historic' deal to save single currency"

DEFAULT_PUBKEY = "04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea" \
                 "1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a" \
                 "4c702b6bf11d5f"

DEFAULT_MERKLE = "e61339a40aa4e90e983fe0d64cf09eed5fa1e6eac227b6761f06ac7af1" \
                 "929baf"

DEFAULT_GENESIS = "0000000062558fec003bcbf29e915cddfc34fa257dc87573f28e4520d" \
                  "1c7c11e"


def create(coin_name="Bitcoin",
           coin_code="BTC",
           coin_uuid=str(uuid.uuid4().hex),
           init_subsidy=50,
           halving_interval=210000,
           block1_value=50,
           block_time=600,
           retarget_num=2016,
           max_money=21000000,
           port=8333,
           testport=18333,
           rpcport=8332,
           rpctestport=18332,
           website="example.com",
           address_version=0,
           address_test_version=111,
           timestamp=DEFAULT_TIMESTAMP,
           time=1311305081,
           pubkey=DEFAULT_PUBKEY,
           nonce=3085127155,
           merkle_hash=DEFAULT_MERKLE,
           genesis_hash=DEFAULT_GENESIS,
           splash_image=None,
           icon_ico=None,
           icon_png=None,
           ):

    blocks_per_day = 60*60*24 / block_time

    if not os.path.exists(SETTINGS.working_dir):
        os.makedirs(SETTINGS.working_dir)

    random_dir = os.path.join(SETTINGS.working_dir, coin_uuid)
    os.makedirs(random_dir)

    copy_anything(SETTINGS.source_dir, os.path.join(random_dir, coin_name))
    os.chdir(os.path.join(random_dir, coin_name))
    coindir = os.getcwd()

    reps = [
        ['CM_LowercaseCoinCode', coin_code.lower()],
        ['CM_AllCapsCoinCode', coin_code.upper()],
        ['CM_LowercaseCoinName', coin_name.lower()],
        ['CM_AllCapsCoinName', coin_name.upper()],
        ['CM_UppercaseCoinName', coin_name.title()],
        ['CM_LowercaseCoinName', coin_name.lower()],
        ['CM_UppercaseCoinName', coin_name.title()],
        ['CM_AllCApsCoinName', coin_name.upper()],
        ['CM_RPCPort', str(rpcport)],
        ['CM_RPCTestnetPort', str(rpctestport)],
        ['CM_Port', str(port)],
        ['CM_TestnetPort', str(testport)],
        ['CM_WebsiteDomain', str(website)],
        ['CM_InitialSubsidy', str(init_subsidy)],
        ['CM_MaxMoney', str(max_money)],
        ['CM_BlocksPerDay', str(blocks_per_day)],
        ['CM_AddressVersion', str(address_version)],
        ['CM_HalvingIntervalBlocks', str(halving_interval)],
        ['CM_GenesisHeadline', str(timestamp)],
        ['CM_GenesisTimecode', str(int(time))],
        ['CM_GenesisPubkey', str(pubkey)],
        ['CM_GenesisNonce', str(int(nonce))],
        ['CM_GenesisMerkleHash', str(merkle_hash)],
        ['CM_GenesisHash', str(genesis_hash)],
        ['CM_BlocksPerDay', str(blocks_per_day)],
        ['CM_GenesisHash', str(genesis_hash)],
        ["CM_RetargetBlocks", str(retarget_num)],
        ["CM_BlockOneValue", str(int(block1_value))],
        ["CM_TargetTimespanSeconds", str(int(block_time))],
        ["CM_BlocksPerDay", str(blocks_per_day)],
        ["CM_RetargetBlocks", str(retarget_num)],
    ]

    replace(coindir, reps, ignore_types=[".png", ".ico"])

#   Copy image files
    if splash_image:
        try:
            shutil.copyfile(splash_image, 'qt/res/images/splash.png')
        except IOError:
            pass

    if icon_ico:
        try:
            shutil.copyfile(icon_ico,
                            'qt/res/icons/{0}.ico'.format(coin_name.lower())
                            )
        except IOError:
            pass

    if icon_png:
        try:
            shutil.copyfile(icon_png,
                            'qt/res/icons/{0}.png'.format(coin_name.lower())
                            )
            shutil.copyfile(icon_png, 'qt/res/icons/toolbar.png')
        except IOError:
            pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',
                        '--coin-name',
                        metavar="Bitcoin",
                        default="Bitcoin",
                        help='Name for coin')
    parser.add_argument('-s',
                        '--coin-code',
                        metavar="BTC",
                        default="BTC",
                        help='3-letter code for coin')
    parser.add_argument('-u',
                        '--coin-uuid',
                        metavar="UUID",
                        default=str(uuid.uuid4().hex),
                        help='UUID for coin')
    parser.add_argument('-i',
                        '--initial-subsidy',
                        default=50,
                        type=int,
                        help='First reward for miners')
    parser.add_argument('-l',
                        '--halving-interval',
                        default=210000,
                        type=int,
                        help='Reward cuts in half after this many blocks')
    parser.add_argument('-g',
                        '--block1-value',
                        default=50,
                        type=int,
                        help='Value of block 1')
    parser.add_argument('-t',
                        '--block-time',
                        default=600,
                        help='Time in seconds to generate blocks')
    parser.add_argument('-r',
                        '--retarget-num',
                        default=2016,
                        type=int,
                        help='Retarget the difficulty after this long')
    parser.add_argument('-m',
                        '--max-money',
                        default=21000000,
                        type=int,
                        help='Maximum money for the network')
    parser.add_argument('-p',
                        '--port',
                        default=8333,
                        type=int,
                        help='Port to connect to other full nodes')
    parser.add_argument('--port-testing',
                        default=18333,
                        type=int,
                        help='Port to connect to other nodes on testnet')
    parser.add_argument('--rpcport',
                        default=8332,
                        type=int,
                        help='Port for RPC connections')
    parser.add_argument('--rpcport-testing',
                        default=18332,
                        type=int,
                        help='Port for RPC connections on testnet ')
    parser.add_argument('-w',
                        '--website',
                        default="bitcoin.org",
                        help='Website host')
    parser.add_argument('-a',
                        '--address-version',
                        default=0,
                        type=int,
                        help='Version number for regular addresses'
                        ', see https://en.bitcoin.it/wiki/'
                        'List_of_address_prefixes')
    parser.add_argument('--address-version-testing',
                        default=111,
                        type=int,
                        help='Version number for testnet addresses')
    parser.add_argument('--timestamp',
                        default=DEFAULT_TIMESTAMP,
                        help='The headline that proves the unix time is valid')
    parser.add_argument('--time',
                        default=1311305081,
                        type=int,
                        help='The unix timecode of the genesis block')
    parser.add_argument('--pubkey',
                        default=DEFAULT_PUBKEY,
                        help='The pubkey that the genesis coins are sent to')
    parser.add_argument('--nonce',
                        default=3085127155,
                        type=int,
                        help='The winning nonce for the mined genesis block')
    parser.add_argument('--merkle_hash',
                        default=DEFAULT_MERKLE,
                        help='The merkle hash of the genesis block')
    parser.add_argument('--genesis_hash',
                        default=DEFAULT_GENESIS,
                        help='The hash of the genesis block')
    parser.add_argument('--splash_image', default=None, help='Splash image')
    parser.add_argument('--icon_ico', default=None, help='Icon ico format')
    parser.add_argument('--icon_png', default=None, help='Icon png format')
    args = parser.parse_args()

    create(coin_name=args.coin_name,
           coin_code=args.coin_code,
           coin_uuid=args.coin_uuid,
           init_subsidy=args.initial_subsidy,
           halving_interval=args.halving_interval,
           block1_value=args.block1_value,
           block_time=args.block_time,
           retarget_num=args.retarget_num,
           max_money=args.max_money,
           port=args.port,
           testport=args.port_testing,
           rpcport=args.rpcport,
           rpctestport=args.rpcport_testing,
           website=args.website,
           address_version=args.address_version,
           address_test_version=args.address_version_testing,
           timestamp=args.timestamp,
           time=args.time,
           pubkey=args.pubkey,
           nonce=args.nonce,
           merkle_hash=args.merkle_hash,
           genesis_hash=args.genesis_hash,
           splash_image=args.splash_image,
           icon_ico=args.icon_ico,
           icon_png=args.icon_png)

if __name__ == "__main__":
    main()
