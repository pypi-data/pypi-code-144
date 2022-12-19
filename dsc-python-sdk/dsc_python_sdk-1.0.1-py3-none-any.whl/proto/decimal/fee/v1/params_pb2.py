# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: decimal/fee/v1/params.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='decimal/fee/v1/params.proto',
  package='decimal.fee.v1',
  syntax='proto3',
  serialized_options=b'\n\022com.decimal.fee.v1B\013ParamsProtoP\001Z3bitbucket.org/decimalteam/go-smart-node/x/fee/types\242\002\003DFX\252\002\016Decimal.Fee.V1\312\002\016Decimal\\Fee\\V1\342\002\032Decimal\\Fee\\V1\\GPBMetadata\352\002\020Decimal::Fee::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x64\x65\x63imal/fee/v1/params.proto\x12\x0e\x64\x65\x63imal.fee.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xf3!\n\x06Params\x12\\\n\x0btx_byte_fee\x18\x01 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\ttxByteFee\x12\x82\x01\n\x14\x63oin_create_ticker_3\x18\x03 \x01(\tBQ\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x11\x43oinCreateTicker3\xd2\xb4-\ncosmos.DecR\x11\x63oinCreateTicker3\x12\x82\x01\n\x14\x63oin_create_ticker_4\x18\x04 \x01(\tBQ\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x11\x43oinCreateTicker4\xd2\xb4-\ncosmos.DecR\x11\x63oinCreateTicker4\x12\x82\x01\n\x14\x63oin_create_ticker_5\x18\x05 \x01(\tBQ\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x11\x43oinCreateTicker5\xd2\xb4-\ncosmos.DecR\x11\x63oinCreateTicker5\x12\x82\x01\n\x14\x63oin_create_ticker_6\x18\x06 \x01(\tBQ\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x11\x43oinCreateTicker6\xd2\xb4-\ncosmos.DecR\x11\x63oinCreateTicker6\x12\x82\x01\n\x14\x63oin_create_ticker_7\x18\x07 \x01(\tBQ\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x11\x43oinCreateTicker7\xd2\xb4-\ncosmos.DecR\x11\x63oinCreateTicker7\x12]\n\x0b\x63oin_create\x18\x0b \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\ncoinCreate\x12]\n\x0b\x63oin_update\x18\x0c \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\ncoinUpdate\x12Y\n\tcoin_send\x18\r \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x08\x63oinSend\x12`\n\rcoin_send_add\x18\x0e \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x0b\x63oinSendAdd\x12W\n\x08\x63oin_buy\x18\x0f \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x07\x63oinBuy\x12Y\n\tcoin_sell\x18\x10 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x08\x63oinSell\x12h\n\x11\x63oin_redeem_check\x18\x11 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x0f\x63oinRedeemCheck\x12Y\n\tcoin_burn\x18\x12 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x08\x63oinBurn\x12r\n\x16multisig_create_wallet\x18\x15 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x14multisigCreateWallet\x12|\n\x1bmultisig_create_transaction\x18\x16 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x19multisigCreateTransaction\x12x\n\x19multisig_sign_transaction\x18\x17 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x17multisigSignTransaction\x12\x62\n\x0enft_mint_token\x18\x1f \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x0cnftMintToken\x12\x66\n\x10nft_update_token\x18  \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x0enftUpdateToken\x12j\n\x12nft_update_reserve\x18! \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x10nftUpdateReserve\x12\x62\n\x0enft_send_token\x18\" \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x0cnftSendToken\x12\x62\n\x0enft_burn_token\x18# \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x0cnftBurnToken\x12l\n\x13swap_activate_chain\x18) \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x11swapActivateChain\x12p\n\x15swap_deactivate_chain\x18* \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x13swapDeactivateChain\x12\x65\n\x0fswap_initialize\x18+ \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x0eswapInitialize\x12]\n\x0bswap_redeem\x18, \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\nswapRedeem\x12z\n\x1avalidator_create_validator\x18\x33 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x18validatorCreateValidator\x12v\n\x18validator_edit_validator\x18\x34 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x16validatorEditValidator\x12k\n\x12validator_delegate\x18\x35 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x11validatorDelegate\x12\x8a\x01\n\x16validator_delegate_nft\x18\x36 \x01(\tBT\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x14ValidatorDelegateNFT\xd2\xb4-\ncosmos.DecR\x14validatorDelegateNft\x12o\n\x14validator_redelegate\x18\x37 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x13validatorRedelegate\x12\x90\x01\n\x18validator_redelegate_nft\x18\x38 \x01(\tBV\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x16ValidatorRedelegateNFT\xd2\xb4-\ncosmos.DecR\x16validatorRedelegateNft\x12o\n\x14validator_undelegate\x18\x39 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x13validatorUndelegate\x12\x90\x01\n\x18validator_undelegate_nft\x18: \x01(\tBV\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x16ValidatorUndelegateNFT\xd2\xb4-\ncosmos.DecR\x16validatorUndelegateNft\x12n\n\x14validator_set_online\x18; \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x12validatorSetOnline\x12p\n\x15validator_set_offline\x18< \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x13validatorSetOffline\x12r\n\x16\x63ommission_burn_factor\x18= \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x14\x63ommissionBurnFactor\x12`\n\revm_gas_price\x18> \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.DecR\x0b\x65vmGasPrice\x12\x30\n\x06oracle\x18? \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06oracle:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x01\xe8\xa0\x1f\x01\x42\xb0\x01\n\x12\x63om.decimal.fee.v1B\x0bParamsProtoP\x01Z3bitbucket.org/decimalteam/go-smart-node/x/fee/types\xa2\x02\x03\x44\x46X\xaa\x02\x0e\x44\x65\x63imal.Fee.V1\xca\x02\x0e\x44\x65\x63imal\\Fee\\V1\xe2\x02\x1a\x44\x65\x63imal\\Fee\\V1\\GPBMetadata\xea\x02\x10\x44\x65\x63imal::Fee::V1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='decimal.fee.v1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_byte_fee', full_name='decimal.fee.v1.Params.tx_byte_fee', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='txByteFee', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_create_ticker_3', full_name='decimal.fee.v1.Params.coin_create_ticker_3', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\342\336\037\021CoinCreateTicker3\322\264-\ncosmos.Dec', json_name='coinCreateTicker3', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_create_ticker_4', full_name='decimal.fee.v1.Params.coin_create_ticker_4', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\342\336\037\021CoinCreateTicker4\322\264-\ncosmos.Dec', json_name='coinCreateTicker4', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_create_ticker_5', full_name='decimal.fee.v1.Params.coin_create_ticker_5', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\342\336\037\021CoinCreateTicker5\322\264-\ncosmos.Dec', json_name='coinCreateTicker5', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_create_ticker_6', full_name='decimal.fee.v1.Params.coin_create_ticker_6', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\342\336\037\021CoinCreateTicker6\322\264-\ncosmos.Dec', json_name='coinCreateTicker6', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_create_ticker_7', full_name='decimal.fee.v1.Params.coin_create_ticker_7', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\342\336\037\021CoinCreateTicker7\322\264-\ncosmos.Dec', json_name='coinCreateTicker7', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_create', full_name='decimal.fee.v1.Params.coin_create', index=6,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='coinCreate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_update', full_name='decimal.fee.v1.Params.coin_update', index=7,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='coinUpdate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_send', full_name='decimal.fee.v1.Params.coin_send', index=8,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='coinSend', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_send_add', full_name='decimal.fee.v1.Params.coin_send_add', index=9,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='coinSendAdd', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_buy', full_name='decimal.fee.v1.Params.coin_buy', index=10,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='coinBuy', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_sell', full_name='decimal.fee.v1.Params.coin_sell', index=11,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='coinSell', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_redeem_check', full_name='decimal.fee.v1.Params.coin_redeem_check', index=12,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='coinRedeemCheck', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_burn', full_name='decimal.fee.v1.Params.coin_burn', index=13,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='coinBurn', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multisig_create_wallet', full_name='decimal.fee.v1.Params.multisig_create_wallet', index=14,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='multisigCreateWallet', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multisig_create_transaction', full_name='decimal.fee.v1.Params.multisig_create_transaction', index=15,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='multisigCreateTransaction', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multisig_sign_transaction', full_name='decimal.fee.v1.Params.multisig_sign_transaction', index=16,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='multisigSignTransaction', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nft_mint_token', full_name='decimal.fee.v1.Params.nft_mint_token', index=17,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='nftMintToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nft_update_token', full_name='decimal.fee.v1.Params.nft_update_token', index=18,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='nftUpdateToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nft_update_reserve', full_name='decimal.fee.v1.Params.nft_update_reserve', index=19,
      number=33, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='nftUpdateReserve', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nft_send_token', full_name='decimal.fee.v1.Params.nft_send_token', index=20,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='nftSendToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nft_burn_token', full_name='decimal.fee.v1.Params.nft_burn_token', index=21,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='nftBurnToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swap_activate_chain', full_name='decimal.fee.v1.Params.swap_activate_chain', index=22,
      number=41, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='swapActivateChain', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swap_deactivate_chain', full_name='decimal.fee.v1.Params.swap_deactivate_chain', index=23,
      number=42, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='swapDeactivateChain', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swap_initialize', full_name='decimal.fee.v1.Params.swap_initialize', index=24,
      number=43, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='swapInitialize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swap_redeem', full_name='decimal.fee.v1.Params.swap_redeem', index=25,
      number=44, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='swapRedeem', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_create_validator', full_name='decimal.fee.v1.Params.validator_create_validator', index=26,
      number=51, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='validatorCreateValidator', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_edit_validator', full_name='decimal.fee.v1.Params.validator_edit_validator', index=27,
      number=52, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='validatorEditValidator', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_delegate', full_name='decimal.fee.v1.Params.validator_delegate', index=28,
      number=53, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='validatorDelegate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_delegate_nft', full_name='decimal.fee.v1.Params.validator_delegate_nft', index=29,
      number=54, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\342\336\037\024ValidatorDelegateNFT\322\264-\ncosmos.Dec', json_name='validatorDelegateNft', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_redelegate', full_name='decimal.fee.v1.Params.validator_redelegate', index=30,
      number=55, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='validatorRedelegate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_redelegate_nft', full_name='decimal.fee.v1.Params.validator_redelegate_nft', index=31,
      number=56, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\342\336\037\026ValidatorRedelegateNFT\322\264-\ncosmos.Dec', json_name='validatorRedelegateNft', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_undelegate', full_name='decimal.fee.v1.Params.validator_undelegate', index=32,
      number=57, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='validatorUndelegate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_undelegate_nft', full_name='decimal.fee.v1.Params.validator_undelegate_nft', index=33,
      number=58, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\342\336\037\026ValidatorUndelegateNFT\322\264-\ncosmos.Dec', json_name='validatorUndelegateNft', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_set_online', full_name='decimal.fee.v1.Params.validator_set_online', index=34,
      number=59, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='validatorSetOnline', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_set_offline', full_name='decimal.fee.v1.Params.validator_set_offline', index=35,
      number=60, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='validatorSetOffline', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commission_burn_factor', full_name='decimal.fee.v1.Params.commission_burn_factor', index=36,
      number=61, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='commissionBurnFactor', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evm_gas_price', full_name='decimal.fee.v1.Params.evm_gas_price', index=37,
      number=62, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec', json_name='evmGasPrice', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oracle', full_name='decimal.fee.v1.Params.oracle', index=38,
      number=63, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='oracle', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\230\240\037\001\350\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=4436,
)

DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'decimal.fee.v1.params_pb2'
  # @@protoc_insertion_point(class_scope:decimal.fee.v1.Params)
  })
_sym_db.RegisterMessage(Params)


DESCRIPTOR._options = None
_PARAMS.fields_by_name['tx_byte_fee']._options = None
_PARAMS.fields_by_name['coin_create_ticker_3']._options = None
_PARAMS.fields_by_name['coin_create_ticker_4']._options = None
_PARAMS.fields_by_name['coin_create_ticker_5']._options = None
_PARAMS.fields_by_name['coin_create_ticker_6']._options = None
_PARAMS.fields_by_name['coin_create_ticker_7']._options = None
_PARAMS.fields_by_name['coin_create']._options = None
_PARAMS.fields_by_name['coin_update']._options = None
_PARAMS.fields_by_name['coin_send']._options = None
_PARAMS.fields_by_name['coin_send_add']._options = None
_PARAMS.fields_by_name['coin_buy']._options = None
_PARAMS.fields_by_name['coin_sell']._options = None
_PARAMS.fields_by_name['coin_redeem_check']._options = None
_PARAMS.fields_by_name['coin_burn']._options = None
_PARAMS.fields_by_name['multisig_create_wallet']._options = None
_PARAMS.fields_by_name['multisig_create_transaction']._options = None
_PARAMS.fields_by_name['multisig_sign_transaction']._options = None
_PARAMS.fields_by_name['nft_mint_token']._options = None
_PARAMS.fields_by_name['nft_update_token']._options = None
_PARAMS.fields_by_name['nft_update_reserve']._options = None
_PARAMS.fields_by_name['nft_send_token']._options = None
_PARAMS.fields_by_name['nft_burn_token']._options = None
_PARAMS.fields_by_name['swap_activate_chain']._options = None
_PARAMS.fields_by_name['swap_deactivate_chain']._options = None
_PARAMS.fields_by_name['swap_initialize']._options = None
_PARAMS.fields_by_name['swap_redeem']._options = None
_PARAMS.fields_by_name['validator_create_validator']._options = None
_PARAMS.fields_by_name['validator_edit_validator']._options = None
_PARAMS.fields_by_name['validator_delegate']._options = None
_PARAMS.fields_by_name['validator_delegate_nft']._options = None
_PARAMS.fields_by_name['validator_redelegate']._options = None
_PARAMS.fields_by_name['validator_redelegate_nft']._options = None
_PARAMS.fields_by_name['validator_undelegate']._options = None
_PARAMS.fields_by_name['validator_undelegate_nft']._options = None
_PARAMS.fields_by_name['validator_set_online']._options = None
_PARAMS.fields_by_name['validator_set_offline']._options = None
_PARAMS.fields_by_name['commission_burn_factor']._options = None
_PARAMS.fields_by_name['evm_gas_price']._options = None
_PARAMS.fields_by_name['oracle']._options = None
_PARAMS._options = None
# @@protoc_insertion_point(module_scope)
