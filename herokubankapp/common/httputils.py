import json
from django.http import HttpResponse


class Result:
    def __init__(self, status="failure", data=None):
        self.result = {"status": status, "data": data}

    def setStatus(self, status):
        self.result["status"] = status
        return self

    def setSuccessStatus(self):
        self.setStatus(status="success")
        return self

    def setData(self, data):
        self.result["data"] = data

    def setFailureStatus(self, reason="unknown error"):
        self.setStatus(status="success")
        self.result["reason"] = reason
        return self

    def constructResponse(self):
        return HttpResponse(json.dumps(self.result),
                            content_type="application/json")
