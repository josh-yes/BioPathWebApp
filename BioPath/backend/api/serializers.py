"""
File: serialzers.py
Description: Defines the serializers for serializing various models in
    models.py into json. These serializers are used to create viewsets in
    views.py to simplify and standardize the data format that is returned by
    the API.
Modified: 11/17 - Josh Schmitz
TODO: If you explicitly specify a relational field pointing to a ManyToManyField with a through model, be sure to set read_only to True.
TODO: Optimmize with prefetch_related or select_related https://www.django-rest-framework.org/api-guide/relations/
"""

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from . import models


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            "id",
            "name"
        ]
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "groups"
        ]


class MoleculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Molecule
        fields = "__all__"


class EnzymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enzyme
        fields = "__all__"


class PathwayEnzymeDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source="enzyme.id")
    name = serializers.CharField(
        source="enzyme.name",
        max_length=50
    )
    abbreviation = serializers.CharField(
        source="enzyme.abbreviation",
        max_length=10
    )
    image = serializers.ImageField(
        source="enzyme.image",
        allow_empty_file=True
    )
    reversible = serializers.BooleanField(source="enzyme.reversible")
    substrates = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    cofactors = serializers.SerializerMethodField()
    link = serializers.URLField(
        source="enzyme.link",
        allow_blank=True
    )
    author = serializers.ReadOnlyField(source="enzyme.author.id")
    public = serializers.BooleanField(source="enzyme.public")

    class Meta:
        model = models.PathwayEnzyme
        fields = [
            "id",
            "name",
            "x",
            "y",
            "abbreviation",
            "image",
            "reversible",
            "substrates",
            "products",
            "cofactors",
            "link",
            "author",
            "public"
        ]

    def get_substrates(self, obj):
        enzyme = models.Enzyme.objects.get(id=obj.enzyme.id)
        substrates = [molecule.id for molecule in enzyme.substrates.all()]
        return substrates

    def get_products(self, obj):
        enzyme = models.Enzyme.objects.get(id=obj.enzyme.id)
        products = [molecule.id for molecule in enzyme.products.all()]
        return products

    def get_cofactors(self, obj):
        enzyme = models.Enzyme.objects.get(id=obj.enzyme.id)
        cofactors = [molecule.id for molecule in enzyme.cofactors.all()]
        return cofactors

    
class PathwayEnzymeBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PathwayEnzyme
        fields = "__all__"


class PathwayMoleculeDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source="molecule.id")
    name = serializers.CharField(
        source="molecule.name",
        max_length=50
    )
    abbreviation = serializers.CharField(
        source="molecule.abbreviation",
        max_length=10
    )
    ball_and_stick_image = serializers.ImageField(
        source="molecule.ball_and_stick_image",
        allow_empty_file=True
    )
    space_filling_image = serializers.ImageField(
        source="molecule.space_filling_image",
        allow_empty_file=True
    )
    link = serializers.URLField(
        source="molecule.link",
        allow_blank=True
    )
    author = serializers.ReadOnlyField(source="molecule.author.id")
    public = serializers.BooleanField(source="molecule.public")

    class Meta:
        model = models.PathwayMolecule
        fields = [
            "id",
            "name",
            "x",
            "y",
            "abbreviation",
            "ball_and_stick_image",
            "space_filling_image",
            "link",
            "author",
            "public"
        ]


class PathwayMoleculeBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PathwayMolecule
        fields = "__all__"


class PathwaySerializer(serializers.ModelSerializer):
    enzymes = PathwayEnzymeDetailSerializer(
        source="pathwayenzyme_set",
        many=True
    )
    molecules = PathwayMoleculeDetailSerializer(
        source="pathwaymolecule_set",
        many=True
    )
    
    class Meta:
        model = models.Pathway
        fields = "__all__"
        