from django.http import HttpResponse

from .models import BankBranches

# Create your views here.
def bankdetails(request, ifsc):
    details = BankBranches.objects.filter(ifsc=ifsc.upper())
    print(details)
    for det in details:
        print(det)
    return HttpResponse("success 200 ok")
