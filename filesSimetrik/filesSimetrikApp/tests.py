from django.test import TestCase,Client
from django.urls import resolve,reverse
from .views import filter, reorder,createConnection 
import pandas as pd
from io import StringIO
import json
from  django.core.paginator import Paginator
# Create your tests here.
class TestViews(TestCase):
    def test_getFile(self):
        client = Client()
        response =client.get(reverse('getFile'))
        self.assertEquals(response.status_code,200)

    def test_filter(self):
        client =Client()
        response = client.get(reverse('filter'))
        self.assertEquals(response.status_code,200)


    def test_reorder(self):
        client = Client()
        response = client.get(reverse('reorder'))
        self.assertEquals(response.status_code,200)


