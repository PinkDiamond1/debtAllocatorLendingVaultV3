from ape import accounts, project
import json
import os
from dotenv import load_dotenv

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
AAVE_STRATEGYY_CALCULATION = [1, 0, 5, 10000, 2, 0, 10001, 3, 0, 2, 3, 0, 10003, 1000000000000000000000020000, 2,10004, 10002, 3, 10005, 4, 1, 1000000000000000000000020000, 4, 1, 10006, 1000000000000000000000020000, 2, 10008, 10007, 3, 10009, 6, 2, 10010, 1000000000000000000000020000, 3,
10011, 5, 0, 10012, 9, 0, 2, 1000000000000000000000020000, 2, 10014, 10003, 3, 10012, 10015, 2, 10016, 1000000000000000000000020000, 3, 10009, 8, 2, 10018, 1000000000000000000000020000, 3, 10019, 7, 0, 10020, 9, 0,
3, 1000000000000000000000020000, 2, 10022, 10003, 3, 10021, 10023, 2, 10024, 1000000000000000000000020000, 3, 10017, 10025, 0, 30000, 0, 1, 10026, 10027, 2, 10028, 30000, 3, 10029, 10005, 2, 10030, 1000000000000000000000020000, 3, 
1, 0, 5, 10000, 2, 0, 10001, 3, 0, 2, 3, 0, 10003, 1000000000000000000000020000, 2, 10004, 10002, 3, 10005, 1000000000000000000000020000, 2, 10006, 4, 3, 10007, 5, 2, 10008, 1000000000000000000000020000, 3, 10009, 9, 0, 2, 1000000000000000000000020000, 2,
10011, 10003, 3, 10012, 10010, 2, 10013, 1000000000000000000000020000, 3, 10007, 7, 2, 10015, 1000000000000000000000020000, 3, 10016, 9, 0, 3, 1000000000000000000000020000, 2, 10018, 10003, 3, 10017, 10019, 2, 10020, 1000000000000000000000020000, 3,
10014, 10021, 0, 30000, 0, 1, 10022, 10023, 2, 10024, 30000, 3, 10025, 10005, 2, 10026, 1000000000000000000000020000, 3]
AAVE_CALCULATION_CONDITION = [1, 0, 5, 10000, 2, 0, 10001, 3, 0, 2, 3, 0, 10003, 1000000000000000000000020000, 2, 10004, 10002, 3, 10005, 4, 32, 28]

def main():
    load_dotenv()
    f = open("./scripts/config_testnet.json")
    config_dict = json.load(f)
    f.close()
    f = open("./scripts/strategies_info.json")
    strategies_info = json.load(f)
    f.close()
    account = accounts.load(os.environ["ACCOUNT_ALIAS"])
    contract = project.DebtAllocator.at(config_dict["debt_allocator_address"])
    aave_strategy = config_dict["strategy_aave_address"]
    addresses = strategies_info["addresses"]
    callLen = strategies_info["callLen"]
    contracts = strategies_info["contracts"]
    checkdata = strategies_info["checkdata"]
    offset = strategies_info["offset"]
    calculationsLen = strategies_info["calculationsLen"]
    calculations = strategies_info["calculations"]
    conditionsLen = strategies_info["conditionsLen"]
    conditions = strategies_info["conditions"]

    tx = contract.addStrategy((addresses, callLen, contracts, checkdata, offset, calculationsLen, calculations, conditionsLen, conditions), aave_strategy, (int(len(AAVE_STRATEGY_CONTRACTS)), AAVE_STRATEGY_CONTRACTS, AAVE_STRATEGYY_CHECKDATA, AAVE_STRATEGYY_OFFSET, int(len(AAVE_STRATEGYY_CALCULATION)), AAVE_STRATEGYY_CALCULATION, int(len(AAVE_CALCULATION_CONDITION)), AAVE_CALCULATION_CONDITION),sender=account, max_priority_fee="1 gwei")
    logs = list(tx.decode_logs(contract.StrategyAdded))
    addresses = logs[0].Strategies
    callLen = logs[0].StrategiesCallLen
    contracts = logs[0].Contracts

    for i in AAVE_STRATEGYY_CHECKDATA:
        checkdata.append(i[2:])
    
    offset = logs[0].Offset
    calculationsLen = logs[0].CalculationsLen
    calculations = logs[0].Calculations
    ConditionsLen = logs[0].ConditionsLen
    conditions = logs[0].Conditions
    result = {}
    result["addresses"] = addresses
    result["callLen"] = callLen
    result["contracts"] = contracts
    result["checkdata"] = checkdata
    result["offset"] = offset
    result["calculationsLen"] = calculationsLen
    result["calculations"] = calculations
    result["conditionsLen"] = ConditionsLen
    result["conditions"] = conditions
    f = open("./scripts/strategies_info.json", "w")
    json.dump(result, f)
    f.close()
    print("new strategies: ")
    print(result)

    
 
