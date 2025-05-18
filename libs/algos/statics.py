import time
def algoStatics(args=None, input=None):
    
    if input is not None:
        ret = -1
        try:
            data = input["value"]
            ret = sum(data)
        except Exception as e:
            print(e)

    return {
        "name":"统计",
        "value":ret
    }
