import allure
import pytest

ALLOWED_CLIENTS = []
DENIED_CLIENTS = []


@pytest.fixture(scope="class")
def prepare_account(operator, faucet, web3_client):
    # """Create new account for tests and save operator pre/post balances"""
    # start_neon_balance = operator.get_neon_balance()
    # start_sol_balance = operator.get_solana_balance()
    # with allure.step(f"Operator initial balance: {start_neon_balance / LAMPORT_PER_SOL} NEON {start_sol_balance / LAMPORT_PER_SOL} SOL"):
    #     pass
    # with allure.step("Create account for tests"):
    #     acc = web3_client.eth.account.create()
    # with allure.step(f"Request 100 NEON from faucet for {acc.address}"):
    #     faucet.request_neon(acc.address, 100)
    #     assert web3_client.get_balance(acc) == 100
    # yield acc
    # end_neon_balance = operator.get_neon_balance()
    # end_sol_balance = operator.get_solana_balance()
    # with allure.step(f"Operator end balance: {end_neon_balance / LAMPORT_PER_SOL} NEON {end_sol_balance / LAMPORT_PER_SOL} SOL"):
    #     pass

    pass


@allure.story("Whitelist")
class TestWhitelist():
    class TestAllowedClient():
        '''
        Whitelisted client accesses faucet
        Whitelisted client requests balance
        Whitelisted client sends tokens
        Whitelisted client is able to receive transferred tokens
        Whitelisted client is able to receive SPL token
        Whitelisted client is able to connect to Neonpass
        Whitelisted client's balance could be supplied with tokens by Airdropper
        '''
        def test_allowed_client_is_able_to_access_faucet():
            '''Whitelisted client accesses faucet'''
            # request faucet
            # check balance
            pass

        def test_allowed_client_is_able_to_request_balance():
            '''Whitelisted client requests balance'''
            # request balance
            pass

        def test_allowed_client_is_able_to_send_tokens():
            '''Whitelisted client sends tokens'''
            # request faucet
            # check balance
            # request faucet
            # check balance
            # send tokens
            pass

        def test_allowed_client_is_able_to_receive_transferred_tokens():
            '''Whitelisted client is able to receive transferred tokens'''
            # request faucet
            # check balance
            # request faucet
            # check balance
            # send tokens
            pass

        @pytest.mark.skip("later")
        def test_allowed_client_is_able_to_receive_spl_token():
            '''Whitelisted client is able to receive SPL token'''
            pass

        @pytest.mark.skip("later")
        def test_allowed_client_is_able_to_connect_to_neonpass():
            '''Whitelisted client is able to connect to Neonpass'''
            pass

        def test_allowed_client_is_able_to_be_supplied_by_airdropper():
            '''Whitelisted client's balance could be supplied with tokens by Airdropper'''
            # request faucet
            # check balance
            # request faucet
            # check balance
            # send tokens
            pass

    class TestDeniedClient():
        '''
        Non-whitelisted client accesses faucet
        Denied client accesses faucet
        Non-whitelisted client requests balance
        Denied client requests balance
        Non-whitelisted client sends tokens
        Denied client sends tokens
        Non-whitelisted client is able to receive transferred tokens
        Denied client is able to receive transferred tokens
        Non-whitelisted client is able to receive SPL token
        Denied client is able to receive SPL token
        Non-whitelisted client is able to connect to Neonpass
        Denied client is able to connect to Neonpass
        Non-whitelisted client's balance could not be supplied with tokens by Airdropper
        Denied client's balance could not be supplied with tokens by Airdropper
        '''
        def test_denied_client_does_not_access_faucet():
            '''Denied client accesses faucet'''
            # request faucet
            # check balance
            pass

        def test_denied_client_fails_to_request_balance():
            '''Denied client requests balance'''
            # request balance
            pass

        def test_denied_client_fails_to_send_tokens():
            '''Denied client sends tokens'''
            # request faucet
            # check balance
            # request faucet
            # check balance
            # send tokens
            pass

        def test_denied_client_fails_to_receive_transferred_tokens():
            '''Denied client is able to receive transferred tokens'''
            # request faucet
            # check balance
            # request faucet
            # check balance
            # send tokens
            pass

        @pytest.mark.skip("later")
        def test_denied_client_fails_to_receive_spl_token():
            '''Denied client is able to receive SPL token'''
            pass

        @pytest.mark.skip("later")
        def test_denied_client_fails_to_connect_to_neonpass():
            '''Denied client is able to connect to Neonpass'''
            pass

        @pytest.mark.skip(
            'airdropper works only with transactions, there should not be transactions for denied clients'
        )
        def test_denied_client_is_never_supplied_by_airdropper():
            # Note: airdropper works only with transactions, there should not be transactions for denied clients
            pass

    class TestAllowedContract():
        '''
        Whitelisted client accesses a whitelisted contract
        Whitelisted client deploys a whitelisted contract
        Whitelisted client deletes a whitelisted contract
        Whitelisted client runs a whitelisted contract, which in turn deploys a non-whitelisted contract
        Whitelisted client runs a whitelisted contract, which in turn deploys a whitelisted contract
        '''
        pass

    class TestDeniedContract():
        '''
        Whitelisted client accesses a non-whitelisted contract
        Whitelisted client deploys a non-whitelisted contract
        Whitelisted client deletes a non-whitelisted contract
        Whitelisted client accesses a denied (prohibited) contract
        Whitelisted client deploys a denied contract
        Whitelisted client deletes a denied contract
        Whitelisted client runs a whitelisted contract, which in turn deploys a non-whitelisted contract
        '''
        pass
