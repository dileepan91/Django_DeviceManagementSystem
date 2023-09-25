from django.http import HttpResponse
from django.template import loader


from .models import Audit


def index(request):
    return HttpResponse("Hello, Have a nice day.")


def view_all(request):
    all_audit_info = Audit.objects.order_by("student_id")
    template = loader.get_template("viewAll.html")
    context = {
        "all_audit_info": all_audit_info,
    }
    return HttpResponse(template.render(context, request))
