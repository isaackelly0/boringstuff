import logging
import sumList
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)
valid = {
    'spaces':sumList.sumList(['a','b','c','d','e','f','g','h'],['1','2','3','4','5','6','7','8']),
    'pieces':sumList.sumList(['w','b'],['P','R','B','N','Q','K']),
    'wK':1,
    'bK':1,
    'wP':list(range(9)),
    'bP':list(range(9)),
}
logging.debug(valid['spaces'])
logging.debug(valid['pieces'])
def isValidChessBoard(dict):
    total = 0
    check = {
        'wK': 0,
        'bK': 0,
        'wP': 0,
        'bP': 0
    }
    #for k, v loop for objects
    for k, v in dict.items():
        total += 1
        #check for invalid keys or values
        if k not in valid['spaces'] or v not in valid['pieces']:
            return False
        #set pieces local var to check for right number of pieces
        else:
            check.setdefault(v,0)
            check[v] +=1
        logging.debug(check)
    #disqualify invalid pieces
    if valid['wK'] != check['wK'] or valid['bK'] != check['bK'] or check['wP'] not in valid['wP'] or check['bP'] not in valid['bP'] or total not in list(range(1,33)):
        return False
    return True
logging.debug(isValidChessBoard({'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'}))