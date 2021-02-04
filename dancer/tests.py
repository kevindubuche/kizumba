from django.test import TestCase, Client
from .models import Dancer
# Create your tests here.

class ModelsTestCase(TestCase):
    def setUp(self):
        #Create dancers
        d1 = Dancer.objects.create(first_name="FA", last_name="LA", age=20, address="AA", latitude=123, longitude=234)
        d2 = Dancer.objects.create(first_name="FB", last_name="LB", age=-24, address="AB", latitude=322, longitude=999)

    def test_dancers_count(self):
        d =  Dancer.objects.filter(first_name='FA').count()
        self.assertEqual(d, 1)

    def test_valid_dancer(self):
        d = Dancer.objects.get(first_name="FA")
        self.assertTrue(d.is_a_valid_dancer())
        
    def test_invalid_dancer(self):
        d = Dancer.objects.get(first_name="FB")
        self.assertFalse(d.is_a_valid_dancer())

    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["dancers"].count(), 2)