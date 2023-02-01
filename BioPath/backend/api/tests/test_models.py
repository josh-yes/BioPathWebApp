"""
File: test_models.py
Description: Unit tests for Django models.
Modified: 12/28 - Josh Schmitz
TODO test images
"""

from django.test import TestCase
from django.core.exceptions import ValidationError

from api import models


class MoleculeTestCase(TestCase):
    """
    All tests for the molecule model. Author is 'MoleculeTestCase'.
    """

    def setUp(self):
        """
        Basic set up functionality required for all tests (function level).
        """
        self.test_author = models.User(username="MoleculeTestCase")
        self.test_author.save()
        
        self.molecule_attributes = {
            "name": "Molecule 1",
            "abbreviation": "m1",
            "ball_and_stick_image": None, # TODO test images
            "space_filling_image": None,
            "link": "hi", #"https://www.django-rest-framework.org/api-guide/testing/",
            "author": self.test_author,
            "public": True
        }
        self.m1 = models.Molecule(**self.molecule_attributes)
        self.m1.save()

    def test_retrieval(self):
        """
        Testing query-abilility using .get() on name, field access, and Molecule.__str__()
        """
        m1 = models.Molecule.objects.get(name="Molecule 1")

        self.assertEqual(m1.name, self.molecule_attributes["name"])
        self.assertEqual(m1.abbreviation, self.molecule_attributes["abbreviation"])
        self.assertEqual(m1.link, self.molecule_attributes["link"])
        self.assertEqual(m1.author, self.molecule_attributes["author"])
        self.assertEqual(m1.public, self.molecule_attributes["public"])
        self.assertEqual(m1.__str__(), self.molecule_attributes["name"])

    def test_validators_blank(self):
        m1 = models.Molecule()
        expected_errors = {
            'name': ['This field cannot be blank.'],
            'abbreviation': ['This field cannot be blank.'],
            'author': ['This field cannot be null.']
        }
        try:
            m1.full_clean()
        except ValidationError as e:
            self.assertDictEqual(expected_errors, e.message_dict)

    def test_validators_empty(self):
        m1 = models.Molecule(
            name="",
            abbreviation="",
            author=self.test_author
        )
        expected_errors = {
            'name': ['This field cannot be blank.'],
            'abbreviation': ['This field cannot be blank.']
        }
        try:
            m1.full_clean()
        except ValidationError as e:
            self.assertDictEqual(expected_errors, e.message_dict)

    def test_validators_max_length(self):
        m1 = models.Molecule(
            name="012345678901234567890123456789012345678901234567890",
            abbreviation="01234567890",
            author=self.test_author
        )
        expected_errors = {
            'name': ['Ensure this value has at most 50 characters (it has 51).'],
            'abbreviation': ['Ensure this value has at most 10 characters (it has 11).']
        }
        try:
            m1.full_clean()
        except ValidationError as e:
            self.assertDictEqual(expected_errors, e.message_dict)


class EnzymeTestCase(TestCase):
    """
    All tests for the Enzyme model. Author is 'EnzymeTestCase'.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up functionality: ran once per TestClass (class level).
        """
        test_author = models.User(username="EnzymeTestCase")
        test_author.save()

        m1 = models.Molecule(
            name="Molecule 1",
            abbreviation="m1",
            # ball_and_stick_image="", # TODO test images
            # space_filling_image="",
            link="https://www.django-rest-framework.org/api-guide/testing/",
            author=test_author,
            public=True
        )
        m1.save()

        m2 = models.Molecule(
            name="Molecule 2",
            abbreviation="m2",
            # ball_and_stick_image="", # TODO test images
            # space_filling_image="",
            link="https://www.django-rest-framework.org/api-guide/testing/",
            author=test_author,
            public=True
        )
        m2.save()

        m3 = models.Molecule(
            name="Molecule 3",
            abbreviation="m3",
            # ball_and_stick_image="", # TODO test images
            # space_filling_image="",
            link="https://www.django-rest-framework.org/api-guide/testing/",
            author=test_author,
            public=True
        )
        m3.save()

    def setUp(self):
        """
        Basic set up functionality required for all tests (function level).
        """
        test_author = models.User.objects.get(username="EnzymeTestCase")
        m1 = models.Molecule.objects.get(name="Molecule 1")
        m2 = models.Molecule.objects.get(name="Molecule 2")
        m3 = models.Molecule.objects.get(name="Molecule 3")

        e1 = models.Enzyme(
            name="Enzyme 1",
            abbreviation="e1",
            reversible=True,
            # image= #TODO
            link="https://www.django-rest-framework.org/api-guide/testing/",
            author=test_author,
            public=True
        )
        e1.save()
        e1.substrates.add(m1)
        e1.products.add(m2)
        e1.cofactors.add(m3)

    def test_basic_retrieval(self):
        """
        Testing query-abilility using .get() on name, field access, and Enzyme.__str__()
        """
        test_author = models.User.objects.get(username="EnzymeTestCase")
        e1 = models.Enzyme.objects.get(name="Enzyme 1")

        self.assertEqual(e1.name, "Enzyme 1")
        self.assertEqual(e1.abbreviation, "e1")
        self.assertEqual(e1.link, "https://www.django-rest-framework.org/api-guide/testing/")
        self.assertEqual(e1.author, test_author)
        self.assertEqual(e1.public, True)
        self.assertEqual(e1.__str__(), "Enzyme 1")

    def test_related_retrieval(self):
        """
        Testing retrieval of related fields
        """
        test_author = models.User.objects.get(username="EnzymeTestCase")
        e1 = models.Enzyme.objects.get(name="Enzyme 1")
        m1 = models.Molecule.objects.get(name="Molecule 1")
        m2 = models.Molecule.objects.get(name="Molecule 2")
        m3 = models.Molecule.objects.get(name="Molecule 3")

        self.assertEqual(e1.substrates.all()[0], m1)
        self.assertEqual(e1.products.all()[0], m2)
        self.assertEqual(e1.cofactors.all()[0], m3)


class PathwayTestCase(TestCase):
    """
    All tests for the Pathway model. Author is 'PathwayTestCase'.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up functionality: ran once per TestClass (class level).
        """
        test_author = models.User(username="PathwayTestCase")
        test_author.save()

        m1 = models.Molecule(
            name="Molecule 1",
            abbreviation="m1",
            # ball_and_stick_image="", # TODO test images
            # space_filling_image="",
            link="https://www.django-rest-framework.org/api-guide/testing/",
            author=test_author,
            public=True
        )
        m1.save()

        m2 = models.Molecule(
            name="Molecule 2",
            abbreviation="m2",
            # ball_and_stick_image="", # TODO test images
            # space_filling_image="",
            link="https://www.django-rest-framework.org/api-guide/testing/",
            author=test_author,
            public=True
        )
        m2.save()

        m3 = models.Molecule(
            name="Molecule 3",
            abbreviation="m3",
            # ball_and_stick_image="", # TODO test images
            # space_filling_image="",
            link="https://www.django-rest-framework.org/api-guide/testing/",
            author=test_author,
            public=True
        )
        m3.save()

        e1 = models.Enzyme(
            name="Enzyme 1",
            abbreviation="e1",
            reversible=True,
            # image= #TODO
            link="https://www.django-rest-framework.org/api-guide/testing/",
            author=test_author,
            public=True
        )
        e1.save()
        e1.substrates.add(m1)
        e1.products.add(m2)

        e2 = models.Enzyme(
            name="Enzyme 2",
            abbreviation="e2",
            reversible=True,
            # image= #TODO
            link="https://www.django-rest-framework.org/api-guide/testing/",
            author=test_author,
            public=True
        )
        e2.save()
        e2.substrates.add(m2)
        e2.products.add(m3)

    def setUp(self):
        """
        Basic set up functionality required for all tests (function level).
        """
        self.test_author = models.User.objects.get(username="PathwayTestCase")
        self.m1 = models.Molecule.objects.get(name="Molecule 1")
        self.m2 = models.Molecule.objects.get(name="Molecule 2")
        self.e1 = models.Enzyme.objects.get(name="Enzyme 1")

        self.p1 = models.Pathway(
            name="Pathway 1",
            author=self.test_author,
            link="https://www.django-rest-framework.org/api-guide/testing/",
            public=True
        )
        self.p1.save()

        self.pe1 = models.PathwayEnzyme(
            pathway=self.p1,
            enzyme=self.e1,
            x=0,
            y=0
        )
        self.pe1.save()

        self.pm1 = models.PathwayMolecule(
            molecule=self.m1,
            pathway=self.p1,
            x=0,
            y=0
        )
        self.pm1.save()

        self.pm2 = models.PathwayMolecule(
            molecule=self.m2,
            pathway=self.p1,
            x=0,
            y=0
        )
        self.pm2.save()

    def test_basic_retrieval(self):
        """
        Testing query-abilility using .get() on name, field access, and Enzyme.__str__()
        """
        p1 = models.Pathway.objects.get(name="Pathway 1")

        self.assertEqual(p1.name, "Pathway 1")
        self.assertEqual(p1.author, self.test_author)

    def test_related_retrieval(self):
        """
        Testing retrieval of related fields
        """
        e1 = models.Enzyme.objects.get(name="Enzyme 1")
        m1 = models.Molecule.objects.get(name="Molecule 1")
        m2 = models.Molecule.objects.get(name="Molecule 2")
        p1 = models.Pathway.objects.get(name="Pathway 1")

        self.assertEqual(p1.enzymes.all()[0], e1)
        self.assertEqual(p1.molecules.all()[0], m1)
        self.assertEqual(p1.molecules.all()[1], m2)
        self.assertEqual(p1.enzymes.all()[0].substrates.all()[0], m1)

    def test_validators_blank(self):
        e = models.Enzyme()
        expected_errors = {
            'name': ['This field cannot be blank.'],
            'abbreviation': ['This field cannot be blank.'],
            'author': ['This field cannot be null.']
        }
        try:
            e.full_clean()
            self.fail()
        except ValidationError as error:
            self.assertDictEqual(expected_errors, error.message_dict)

    def test_validators_empty(self):
        e = models.Enzyme(
            name="",
            abbreviation="",
            author=self.test_author
        )
        expected_errors = {
            'name': ['This field cannot be blank.'],
            'abbreviation': ['This field cannot be blank.']
        }
        try:
            e.full_clean()
            self.fail()
        except ValidationError as error:
            self.assertDictEqual(expected_errors, error.message_dict)

    def test_validators_max_length(self):
        e = models.Enzyme(
            name="012345678901234567890123456789012345678901234567890",
            abbreviation="01234567890",
            author=self.test_author
        )
        expected_errors = {
            'name': ['Ensure this value has at most 50 characters (it has 51).'],
            'abbreviation': ['Ensure this value has at most 10 characters (it has 11).']
        }
        try:
            e.full_clean()
            self.fail()
        except ValidationError as error:
            self.assertDictEqual(expected_errors, error.message_dict)