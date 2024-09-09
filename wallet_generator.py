import json
from eth_account import Account
from tronpy import Tron
from tronpy.keys import PrivateKey

# 生成以太坊（ERC-20）钱包
def generate_erc20_wallet():
    account = Account.create()
    address = account.address
    private_key = account.key.hex()
    print('以太坊地址:', address)
    print('以太坊私钥:', private_key)
    return address, private_key

# 生成 Tron 地址
def generate_tron_wallet():
    private_key = PrivateKey.random()
    address = private_key.public_key.to_base58check_address()
    print('Tron 地址:', address)
    print('Tron 私钥:', private_key.hex())
    return address, private_key.hex()

# 保存钱包信息到本地文件
def save_wallet(tron_address, tron_private_key, erc_address, erc_private_key):
    wallet_info = {
        'tron': {
            'address': tron_address,
            'private_key': tron_private_key
        },
        'erc20': {
            'address': erc_address,
            'private_key': erc_private_key
        }
    }
    with open('wallets.json', 'w') as f:
        json.dump(wallet_info, f, indent=2)
    print('钱包信息已保存到 wallets.json 文件中')

# 从本地文件读取钱包信息
def load_wallet():
    with open('wallets.json', 'r') as f:
        wallet_info = json.load(f)
    print('加载 Tron 地址:', wallet_info['tron']['address'])
    print('加载 Tron 私钥:', wallet_info['tron']['private_key'])
    print('加载 以太坊 地址:', wallet_info['erc20']['address'])
    print('加载 以太坊 私钥:', wallet_info['erc20']['private_key'])
    return wallet_info

# 示例：生成并保存 Tron 和 ERC-20 钱包地址
tron_address, tron_private_key = generate_tron_wallet()
erc_address, erc_private_key = generate_erc20_wallet()
save_wallet(tron_address, tron_private_key, erc_address, erc_private_key)

# 示例：加载已有钱包地址
# wallet = load_wallet()
