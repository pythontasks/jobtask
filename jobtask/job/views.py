# Create your views here.
from django.views.decorators.http import require_http_methods
import json
from django.http import HttpResponse
import urllib2
import urllib
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(["POST"])
@csrf_exempt
def job(request):
    contactInfo = {"email":"art.cudejko@hotmail.co.uk", "twitter":"none", "github":"https://github.com/jobtask1/jobtask", "skype":"arturmisio", "gitrepo":""}
    return HttpResponse(json.dumps(contactInfo), content_type="application/json")

def jobtest(request):
    return HttpResponse(urllib2.urlopen("http://127.0.0.1:8000/job", data=urllib.urlencode({})).read())
