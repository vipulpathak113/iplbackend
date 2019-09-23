from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from .models import PointsTable
from django.test import TestCase


class ModelTestCase(TestCase):
    def setUp(self):
        self_team = "Write Team name"
        self.teams = PointsTable(name=self_team)

        def test_model_can_create_team(self):
            old_count = PointsTable.objects.count()
            self.bucketlist.save()
            new_count = PointsTable.objects.count()
            self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.teamlist_data = {'team_name': 'Mumbai Indians'}
        self.response = self.client.post(
            reverse('create'),
            self.teamlist_data,
            format="json"
        )

    def test_api_can_create_teamlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
