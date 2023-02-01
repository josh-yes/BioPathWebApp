"""
File: models.py
Description: Defines the models for enzymes, substrates, connections, etc. Django uses
    these models to construct the database tables. They are used by serializers.py which
    serializes the data into json for easy view building.
Modified: 11/17 - Josh Schmitz
TODO default images https://stackoverflow.com/questions/15322391/django-the-image-attribute-has-no-file-associated-with-it
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group
from django.core.validators import MinLengthValidator


class Molecule(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        validators=[MinLengthValidator(1)]
    )
    abbreviation = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=[MinLengthValidator(1)]
    )
    ball_and_stick_image = models.ImageField(
        null=True,
        blank=True
    )
    space_filling_image = models.ImageField(
        null=True,
        blank=True
    )
    link = models.URLField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Enzyme(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        validators=[MinLengthValidator(1)]
    )
    abbreviation = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=[MinLengthValidator(1)]
    )
    reversible = models.BooleanField(
        default=True,
        null=False,
        blank=False
    )
    substrates = models.ManyToManyField(
        Molecule,
        related_name="enzymes_substrates"
    )
    products = models.ManyToManyField(
        Molecule,
        related_name="enzymes_products"
    )
    cofactors = models.ManyToManyField(
        Molecule,
        related_name="enzymes_cofactors"
    )
    image = models.ImageField(null=True, blank=True) # space filling
    link = models.URLField(null=True, blank=True) # link to protopedia
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    
class Pathway(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        validators=[MinLengthValidator(1)]
    )
    enzymes = models.ManyToManyField(
        Enzyme,
        through='PathwayEnzyme',
        related_name="pathways_enzyme"
    )
    molecules = models.ManyToManyField(
        Molecule,
        through='PathwayMolecule',
        related_name="pathways_molecule"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(null=True, blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PathwayEnzyme(models.Model):
    enzyme = models.ForeignKey(Enzyme, on_delete=models.PROTECT)
    pathway = models.ForeignKey(Pathway, on_delete=models.CASCADE)
    x = models.PositiveSmallIntegerField(null=False, blank=False)
    y = models.PositiveSmallIntegerField(null=False, blank=False)
    limiting = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pathway.__str__()} - {self.enzyme.__str__()}"

  
class PathwayMolecule(models.Model):
    molecule = models.ForeignKey(Molecule, on_delete=models.PROTECT)
    pathway = models.ForeignKey(Pathway, on_delete=models.CASCADE)
    x = models.PositiveSmallIntegerField(null=False, blank=False)
    y = models.PositiveSmallIntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.pathway.__str__()} - {self.molecule.__str__()}"
