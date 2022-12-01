export WEB3_INFURA_PROJECT_ID=eebdf8732cd044f0a52f976af7781260      
ape run deploy --network ethereum:goerli:infura 
ape run addCompV2 --network ethereum:goerli:infura 
ape run addAaveV2 --network ethereum:goerli:infura 
ape run saveSnapshot --network ethereum:goerli:infura 

[<NewSnapshot 
dataStrategies=(
        (947419739009127, 62655567454945, 10000002244417, 75000000000000000, 800000000000000000, 14139, 246601, 0, 2102400, 0, 99980000, 8, 100000000, 8, 6), 
        (1000, 11101567370227779740367, 1559424876440476114637, 413631211759288292676, 650000000000000000000000000, 100000000000000000000000000, 1000000000000000000000000000, 80000000000000000000000000, 1000000000000000000000000000, 0)
    ) 
calculation=(
        (0, 1, 0, 10000, 2, 1, 1, 1000000000000020000, 2, 10002, 10001, 3, 4, 5, 2, 10004, 1000000000000020000, 3, 10005, 7, 0, 10003, 4, 1, 10007, 6, 2, 10008, 1000000000000020000, 3, 10009, 10006, 0, 1000000000000020000, 3, 1, 10010, 10011, 2, 10012, 1000000000000020000, 3, 10013, 10003, 2, 10014, 1000000000000020000, 3, 10015, 8, 2, 9, 8, 2, 20010, 14, 4, 10017, 10018, 2, 10019, 10001, 3, 10020, 10, 2, 20010, 11, 4, 10021, 10022, 3, 20010, 13, 4, 10023, 10024, 2, 10025, 12, 3, 10026, 10016, 0, 10027, 1000020000, 2, 0, 1, 0, 10000, 2, 1, 1, 1000000000000020000, 2, 10002, 10001, 3, 10003, 5, 2, 10004, 1000000000000020000, 3, 10005, 7, 0, 1000000000000020000, 3, 1, 10007, 10006, 2, 10008, 1000000000000020000, 3, 10009, 10003, 2, 10010, 1000000000000020000, 3, 10011, 8, 2, 9, 8, 2, 20010, 14, 4, 10013, 10014, 2, 10015, 10001, 3, 10016, 10, 2, 20010, 11, 4, 10017, 10018, 3, 20010, 13, 4, 10019, 20020, 2, 10021, 12, 3, 10022, 10012, 0, 10023, 1000020000, 2), 
        (1, 2, 0, 10000, 3, 0, 2, 3, 0, 10002, 1000000000000000000000020000, 2, 10003, 10001, 3, 10004, 4, 1, 1000000000000000000000020000, 4, 1, 10005, 1000000000000000000000020000, 2, 10007, 10006, 3, 10008, 6, 2, 10009, 1000000000000000000000020000, 3, 10010, 5, 0, 10011, 9, 0, 2, 1000000000000000000000020000, 2, 10013, 10002, 3, 10011, 10014, 2, 10015, 1000000000000000000000020000, 3, 10008, 8, 2, 10017, 1000000000000000000000020000, 3, 10018, 7, 0, 10019, 9, 0, 3, 1000000000000000000000020000, 2, 10021, 10002, 3, 10020, 10022, 2, 10023, 1000000000000000000000020000, 3, 10016, 10024, 0, 30000, 0, 1, 10025, 10026, 2, 10027, 30000, 3, 10028, 10004, 2, 10029, 1000000000000000000000020000, 3, 1, 2, 0, 10000, 3, 0, 2, 3, 0, 10002, 1000000000000000000000020000, 2, 10003, 10001, 3, 10004, 1000000000000000000000020000, 2, 10005, 4, 3, 10006, 5, 2, 10007, 1000000000000000000000020000, 3, 10008, 9, 0, 2, 1000000000000000000000020000, 2, 10010, 10002, 3, 10011, 10009, 2, 10012, 1000000000000000000000020000, 3, 10006, 7, 2, 10014, 1000000000000000000000020000, 3, 10015, 9, 0, 3, 1000000000000000000000020000, 2, 10017, 10002, 3, 10016, 10018, 2, 10019, 1000000000000000000000020000, 3, 10013, 10020, 0, 30000, 0, 1, 10021, 10022, 2, 10023, 30000, 3, 10024, 10004, 2, 10025, 1000000000000000000000020000, 3)
    ) 
condition=(
        (0, 1, 0, 10000, 2, 1, 1, 1000000000000020000, 2, 10002, 10001, 3, 10003, 4, 29, 25), 
        (1, 2, 0, 10000, 3, 0, 2, 3, 0, 10002, 1000000000000000000000020000, 2, 10003, 10001, 3, 10004, 4, 31, 27)
    ) 
inputHash=23778023730812411845676991316614654607903875471757921773405581978580488471015 timestamp=1669916364>]

Program output:
  69877331423220707281243982024735471462
  198902898170385006158168479911819002343
  2
  0
  0
  2
  5000
  5000
  0
  1510489860937415003303867

  
ape run verifySolution --network ethereum:goerli:infura 