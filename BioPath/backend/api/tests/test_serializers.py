"""
File: test_serializers.py
Description: Unit tests for Django serializers.
Modified: 12/28 - Josh Schmitz
TODO test images
TODO test creation/modification
"""

from django.test import TestCase

from api import models, serializers


class GroupSerializerTestCase(TestCase):
    """
    All tests for the group serializer.
    """
    def setUp(self):
        self.group_attributes = {
            "id": 5,
            "name": "group1"
        }
        self.group = models.Group(**self.group_attributes)
        self.serializer = serializers.GroupSerializer(instance=self.group)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ["id", "name"])

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["id"], self.group_attributes["id"])


class UserSerializerTestCase(TestCase):
    """
    All tests for the user serializer.
    """
    def setUp(self):
        self.user_attributes = {
            "id": 5,
            "username": "us1"
        }
        self.user = models.User(**self.user_attributes)
        self.serializer = serializers.UserSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ["id", "username", "groups"])

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["id"], self.user_attributes["id"])
        self.assertEqual(data["username"], "us1")
        self.assertEqual(data["groups"], [])


class MoleculeSerializerTestCase(TestCase):
    """
    All tests for the molecule serializer.
    """

    @classmethod
    def setUpTestData(cls):
        author = models.User(username="MoleculeSerializerTestCase")
        author.save()

    def setUp(self):
        self.author = models.User.objects.get(username="MoleculeSerializerTestCase")
        self.molecule_attributes = {
            "id": 1,
            "name": "Molecule 1",
            "abbreviation": "m1",
            # "ball_and_stick_image": 
            # "space_filling_image": 
            "link": "https://www.django-rest-framework.org/api-guide/testing/",
            "author": self.author,
            "public": True
        }
        self.molecule = models.Molecule(**self.molecule_attributes)
        self.serializer = serializers.MoleculeSerializer(instance=self.molecule)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(),
            ["id", "name", "abbreviation", "ball_and_stick_image", "space_filling_image", "link", "author", "public"]
        )

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["id"], self.molecule_attributes["id"])
        self.assertEqual(data["name"], self.molecule_attributes["name"])
        self.assertEqual(data["abbreviation"], self.molecule_attributes["abbreviation"])
        self.assertEqual(data["ball_and_stick_image"], None)
        self.assertEqual(data["space_filling_image"], None)
        self.assertEqual(data["link"], self.molecule_attributes["link"])
        self.assertEqual(data["author"], self.molecule_attributes["author"].id)
        self.assertEqual(data["public"], self.molecule_attributes["public"])