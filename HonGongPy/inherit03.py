class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("### Make My Error!! ###")
    def __str__(self):
        return "오류가 발생했어요"
           
raise CustomException

