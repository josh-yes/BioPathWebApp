"""
File: test_views.py
Description: Unit tests for Django views.
Modified: 12/28 - Josh Schmitz
"""

import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from api import models

NUMBER_OF_MOLECULES = 20
MOLECULE_FIELDS = {
    "id",
    "name",
    "abbreviation",
    "ball_and_stick_image",
    "space_filling_image",
    "link",
    "public",
    "author"
}
NUMBER_OF_ENZYMES = 20
ENZYME_FIELDS = {
    "id",
    "name",
    "abbreviation",
    "reversible",
    "substrates",
    "products",
    "cofactors",
    "image",
    "link",
    "author",
    "public"
}

class MoleculeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = models.User(username="MoleculeListViewTestCase")
        author.save()

        for molecule_id in range(NUMBER_OF_MOLECULES):
            models.Molecule.objects.create(
                name=f"m{molecule_id}",
                abbreviation=f"m{molecule_id}",
                author=author
            )

    def setUp(self):
        self.author = models.User.objects.get(username="MoleculeListViewTestCase")
        self.client = APIClient()
        self.client.force_authenticate(user=self.author)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/api/molecules/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('molecules-list'))
        self.assertEqual(response.status_code, 200)

    def test_lists_all_molecules(self):
        response = self.client.get(reverse('molecules-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), NUMBER_OF_MOLECULES)

    def test_correct_molecule_response(self):
        response = self.client.get(reverse('molecules-list'))
        self.assertEqual(response.status_code, 200)
        molecule_list = json.loads(response.content)
        self.assertEqual(set(molecule_list[0].keys()), MOLECULE_FIELDS)

    def test_nonpublic_accessibility(self):
        # create new user/client
        new_user = models.User.objects.create(username="NonpublicMoleculeTestUser")
        new_client = APIClient()
        new_client.force_authenticate(user=new_user)

        # users can't view other's private molecules
        response = new_client.get(reverse("molecules-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), 0)

        # users can view other's public molecules
        models.Molecule.objects.create(
            name="public molecule",
            abbreviation="pm",
            author=new_user,
            public=True
        )
        response = self.client.get(reverse("molecules-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), NUMBER_OF_MOLECULES + 1)
        self.assertIn("public molecule", [mol["name"] for mol in json.loads(response.content)])
        
class EnzymeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = models.User(username="EnzymeListViewTestCase")
        author.save()

        for enzyme_id in range(NUMBER_OF_ENZYMES):
            models.Enzyme.objects.create(
                name=f"m{enzyme_id}",
                abbreviation=f"m{enzyme_id}",
                author=author
            )

    def setUp(self):
        self.author = models.User.objects.get(username="EnzymeListViewTestCase")
        self.client = APIClient()
        self.client.force_authenticate(user=self.author)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/api/enzymes/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('enzymes-list'))
        self.assertEqual(response.status_code, 200)

    def test_lists_all_enzymes(self):
        response = self.client.get(reverse('enzymes-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), NUMBER_OF_ENZYMES)

    def test_correct_enzyme_response(self):
        response = self.client.get(reverse('enzymes-list'))
        self.assertEqual(response.status_code, 200)
        enzyme_list = json.loads(response.content)
        self.assertEqual(set(enzyme_list[0].keys()), ENZYME_FIELDS)

    def test_molecule_format_in_enzyme_view(self):
        """
        Within the enzyme list, the related molecules (substrates etc) should only
            contain the id of the molecules
        """
        # create molecules relations to enzyme
        substrate = models.Molecule.objects.create(
                name="substrate",
                abbreviation="s",
                author=self.author
        )
        product = models.Molecule.objects.create(
                name="product",
                abbreviation="p",
                author=self.author
        )
        cofactor = models.Molecule.objects.create(
                name="cofactor",
                abbreviation="c",
                author=self.author
        )

        # add molecules to a new enzyme
        enzyme = models.Enzyme.objects.create(
            name="new enzyme",
            abbreviation="ne",
            author=self.author
        )
        enzyme.substrates.add(substrate)
        enzyme.products.add(product)
        enzyme.cofactors.add(cofactor)
        
        # get enzyme list view response
        response = self.client.get(reverse("enzymes-list"))
        self.assertEqual(response.status_code, 200)
        enzymes = json.loads(response.content)

        # verify the new enzyme's related molecules are formatted correctly
        for enzyme in enzymes:
            if enzyme["name"] == "new enzyme":
                self.assertEqual(enzyme["substrates"], [substrate.id])
                self.assertEqual(enzyme["cofactors"], [cofactor.id])
                self.assertEqual(enzyme["products"], [product.id])

    def test_nonpublic_accessibility(self):
        # create new user/client
        new_user = models.User.objects.create(username="NonpublicEnzymeTestUser")
        new_client = APIClient()
        new_client.force_authenticate(user=new_user)

        # users can't view other's private enzymes
        response = new_client.get(reverse("enzymes-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), 0)

        # users can view other's public enzymes
        models.Enzyme.objects.create(
            name="public enzyme",
            abbreviation="pe",
            author=new_user,
            public=True
        )
        response = self.client.get(reverse("enzymes-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), NUMBER_OF_ENZYMES + 1)
        self.assertIn("public enzyme", [enz["name"] for enz in json.loads(response.content)])