import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, States, Region, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    for row in reader:
        try:
            y = int(row[3])
        except:
            y = None
        try:
            lo = float(row[4])

        except:
            lo = None
        try:
            la = float(row[5])
        except:
            la = None
        try:
            a = float(row[6].strip())
        except:
            a = None

        # print(y,lo,la,a)

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python
    # try:
    #     site = Site.objects.get(name=row[0])
    # except:
    #     site = Site(name=row[0], description=row[1], justification=row[2], year=y, longitude=lo,latitude=la,acrea_hectares=a )
    #     site.save()

    # try:
    #     category = Category.objects.get(category=row[7])
    # except:
    #     category = Category(category=row[7])
    #     category.save()


        category, created = Category.objects.get_or_create(name=row[7])
        states, created = States.objects.get_or_create(name=row[8])
        region, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])
        site, created = Site.objects.get_or_create(name=row[0], description=row[1], justification=row[2], year=y, longitude=lo,latitude=la,area_hectares=a,category=category,states=states,region=region,iso=iso)


        category.save()
        states.save()
        region.save()
        iso.save()
        site.save()

