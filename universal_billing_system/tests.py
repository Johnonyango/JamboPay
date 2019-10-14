from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt

class IndustryTestClass(TestCase):
    def setUp(self):
        self.hospitality = Industry(name = 'Hospitality')

    def test_instance(self):
        self.assertTrue(isinstance(self.hospitality,Industry))

    def test_save_method(self):
        self.hospitality.save_industry()
        industries = Industry.objects.all()
        self.assertTrue(len(industries))

# class MerchantTestClass(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='Emmanuel')
        # self.revstreams = Revstreams.objects.create_revstream(revstream = 'Food & Beverages')
        # self.industry = Industry.objects.create_industry(industry = 'Ho')
    #     self.aquamist = Merchant(Business_name = 'Aquamist', Business_owner = self.user,Email = 'john@gmail.com', Phone_number = '80745637', Physical_address ='P.O Box 10702', Post_code = '00100', Town = 'Nairobi', JP_paybill = '23451', Industry = 'Hospitality', Revstreams ='Food & Beverages', join_date = '2019-09-01' )
        

    # def test_instance(self):
    #     self.assertTrue(isinstance(self.aquamist,Merchant))


# class BillsTestCase(TestCase):
#     def setUp(self):
#         self.james= Bills(customer_name = 'James', customer_phone ='9087645', customer_email ='james@moringaschool.com', Revstreams ='Food & Beverages', narration ='deliverd on October', amount ='20000', quantity ='30', post_date ='2019-09-01',status ='unpaid')
    
#     def test_instance(self):
#         self.assertTrue(isinstance(self.james,Bills))

# class PaymentsTestCase(TestCase):
#     def setUp(self):
#         self.james= Payments(bill_number ='9087645',payers_name = 'James',  customer_email ='james@moringaschool.com', Revstreams ='Food & Beverages', narration ='deliverd on October', amount ='20000', quantity ='30', post_date ='2019-09-01',status ='unpaid')

