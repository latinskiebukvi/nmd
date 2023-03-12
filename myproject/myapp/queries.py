from django.db.models import Count
from myapp.models import Device


same = Device.objects.filter(
    end_date=None
).select_related(
    "storage", "model"
).all()

count_device_by_model = same.values(
    "model__model_name"
).order_by(
    "model__model_name"
).annotate(
    count=Count("model__model_name")
)

count_device_by_storage = same.values(
    "storage__addres", "model__model_name"
).order_by(
    "storage__addres"
).annotate(
    count=Count("model__model_name")
)