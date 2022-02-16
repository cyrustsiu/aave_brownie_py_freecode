from scripts.helpful_scripts import get_account
from brownie import interface, config, network


def main():
    withdraw_weth()


def withdraw_weth():
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(
        config["networks"][network.show_active()]["weth_token"])
    ammount = 0.1 * 10 ** 18
    tx = weth.withdraw(ammount, {"from": account})
    print("Withdrew 0.1 WETH")
    return tx
