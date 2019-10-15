from .bill_num import unique_order_id_generator
from django.db.models.signals import pre_save
from .models import Bills




def pre_save_create_bill_id(sender, instance, *args, **kwargs):
      if not instance.bill_id:
        instance.bill_id= unique_order_id_generator(instance)

pre_save.connect(pre_save_create_bill_id, sender = Bills)

    