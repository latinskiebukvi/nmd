from django.http import HttpResponse
from django.template import loader
from .queries import count_device_by_model, count_device_by_storage

def index(request):
    template = loader.get_template('index.html')
    context = {
        "items": {
            "count_device_by_storage": count_device_by_storage,
            "count_device_by_model": count_device_by_model,
        }
    }
    print(count_device_by_storage)
    return HttpResponse(template.render(context, request))