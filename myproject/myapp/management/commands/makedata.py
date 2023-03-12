import json
import os
from random import randint

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from myapp.models import Customer, Storage, Developer, Model, Country, Device


def setter(obj, values):
    for key, val in values.items():
        setattr(obj, key, val)
    return obj


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        with open(os.path.join(os.getcwd(), "data.json"), "r", encoding="utf-8-sig") as js:
            content = json.load(js)
        
        customers = content["customers"]
        storages = content["storages"]
        developers = content["developers"]
        models = content["models"]
        countries = content["countries"]

        for c, s in zip(customers, storages):
            customer = Customer()
            customer = setter(customer, c)
            customer.start_date = timezone.now()
            customer.end_date = None
            customer.save()

            stor = Storage()
            stor = setter(stor, s)
            stor.customer = customer
            stor.save()

        for dev in developers:
            developer = Developer()
            developer = setter(developer, dev)
            developer.save()

        for key, vals in models.items():
            dev = Developer.objects.get(dev_name=key)
            for val in vals:
                mod = Model()
                mod = setter(mod, val)
                mod.developer = dev
                mod.save()

        for c in countries:
            country = Country()
            country = setter(country, c)
            country.save()

        for _ in range(randint(50, 100)):
            device = Device()
            device.storage = Storage.objects.get(id=randint(1, len(storages)))
            device.model = Model.objects.get(id=randint(1, len(models)))
            device.country = Country.objects.get(id=randint(1, len(countries)))
            device.start_date = timezone.now()
            device.end_date = None
            device.save()