import allure
import pytest
from typing import Union
from integration.tests.basic.helpers.basic_helpers import DEFAULT_TRANSFER_AMOUNT, FIRST_FAUCET_REQUEST_AMOUNT, \
    GREAT_AMOUNT, NOT_YET_DONE, WAITING_FOR_ERC20, WAITING_FOR_MS, \
    BasicHelpers

NON_EXISTING_ADDRESS = "0xmmmmm"
INVALID_ADDRESS = "0x12345"

ENS_NAME_ERROR = f"ENS name: '{INVALID_ADDRESS}' is invalid."
EIP55_INVALID_CHECKUM = "'Address has an invalid EIP-55 checksum. After looking up the address from the original source, try again.'"

WRONG_TRANSFER_AMOUNT_DATA = [(10), (100), (10.1)]
TRANSFER_AMOUNT_DATA = [(0.01), (1), (1.1)]


@allure.story("Basic: transfer tests")
class TestTransfer(BasicHelpers):
    @allure.step("test: send neon from one account to another")
    @pytest.mark.parametrize("amount", TRANSFER_AMOUNT_DATA)
    def test_send_neon_from_one_account_to_another(self, amount: Union[int,
                                                                       float]):
        """Send neon from one account to another"""
        sender_account = self.create_account_with_balance(GREAT_AMOUNT)
        recipient_account = self.create_account_with_balance(
            FIRST_FAUCET_REQUEST_AMOUNT)

        self.transfer_neon(sender_account, recipient_account, amount)

        self.assert_sender_amount(sender_account.address,
                                  GREAT_AMOUNT - amount)
        self.assert_recipient_amount(recipient_account.address,
                                     FIRST_FAUCET_REQUEST_AMOUNT + amount)

    @pytest.mark.skip(WAITING_FOR_MS)
    @allure.step("test: send spl wrapped account from one account to another")
    def test_send_spl_wrapped_account_from_one_account_to_another(self):
        """Send spl wrapped account from one account to another"""
        pass

    @allure.step("test: send more than exist on account: neon")
    @pytest.mark.parametrize("amount", WRONG_TRANSFER_AMOUNT_DATA)
    def test_send_more_than_exist_on_account_neon(self, amount: Union[int,
                                                                      float]):
        """Send more than exist on account: neon"""
        sender_account = self.create_account_with_balance(
            FIRST_FAUCET_REQUEST_AMOUNT)
        recipient_account = self.create_account_with_balance(
            FIRST_FAUCET_REQUEST_AMOUNT)

        self.check_value_error_if_less_than_required(sender_account,
                                                     recipient_account, amount)

        self.assert_sender_amount(sender_account.address,
                                  FIRST_FAUCET_REQUEST_AMOUNT)
        self.assert_recipient_amount(recipient_account.address,
                                     FIRST_FAUCET_REQUEST_AMOUNT)

    @pytest.mark.skip(WAITING_FOR_MS)
    @allure.step(
        "test: send more than exist on account: spl (with different precision)"
    )
    @pytest.mark.parametrize("amount", TRANSFER_AMOUNT_DATA)
    def test_send_more_than_exist_on_account_spl(self, amount):
        """Send more than exist on account: spl (with different precision)"""
        pass

    @pytest.mark.skip(WAITING_FOR_ERC20)
    @allure.step("test: send more than exist on account: ERC20")
    def test_send_more_than_exist_on_account_erc20(self):
        """Send more than exist on account: ERC20"""
        pass

    @allure.step("test: send zero: neon")
    def test_zero_neon(self):
        """Send zero: neon"""
        sender_account = self.create_account_with_balance(
            FIRST_FAUCET_REQUEST_AMOUNT)
        recipient_account = self.create_account_with_balance(
            FIRST_FAUCET_REQUEST_AMOUNT)

        self.transfer_zero_neon(sender_account, recipient_account, 0)

        self.assert_sender_amount(sender_account.address,
                                  FIRST_FAUCET_REQUEST_AMOUNT)
        self.assert_recipient_amount(recipient_account.address,
                                     FIRST_FAUCET_REQUEST_AMOUNT)

    @pytest.mark.skip(WAITING_FOR_MS)
    @allure.step("test: send zero: spl (with different precision)")
    def test_zero_spl(self):
        """Send zero: spl (with different precision)"""
        pass

    # @pytest.mark.skip(NOT_YET_DONE)
    # @pytest.fail(NOT_YET_DONE)
    @pytest.mark.xfail()
    @allure.step("test: send zero: ERC20")
    def test_zero_erc20(self):
        """Send zero: ERC20"""
        pass

    @allure.step("test: send negative sum from account: neon")
    def test_send_negative_sum_from_account_neon(self):
        """Send negative sum from account: neon"""
        sender_account = self.create_account_with_balance(
            FIRST_FAUCET_REQUEST_AMOUNT)
        recipient_account = self.create_account_with_balance(
            FIRST_FAUCET_REQUEST_AMOUNT)

        self.transfer_zero_neon(sender_account, recipient_account, -1)

        self.assert_sender_amount(sender_account.address,
                                  FIRST_FAUCET_REQUEST_AMOUNT)
        self.assert_recipient_amount(recipient_account.address,
                                     FIRST_FAUCET_REQUEST_AMOUNT)

    @pytest.mark.skip(WAITING_FOR_MS)
    @allure.step(
        "test: send negative sum from account: spl (with different precision)")
    def test_send_negative_sum_from_account_spl(self):
        """Send negative sum from account: spl (with different precision)"""
        pass

    @pytest.mark.skip(WAITING_FOR_ERC20)
    @allure.step("test: send negative sum from account: ERC20")
    def test_send_negative_sum_from_account_erc20(self):
        """Send negative sum from account: ERC20"""
        pass

    @allure.step("test: send token to an invalid address")
    def test_send_token_to_an_invalid_address(self):
        """Send token to an invalid address"""
        sender_account = self.create_account_with_balance(
            FIRST_FAUCET_REQUEST_AMOUNT)
        recipient_address = INVALID_ADDRESS

        self.transfer_to_invalid_address(sender_account, recipient_address,
                                         DEFAULT_TRANSFER_AMOUNT,
                                         ENS_NAME_ERROR)

        self.assert_sender_amount(sender_account.address,
                                  FIRST_FAUCET_REQUEST_AMOUNT)

    @allure.step("test: send token to a non-existing address")
    def test_send_more_token_to_non_existing_address(self):
        """Send token to a non-existing address"""
        sender_account = self.create_account_with_balance(
            FIRST_FAUCET_REQUEST_AMOUNT)
        recipient_address = sender_account.address.replace('1', '2').replace(
            '3', '4')

        self.transfer_to_invalid_address(sender_account, recipient_address,
                                         DEFAULT_TRANSFER_AMOUNT,
                                         EIP55_INVALID_CHECKUM)

        self.assert_sender_amount(sender_account.address,
                                  FIRST_FAUCET_REQUEST_AMOUNT)
