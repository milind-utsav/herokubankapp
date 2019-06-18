import json
from django.core import serializers

from .models import BankBranches
import herokubankapp.common.utils as utils
import herokubankapp.common.httputils as httputils


# Create your views here.
def bankdetails(request):
    result = httputils.Result()
    if "ifsc" in request.GET:
        ifsc = request.GET.get("ifsc", "").strip()
        # ifsc should be 11 characters long
        if utils.isIfscValid(ifsc):
            # get bank details against ifsc from model
            details = BankBranches.objects.filter(ifsc=ifsc.upper())
            if details.count() > 0:
                # if found, serialize to json and return fields
                serialized_json = serializers.serialize("json", details)
                bank = json.loads(serialized_json)[0]
                if "fields" in bank:
                    result.setSuccessStatus().setData(bank["fields"])
                else:
                    result.setSuccessStatus().setData(bank)
            else:
                result.setFailureStatus(reason="bank details not found")
        else:
            result.setFailureStatus(reason="invalid ifsc code")
    elif "name" in request.GET and "city" in request.GET:
        name = request.GET.get("name", "").strip()
        city = request.GET.get("city", "").strip()
        if len(name) <= 0:
            result.setFailureStatus(reason="bank name empty")
        elif len(city) <= 0:
            result.setFailureStatus(reason="city empty")
        else:
            # find banks in the city with given name
            banks = BankBranches.objects.filter(city=city.upper(),
                                                bank_name=name.upper())
            bank_list = []
            # convert banks to json and return data
            for bank in banks:
                bank_list.append({"ifsc": bank.ifsc,
                                  "branch": bank.branch,
                                  "address": bank.address,
                                  "city": bank.city,
                                  "state": bank.state,
                                  "name": bank.bank_name})
            if len(bank_list) > 0:
                result.setSuccessStatus().setData(bank_list)
            else:
                result.setFailureStatus(reason="no matching banks found")
    else:
        result.setFailureStatus(reason="insufficient parameters. pass either ifsc or bank name and city")
    return result.constructResponse()
