from django.http import HttpResponse

from .models import Bank_Branches

# Create your views here.
def bankdetails(request, ifsc):
    details = Bank_Branches.objects.filter(ifsc=ifsc.upper())
    print(details)
    for det in details:
        print(det)
    return HttpResponse("success 200 ok")
