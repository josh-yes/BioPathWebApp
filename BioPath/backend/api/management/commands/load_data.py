"""
File: load_data.py

Script for clearing and loading fresh data into the database.
Ideally used for testing and to have a consistent database everytime.
This script is called using "python manage.py load_data" from setup.sh
and can be ommitted to retain old database data. 
"""

import api.models as models
from django.contrib.auth.models import User

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, **options):
        
        # now do the things that you want with your models here
        
        for e in models.PathwayEnzyme.objects.all():
          e.delete()
        for e in models.PathwayMolecule.objects.all():
          e.delete()
        for m in models.Molecule.objects.all():
          m.delete()
        for e in models.Enzyme.objects.all():
          e.delete()
        for e in models.Pathway.objects.all():
          e.delete()
        for e in User.objects.all():
          e.delete()

        root = User.objects.create_superuser('root', 'root@biopath.com', 'root')
        m1 = models.Molecule(
            name="molecule1",
            link="",
            abbreviation="m1",
            author=root
        )
        m1.save()

        m2 = models.Molecule(
            name="molecule2",
            link="",
            abbreviation="m2",
            author=root
        )
        m2.save()

        m3 = models.Molecule(
            name="molecule3",
            link="",
            abbreviation="m3",
            author=root
        )
        m3.save()

        e1 = models.Enzyme(
            name="enzyme1",
            link="",
            abbreviation="e1",
            reversible=True,
            author=root
        )
        e1.save()

        e1.cofactors.add(m3)
        e1.substrates.add(m1)
        e1.products.add(m2)

        p1 = models.Pathway(
            name="path1",
            link="",
            public=True,
            author=root
        )
        p1.save()

        pe1 = models.PathwayEnzyme(
            enzyme=e1,
            pathway=p1,
            x=0,
            y=100
        )
        pe1.save()
        pm1 = models.PathwayMolecule(
            molecule=m1,
            pathway=p1,
            x=45,
            y=0
        )
        pm1.save()
        pm2 = models.PathwayMolecule(
            molecule=m2,
            pathway=p1,
            x=45,
            y=240
        )
        pm2.save()
        pm3 = models.PathwayMolecule(
            molecule=m3,
            pathway=p1,
            x=195,
            y=120
        )
        pm3.save()



        # Begin Glucose
        glu = models.Molecule(
            name="Glucose",
            abbreviation="GLU",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        glu.save()

        g6p = models.Molecule(
            name="Glucose 6-Phosphate",
            abbreviation="G6P",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        g6p.save()

        f6p = models.Molecule(
            name="Fructose 6-Phosphate",
            abbreviation="F6P",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        f6p.save()

        f16bp = models.Molecule(
            name="Fructose 1,6-Biphosphate",
            abbreviation="F16BP",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        f16bp.save()

        g3p = models.Molecule(
            name="Glyceraldehyde 3-Phosphate",
            abbreviation="G3P",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        g3p.save()

        dhap = models.Molecule(
            name="Dehydrocycetone Phosphate",
            abbreviation="DHAP",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        dhap.save()

        bpg = models.Molecule(
            name="1,3-Bisphosphoglycerate",
            abbreviation="13BPG",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        bpg.save()

        pg3 = models.Molecule(
            name="3-Phosphoglycerate",
            abbreviation="3PG",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        pg3.save()

        pg2 = models.Molecule(
            name="2-Phosphoglycerate",
            abbreviation="2PG",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        pg2.save()

        pep = models.Molecule(
            name="Phosphoenolpyruvate",
            abbreviation="PEP",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        pep.save()

        pyr = models.Molecule(
            name="Pyruvate",
            abbreviation="PYR",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        pyr.save()

        nad = models.Molecule(
            name="NAD+",
            abbreviation="NAD+",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        nad.save()

        nadh = models.Molecule(
            name="NADH",
            abbreviation="NADH",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        nadh.save()

        h = models.Molecule(
            name="H+",
            abbreviation="H+",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        h.save()

        atp = models.Molecule(
            name="ATP",
            abbreviation="ATP",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        atp.save()

        adp = models.Molecule(
            name="ADP",
            abbreviation="ADP",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        adp.save()

        atp1 = models.Molecule(
            name="ATP",
            abbreviation="ATP",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        atp1.save()

        adp1 = models.Molecule(
            name="ADP",
            abbreviation="ADP",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        adp1.save()

        atp2 = models.Molecule(
            name="ATP",
            abbreviation="ATP",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        atp2.save()

        adp2 = models.Molecule(
            name="ADP",
            abbreviation="ADP",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        adp2.save()

        atp3 = models.Molecule(
            name="ATP",
            abbreviation="ATP",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        atp3.save()

        adp3 = models.Molecule(
            name="ADP",
            abbreviation="ADP",
            #ball_and_stick_image=,
            #space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        adp3.save()

        h2o = models.Molecule(
            name="Hydrogen Dioxide",
            abbreviation="H2O",
            # ball_and_stick_image=,
            # space_filling_image=,
            # link=,
            author=root,
            public=True
        )
        h2o.save()


        # ----- enzymes -----
        hexokinase = models.Enzyme(
            name="Hexokinase",
            abbreviation="HK",
            # image=,
            # link="",
            author=root,
            public=True,
            reversible=False,
            # substrates=[glu, atp],
            # products=[g6p, adp],
            # cofactors=[]
        )
        hexokinase.save()
        hexokinase.substrates.add(glu, atp)
        hexokinase.products.add(g6p, adp)

        phosphoglucoisomerase = models.Enzyme(
            name="Phosphoglucoisomerase",
            abbreviation="PGI",
            # image=,
            # link="",
            author=root,
            public=True,
            reversible=True,
            # substrates=[g6p],
            # products=[f6p],
            # cofactors=[]
        )
        phosphoglucoisomerase.save()
        phosphoglucoisomerase.substrates.add(g6p)
        phosphoglucoisomerase.products.add(f6p)

        phosphofructokinase = models.Enzyme(
            name="Phosphofructokinase",
            abbreviation="PFK",
            # image=,
            # link="",
            author=root,
            public=True,
            reversible=False,
            # substrates=[f6p, atp],
            # products=[f16bp, adp],
            # cofactors=[]
        )
        phosphofructokinase.save()
        phosphofructokinase.substrates.add(f6p, atp1)
        phosphofructokinase.products.add(f16bp, adp1)

        aldolase = models.Enzyme(
            name="Aldolase",
            abbreviation="ALD",
            # image=,
            # link="",
            author=root,
            public=True,
            reversible=True,
            # substrates=[f16bp],
            # products=[g3p, dhap],
            # cofactors=[]
        )
        aldolase.save()
        aldolase.substrates.add(f16bp)
        aldolase.products.add(g3p, dhap)

        triose_phosphate_isomerase = models.Enzyme(
            name="Triose Phosphate Isomerase",
            abbreviation="ISO",
            # image=,
            # link="",
            author=root,
            public=True,
            reversible=True,
            # substrates=[dhap],
            # products=[g3p],
            # cofactors=[]
        )
        triose_phosphate_isomerase.save()
        triose_phosphate_isomerase.substrates.add(dhap)
        triose_phosphate_isomerase.products.add(g3p)

        tpd = models.Enzyme(
            name="Trios Phosphate Dehydrogenase",
            abbreviation="",
            # image=,
            # link="",
            author=root,
            public=True,
            reversible=True,
            # substrates=[g3p, nad],
            # products=[bpg, nadh, h],
            # cofactors=[]
        )
        tpd.save()
        tpd.substrates.add(g3p, nad)
        tpd.products.add(bpg, nadh, h)

        phosphoglycerokinase = models.Enzyme(
            name="Phosphoglycerokinase",
            abbreviation="PGK",
            # image=,
            # link="",
            author=root,
            public=True,
            reversible=True,
            # substrates=[bpg, atp],
            # products=[pg3, adp],
            # cofactors=[]
        )
        phosphoglycerokinase.save()
        phosphoglycerokinase.substrates.add(bpg, atp2)
        phosphoglycerokinase.products.add(pg3, adp2)

        phosphoglyceromutase = models.Enzyme(
            name="Phosphoglyceromutase",
            abbreviation="PGM",
            # image=,
            # link="",
            author=root,
            public=True,
            reversible=True,
            # substrates=[pg3],
            # products=[pg2],
            # cofactors=[]
        )
        phosphoglyceromutase.save()
        phosphoglyceromutase.substrates.add(pg3)
        phosphoglyceromutase.products.add(pg2)

        enolase = models.Enzyme(
            name="Enolase",
            abbreviation="ENO",
            # image=,
            # link="",
            author=root,
            public=True,
            reversible=True,
            # substrates=[pg2],
            # products=[pep],
            # cofactors=[]
        )
        enolase.save()
        enolase.substrates.add(pg2)
        enolase.products.add(pep)

        pyrk = models.Enzyme(
            name="Pyruvate Kinase",
            abbreviation="PYRK",
            # image=,
            # link="",
            author=root,
            public=True,
            reversible=True,
            # substrates=[pep, atp],
            # products=[pyr, adp],
            # cofactors=[]
        )
        pyrk.save()
        pyrk.substrates.add(pep, atp3)
        pyrk.products.add(pyr, adp3)


        # ----- pathway -----
        glycolysis = models.Pathway(
            name="Glycolysis",
            author=root,
            #link=
            public=True
        )
        glycolysis.save()
        # glycolysis.molecules.add(
        #     glu,
        #     g6p,
        #     f6p,
        #     f16bp,
        #     g3p,
        #     dhap,
        #     bpg,
        #     pg3,
        #     pg2,
        #     pep,
        #     pyr,
        #     nad,
        #     nadh,
        #     h,
        #     atp,
        #     adp,
        #     atp1,
        #     adp1,
        #     atp2,
        #     adp2,
        #     h2o
        # )
        # glycolysis.enzymes.add(
        #     hexokinase,
        #     phosphoglucoisomerase,
        #     phosphofructokinase,
        #     aldolase,
        #     triose_phosphate_isomerase,
        #     tpd,
        #     phosphoglycerokinase,
        #     phosphoglyceromutase,
        #     enolase,
        #     pyrk
        # )


        # ----- pathway enzymes -----
        pe1 = models.PathwayEnzyme(
            enzyme=hexokinase,
            pathway=glycolysis,
            x=210,
            y=240
        )
        pe1.save()

        pe2 = models.PathwayEnzyme(
            enzyme=phosphoglucoisomerase,
            pathway=glycolysis,
            x=210,
            y=480
        )
        pe2.save()

        pe3 = models.PathwayEnzyme(
            enzyme=phosphofructokinase,
            pathway=glycolysis,
            x=210,
            y=720
        )
        pe3.save()

        pe4 = models.PathwayEnzyme(
            enzyme=aldolase,
            pathway=glycolysis,
            x=210,
            y=945
        )
        pe4.save()

        pe5 = models.PathwayEnzyme(
            enzyme=triose_phosphate_isomerase,
            pathway=glycolysis,
            x=300,
            y=1200
        )
        pe5.save()

        pe6 = models.PathwayEnzyme(
            enzyme=tpd,
            pathway=glycolysis,
            x=225,
            y=1425
        )
        pe6.save()

        pe7 = models.PathwayEnzyme(
            enzyme=phosphoglycerokinase,
            pathway=glycolysis,
            x=225,
            y=1725
        )
        pe7.save()

        pe8 = models.PathwayEnzyme(
            enzyme=phosphoglyceromutase,
            pathway=glycolysis,
            x=225,
            y=1965
        )
        pe8.save()

        pe9 = models.PathwayEnzyme(
            enzyme=enolase,
            pathway=glycolysis,
            x=225,
            y=2235
        )
        pe9.save()

        pe10 = models.PathwayEnzyme(
            enzyme=pyrk,
            pathway=glycolysis,
            x=225,
            y=2520
        )
        pe10.save()

        # ----- pathway molecule -----
        pm1 = models.PathwayMolecule(
            molecule=glu,
            pathway=glycolysis,
            x=200,
            y=150
        )
        pm1.save()

        pm2 = models.PathwayMolecule(
            molecule=atp,
            pathway=glycolysis,
            x=315,
            y=150
        )
        pm2.save()

        pm3 = models.PathwayMolecule(
            molecule=g6p,
            pathway=glycolysis,
            x=195,
            y=390
        )
        pm3.save()

        pm4 = models.PathwayMolecule(
            molecule=adp,
            pathway=glycolysis,
            x=315,
            y=390
        )
        pm4.save()

        pm5 = models.PathwayMolecule(
            molecule=f6p,
            pathway=glycolysis,
            x=195,
            y=615
        )
        pm5.save()

        pm6 = models.PathwayMolecule(
            molecule=atp1,
            pathway=glycolysis,
            x=315,
            y=615
        )
        pm6.save()

        pm7 = models.PathwayMolecule(
            molecule=f16bp,
            pathway=glycolysis,
            x=210,
            y=855
        )
        pm7.save()

        pm8 = models.PathwayMolecule(
            molecule=adp1,
            pathway=glycolysis,
            x=300,
            y=855
        )
        pm8.save()

        pm9 = models.PathwayMolecule(
            molecule=dhap,
            pathway=glycolysis,
            x=345,
            y=1110
        )
        pm9.save()

        pm10 = models.PathwayMolecule(
            molecule=g3p,
            pathway=glycolysis,
            x=195,
            y=1335
        )
        pm10.save()

        pm11 = models.PathwayMolecule(
            molecule=nad,
            pathway=glycolysis,
            x=330,
            y=1335
        )
        pm11.save()

        pm12 = models.PathwayMolecule(
            molecule=bpg,
            pathway=glycolysis,
            x=225,
            y=1560
        )
        pm12.save()

        pm13 = models.PathwayMolecule(
            molecule=nadh,
            pathway=glycolysis,
            x=315,
            y=1560
        )
        pm13.save()

        pm14 = models.PathwayMolecule(
            molecule=adp2,
            pathway=glycolysis,
            x=315,
            y=1875
        )
        pm14.save()

        pm15 = models.PathwayMolecule(
            molecule=pg3,
            pathway=glycolysis,
            x=225,
            y=1875
        )
        pm15.save()

        pm16 = models.PathwayMolecule(
            molecule=atp2,
            pathway=glycolysis,
            x=315,
            y=1635
        )
        pm16.save()

        pm17 = models.PathwayMolecule(
            molecule=pg2,
            pathway=glycolysis,
            x=270,
            y=2130
        )
        pm17.save()

        pm18 = models.PathwayMolecule(
            molecule=pep,
            pathway=glycolysis,
            x=210,
            y=2385
        )
        pm18.save()

        pm19 = models.PathwayMolecule(
            molecule=atp3,
            pathway=glycolysis,
            x=330,
            y=2385
        )
        pm19.save()

        pm20 = models.PathwayMolecule(
            molecule=pyr,
            pathway=glycolysis,
            x=210,
            y=2670
        )
        pm20.save()

        pm21 = models.PathwayMolecule(
            molecule=adp3,
            pathway=glycolysis,
            x=330,
            y=2670
        )
        pm21.save()