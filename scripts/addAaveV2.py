import click
from ape.cli import network_option, NetworkBoundCommand
from ape import accounts, project



CAIRO_VERIFIER = "0xAB43bA48c9edF4C2C4bB01237348D1D7B28ef168"
CAIRO_PROGRAM_HASH = "0x18261fedf8bb9295db94450fdda4343f1b04d3ae08f198d079a0e178596f494"

#
## AAVE 
#

## Goerli, with WETH ASSET
AAVE_WETH = "0xCCa7d1416518D095E729904aAeA087dBA749A4dC"
AAVE_PROTOCOL_DATA_PROVIDER = "0x927F584d4321C1dCcBf5e2902368124b02419a1E"
AAVE_RESERVE_INTEREST_RATE_STRATEGY= "0x5ecE040038c822d7228F24D9F2e1Fd41bc77A3c4"
AAVE_CONTRACT_ADDRESS_0 = AAVE_PROTOCOL_DATA_PROVIDER
AAVE_CHECKDATA_0 = "0x3e150141000000000000000000000000CCa7d1416518D095E729904aAeA087dBA749A4dC"
AAVE_STRATEGYY_OFFSET_0 = 128
AAVE_CONTRACT_ADDRESS_1 = AAVE_PROTOCOL_DATA_PROVIDER
AAVE_CHECKDATA_1 = "0x35ea6a75000000000000000000000000CCa7d1416518D095E729904aAeA087dBA749A4dC"
AAVE_STRATEGYY_OFFSET_1 = 0 
AAVE_CONTRACT_ADDRESS_2 = AAVE_PROTOCOL_DATA_PROVIDER
AAVE_CHECKDATA_2 = "0x35ea6a75000000000000000000000000CCa7d1416518D095E729904aAeA087dBA749A4dC"
AAVE_STRATEGYY_OFFSET_2 = 32
AAVE_CONTRACT_ADDRESS_3 = AAVE_PROTOCOL_DATA_PROVIDER
AAVE_CHECKDATA_3 = "0x35ea6a75000000000000000000000000CCa7d1416518D095E729904aAeA087dBA749A4dC"
AAVE_STRATEGYY_OFFSET_3 = 64
AAVE_CONTRACT_ADDRESS_4 = AAVE_RESERVE_INTEREST_RATE_STRATEGY
AAVE_CHECKDATA_4 = "0xa15f30ac"
AAVE_STRATEGYY_OFFSET_4 = 0
AAVE_CONTRACT_ADDRESS_5 = AAVE_RESERVE_INTEREST_RATE_STRATEGY
AAVE_CHECKDATA_5 = "0x0bdf953f"
AAVE_STRATEGYY_OFFSET_5 = 0
AAVE_CONTRACT_ADDRESS_6 = AAVE_RESERVE_INTEREST_RATE_STRATEGY
AAVE_CHECKDATA_6 = "0xccab01a3"
AAVE_STRATEGYY_OFFSET_6 = 0
AAVE_CONTRACT_ADDRESS_7 = AAVE_RESERVE_INTEREST_RATE_STRATEGY
AAVE_CHECKDATA_7 = "0x7b832f58"
AAVE_STRATEGYY_OFFSET_7 = 0
AAVE_CONTRACT_ADDRESS_8 = AAVE_RESERVE_INTEREST_RATE_STRATEGY
AAVE_CHECKDATA_8 = "0x65614f81"
AAVE_STRATEGYY_OFFSET_8 = 0
AAVE_CONTRACT_ADDRESS_9 = AAVE_RESERVE_INTEREST_RATE_STRATEGY
AAVE_CHECKDATA_9 = "0xb2589544"
AAVE_STRATEGYY_OFFSET_9 = 0
AAVE_STRATEGY_ADDRESS= "0x76aFA2b6C29E1B277A3BB1CD320b2756c1674c91" 
AAVE_MAX_STRATEGY_DEBT_RATIO = 10000
AAVE_STRATEGY_CONTRACTS = [AAVE_CONTRACT_ADDRESS_0, AAVE_CONTRACT_ADDRESS_1, AAVE_CONTRACT_ADDRESS_2, AAVE_CONTRACT_ADDRESS_3, AAVE_CONTRACT_ADDRESS_4, AAVE_CONTRACT_ADDRESS_5, AAVE_CONTRACT_ADDRESS_6, AAVE_CONTRACT_ADDRESS_7, AAVE_CONTRACT_ADDRESS_8, AAVE_CONTRACT_ADDRESS_9]
AAVE_STRATEGYY_CHECKDATA = [AAVE_CHECKDATA_0, AAVE_CHECKDATA_1, AAVE_CHECKDATA_2, AAVE_CHECKDATA_3, AAVE_CHECKDATA_4, AAVE_CHECKDATA_5, AAVE_CHECKDATA_6, AAVE_CHECKDATA_7, AAVE_CHECKDATA_8, AAVE_CHECKDATA_9]
AAVE_STRATEGYY_OFFSET = [AAVE_STRATEGYY_OFFSET_0, AAVE_STRATEGYY_OFFSET_1, AAVE_STRATEGYY_OFFSET_2, AAVE_STRATEGYY_OFFSET_3, AAVE_STRATEGYY_OFFSET_4, AAVE_STRATEGYY_OFFSET_5, AAVE_STRATEGYY_OFFSET_6, AAVE_STRATEGYY_OFFSET_7, AAVE_STRATEGYY_OFFSET_8, AAVE_STRATEGYY_OFFSET_9]
AAVE_STRATEGYY_CALCULATION = [1, 2, 0, 10000, 3, 0, 2, 3, 0, 10002, 1000000000000000000000020000, 2,10003, 10001, 3, 10004, 4, 1, 1000000000000000000000020000, 4, 1, 10005, 1000000000000000000000020000, 2, 10007, 10006, 3, 10008, 6, 2, 10009, 1000000000000000000000020000, 3,
                10010, 5, 0, 10011, 9, 0, 2, 1000000000000000000000020000, 2, 10013, 10002, 3, 10011, 10014, 2, 10015, 1000000000000000000000020000, 3, 10008, 8, 2, 10017, 1000000000000000000000020000, 3, 10018, 7, 0, 10019, 9, 0,
                3, 1000000000000000000000020000, 2, 10021, 10002, 3, 10020, 10022, 2, 10023, 1000000000000000000000020000, 3, 10016, 10024, 0, 30000, 0, 1, 10025, 10026, 2, 10027, 30000, 3, 10028, 10004, 2, 10029, 1000000000000000000000020000, 3, 1, 2, 0, 10000, 3, 
                0, 2, 3, 0, 10002, 1000000000000000000000020000, 2, 10003, 10001, 3, 10004, 1000000000000000000000020000, 2, 10005, 4, 3, 10006, 5, 2, 10007, 1000000000000000000000020000, 3, 10008, 9, 0, 2, 1000000000000000000000020000, 2,
                     10010, 10002, 3, 10011, 10009, 2, 10012, 1000000000000000000000020000, 3, 10006, 7, 2, 10014, 1000000000000000000000020000, 3, 10015, 9, 0, 3, 1000000000000000000000020000, 2, 10017, 10002, 3, 10016, 10018, 2, 10019, 1000000000000000000000020000, 3,
                     10013, 10020, 0, 30000, 0, 1, 10021, 10022, 2, 10023, 30000, 3, 10024, 10004, 2, 10025, 1000000000000000000000020000, 3]
AAVE_CALCULATION_CONDITION = [1, 2, 0, 10000, 3, 0, 2, 3, 0, 10002, 1000000000000000000000020000, 2, 10003, 10001, 3, 10004, 4, 31, 27]

def main():
    account = accounts.load("sach")
    contract = project.DebtAllocator.at("0xDcAA40F17cEce7c7aB9c37E6e54754aA6985DEe1")
    contract.addStrategy(AAVE_STRATEGY_ADDRESS, AAVE_MAX_STRATEGY_DEBT_RATIO, AAVE_STRATEGY_CONTRACTS, AAVE_STRATEGYY_CHECKDATA, AAVE_STRATEGYY_OFFSET, AAVE_STRATEGYY_CALCULATION, AAVE_CALCULATION_CONDITION,sender=account)
