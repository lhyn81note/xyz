import logging
import os,sys
_top = sys.modules['__main__']

def algoSummary(args=None,input=None):
    summary = []
    for cmd in _top.curTask.theCmdManager.cmdObjs.values():
        try:
            print(f"{cmd.result}")
            if cmd.result is not None:
                summary.append(f"{cmd.result['name']},{cmd.result['value']},指令耗时:{cmd.duration}")
        except Exception as e:
            print(e)
        # write to csv file
    with open(r"runtime/report/summary.csv", "w") as f:
        f.write("\n".join(summary))

    return {
        "name":"总结",
        "value":summary
    }
