from typing import Union
import allure
import pytest
from integration.tests.basic.helpers.assert_message import AssertMessage
from integration.tests.basic.helpers.rpc_request_params_factory import RpcRequestParamsFactory
from integration.tests.basic.model.json_rpc_response import JsonRpcResponse
from integration.tests.basic.helpers.basic_helpers import FIRST_FAUCET_REQUEST_AMOUNT, GREAT_AMOUNT, NOT_YET_DONE, BasicHelpers
from integration.tests.basic.helpers.rpc_request_factory import RpcRequestFactory
from integration.tests.basic.model.json_rpc_request_parameters import JsonRpcRequestParams
from integration.tests.basic.model.tags import Tag
from integration.tests.basic.test_transactions import SAMPLE_AMOUNT
'''
12.	Verify implemented rpc calls work
12.1.	eth_getBlockByHash		
12.2.	eth_getBlockByNumber		
12.11.	eth_blockNumber		
12.12.	eth_call		
12.13.	eth_estimateGas		
12.14.	eth_gasPrice		
12.22.	eth_getLogs		
12.30.	eth_getBalance		
12.32.	eth_getTransactionCount		
12.33.	eth_getCode		
12.35.	eth_sendRawTransaction		
12.36.	eth_getTransactionByHash		
12.39.	eth_getTransactionReceipt		
12.40.	eht_getStorageAt		
12.61.	web3_clientVersion		
12.63.	net_version
'''

# TODO: fix earliest and penging if possible
TAGS_TEST_DATA = [(Tag.EARLIEST, True), (Tag.EARLIEST, False),
                  (Tag.LATEST, True), (Tag.LATEST, False), (Tag.PENDING, True),
                  (Tag.PENDING, False)]


@allure.story("Basic: Json-RPC call tests - blocks")
class TestRpcCallsBlocks(BasicHelpers):

    # TODO: implement numerous variants
    @allure.step("test: verify implemented rpc calls work eth_getBlockByHash")
    def test_rpc_call_eth_getBlockByHash(self):
        """Verify implemented rpc calls work eth_getBlockByHash"""
        sender_account = self.create_account_with_balance(GREAT_AMOUNT)
        recipient_account = self.create_account_with_balance(
            FIRST_FAUCET_REQUEST_AMOUNT)

        tx_receipt = self.transfer_neon(sender_account, recipient_account,
                                        SAMPLE_AMOUNT)

        #
        print("----------------------------------------------------")
        print(tx_receipt)
        '''
----------------------------------------------------
AttributeDict({'transactionHash': HexBytes('0xdb17af3d719ba9c32ed98741eb4b3fb568aadc7f0ba4a981fd494aef9a723345'), 'transactionIndex': 0, 'blockHash': HexBytes('0x33f9147e12a0d264ccc31cf12e4c90010c3c6fd2b370211f337616ba3de87430'), 'blockNumber': 1010220, 'from': '0x98CeE1c921D16ed20B58C8f9d8A3A128492A5f7B', 'to': '0x3E14f865E7332913F1de50d7B5Bb0fA6Cc335359', 'gasUsed': 15000, 'cumulativeGasUsed': 15000, 'contractAddress': None, 'logs': [], 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
:::::::::::::::::::::::::::::::::::::::::::
        '''
        print(self.web3_client.gas_price())
        print(self.web3_client.gas_price() * 15000)
        print(":::::::::::::::::::::::::::::::::::::::::::")
        #
        model = RpcRequestFactory.get_block_by_hash(
            req_id=1, params=JsonRpcRequestParams())

        # TODO: remove
        print(model)
        #

        response = self.jsonrpc_requester.request_json_rpc(model)
        actual_result = self.jsonrpc_requester.deserialize_response(response)

        assert actual_result.id == model.id, AssertMessage.WRONG_ID.value
        # assert self.assert_no_error_object(
        #     actual_result), AssertMessage.CONTAINS_ERROR
        # assert self.assert_result_object(
        #     actual_result), AssertMessage.DOES_NOT_CONTAIN_RESULT

    @pytest.mark.parametrize("quantity_tag,full_trx", TAGS_TEST_DATA)
    @allure.step(
        "test: verify implemented rpc calls work eth_getBlockByNumber via tags"
    )
    def test_rpc_call_eth_getBlockByNumber_via_tags(self,
                                                    quantity_tag: Union[int,
                                                                        Tag],
                                                    full_trx: bool):
        """Verify implemented rpc calls work eth_getBlockByNumber"""
        params = RpcRequestParamsFactory.get_block_by_number(
            quantity_tag, full_trx)
        model = RpcRequestFactory.get_block_by_number(params=params)

        response = self.jsonrpc_requester.request_json_rpc(model)
        actual_result = self.jsonrpc_requester.deserialize_response(response)

        assert actual_result.id == model.id, AssertMessage.WRONG_ID.value
        # assert self.assert_no_error_object(
        #     actual_result), AssertMessage.CONTAINS_ERROR
        # assert self.assert_result_object(
        #     actual_result), AssertMessage.DOES_NOT_CONTAIN_RESULT

    @pytest.mark.parametrize("quantity_tag,full_trx", TAGS_TEST_DATA)
    @allure.step(
        "test: verify implemented rpc calls work eth_getBlockByNumber via numbers"
    )
    def test_rpc_call_eth_getBlockByNumber_via_numbers(self):
        """Verify implemented rpc calls work eth_getBlockByNumber"""
        sender_account = self.create_account_with_balance(GREAT_AMOUNT)
        recipient_account = self.create_account_with_balance(
            FIRST_FAUCET_REQUEST_AMOUNT)

        tx_receipt = self.transfer_neon(sender_account, recipient_account,
                                        SAMPLE_AMOUNT)

        params = RpcRequestParamsFactory.get_block_by_number(
            tx_receipt.blockNumber, True)
        model = RpcRequestFactory.get_block_by_number(params=params)

        response = self.jsonrpc_requester.request_json_rpc(model)
        actual_result = self.jsonrpc_requester.deserialize_response(response)

        assert actual_result.id == model.id, AssertMessage.WRONG_ID.value
        # assert self.assert_no_error_object(
        #     actual_result), AssertMessage.CONTAINS_ERROR
        # assert self.assert_result_object(
        #     actual_result), AssertMessage.DOES_NOT_CONTAIN_RESULT

    @allure.step("test: verify implemented rpc calls work eth_blockNumber")
    def test_rpc_call_eth_blockNumber(self):
        """Verify implemented rpc calls work work eth_blockNumber"""
        model = RpcRequestFactory.get_block_number(params=[])
        response = self.jsonrpc_requester.request_json_rpc(model)
        actual_result = self.jsonrpc_requester.deserialize_response(response)

        assert actual_result.id == model.id, AssertMessage.WRONG_ID.value
        assert isinstance(actual_result,
                          JsonRpcResponse), AssertMessage.WRONG_TYPE.value
        assert '0x' in actual_result.result, AssertMessage.DOES_NOT_START_WITH_0X.value