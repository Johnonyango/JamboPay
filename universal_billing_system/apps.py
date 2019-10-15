from django.apps import AppConfig


class UniversalBillingSystemConfig(AppConfig):
    name = 'universal_billing_system'
    def ready(self):
        print ('signal inawork')
        import universal_billing_system.signals








    9
