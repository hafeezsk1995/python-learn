class ErrorHandling(Exception):
    pass

inp = int(input("pls enter student marks"))
try:
    if inp>0 and inp<100:
        print("correct")
    else:
        raise ErrorHandling
except ErrorHandling:
    print("pls enter more thand 0 and less than 100")    