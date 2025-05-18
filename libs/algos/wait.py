import time
def algoWait(secs, input=None):
    time.sleep(secs)
    return {
        "name":"等待时间",
        "value":secs
    }
