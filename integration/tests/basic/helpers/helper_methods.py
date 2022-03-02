import allure
from integration.tests.basic.helpers.json_rpc_requester import JsonRpcRequester
import pytest
import web3
from _pytest.config import Config
from eth_account import Account
from typing import Optional
from integration.tests.base import BaseTests

FIRST_FAUCET_REQUEST_AMOUNT = 5
SECOND_FAUCET_REQUEST_AMOUNT = 3
GREAT_AMOUNT = 1_000
DEFAULT_TRANSFER_AMOUNT = 3


class BasicHelpers(BaseTests):
    jsonrpc_requester: JsonRpcRequester

    @pytest.fixture(autouse=True)
    def prepare_json_rpc_requester(self, jsonrpc_requester: JsonRpcRequester):
        self.jsonrpc_requester = jsonrpc_requester

    @allure.step("creating a new account")
    def create_account(self) -> Account:
        return self.web3_client.create_account()

    @allure.step("getting balance of account")
    def get_balance(self, address: str) -> int:
        return self.web3_client.eth.get_balance(address)

    @allure.step("requesting faucet for Neon")
    def request_faucet_neon(self, wallet: str, amount: int):
        self.faucet.request_neon(wallet, amount=amount)

    @allure.step("creating a new account with balance")
    def create_account_with_balance(self, amount: int) -> Account:
        account = self.create_account()
        self.request_faucet_neon(account.address, amount)
        return account

    # @allure.step("requesting faucet for ERC20")
    # def request_faucet_erc20(self, wallet: str, amount: int):
    #     self.faucet.request_sol(wallet, amount=amount)

    @allure.step("processing transaction")
    def process_transaction(self,
                            sender_account: Account,
                            recipient_account: Account,
                            amount: int,
                            # gas: Optional[int] = 0,
                            # gas_price: Optional[int] = None,
                            message: str = ""):
        # try:
        # with pytest.raises(ValueError) as error_info:
        #     self.web3_client.send_neon(sender_account, recipient_account,
        #                                amount, gas, gas_price)
        #     print(error_info)
        # assert message in str(error_info.value)

        with pytest.raises(Exception) as error_info:
            self.web3_client.send_neon(sender_account, recipient_account,
                                       amount)
                                    #    , gas, gas_price)
        print(error_info)
        assert message in str(error_info)
        # except ValueError as error_info:
        #     print(error_info)
        #     assert "The account balance is less than required" in str(
        #         error_info)
        # except Exception as error_info:
        #     print(error_info)
        #     assert 1 == 2, f"Error is not ValueError: {error_info}"

    @allure.step("transferring tokens")
    def transfer_neon(self, sender_account: Account,
                      recipient_account: Account,
                      amount: int) -> web3.types.TxReceipt:  # ,
        #   gas: Optional[int] = 0,
        #   gas_price: Optional[int] = None) -> web3.types.TxReceipt:
        self.process_transaction(sender_account, recipient_account, amount,
                                #  gas, gas_price, 
                                 "InvalidInstructionData")

    @allure.step("transferring 0 tokens")
    def transfer_zero_neon(self, sender_account: Account,
                           recipient_account: Account,
                           amount: int) -> web3.types.TxReceipt:  # ,
        # gas: Optional[int] = 0,
        # gas_price: Optional[int] = None) -> web3.types.TxReceipt:
        self.process_transaction(sender_account, recipient_account, amount,
                                #  gas, gas_price, 
                                 "aaa")

    @allure.step("checking less than required")
    def check_value_error_if_less_than_required(
            self, sender_account: Account, recipient_account: Account,
            amount: int) -> web3.types.TxReceipt:  # ,
        # gas: Optional[int] = 0,
        # gas_price: Optional[int] = None):
        self.process_transaction(sender_account, recipient_account, amount,
                                #  gas, gas_price,
                                 "The account balance is less than required")

    def compare_balance(self, expected: int, actual: int, message: str):
        assert actual == expected, message + f"expected balance = {expected}, actual balance = {actual}"

    def assert_amount(self,
                      address: str,
                      expected_amount: int,
                      message: str = ""):
        balance = self.web3_client.fromWei(self.get_balance(address), "ether")
        self.compare_balance(expected_amount, balance, message)

    @allure.step("checking sender balance")
    def assert_sender_amount(self, address: str, expected_amount: int):
        balance = self.web3_client.fromWei(self.get_balance(address), "ether")
        self.compare_balance(expected_amount, balance, "Sender: ")

    @allure.step("checking recipient balance")
    def assert_recipient_amount(self, address: str, expected_amount: int):
        balance = self.web3_client.fromWei(self.get_balance(address), "ether")
        self.compare_balance(expected_amount, balance, "Recipient: ")