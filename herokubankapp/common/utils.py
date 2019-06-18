import herokubankapp.common.consts as consts


def isIfscValid(ifsc):
    val = True
    if len(ifsc) != consts.IFSC_CODE_LEN:
        val = False
    return val
