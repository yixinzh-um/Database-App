import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from jobs.models import Job,Employer,Comment, Location


import re

def run():
    fhand = open('jobs/all_jobs.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header


    Job.objects.all().delete()
    Employer.objects.all().delete()
    Comment.objects.all().delete()

    for row in reader:

        row=[None if i.strip() =="-1" else i for i in row ]

        s = re.findall('[0-9]+',row[2])

        des=row[3].replace('\n', ' <br />')

        sl=s[0]
        sh=s[1]
        try:
            sl= int(sl)
        except:
            sl = None
        try:
            sh=int(sh)
        except:
            lo = None

        e = row[5].split('\n')[0]
        try:
            r= float(row[4])
        except:
            r = None


        ea=row[15]
        if ea == "TRUE":
            ea= "Yes"
        else:
            ea= "No"

        employer, created = Employer.objects.get_or_create(name=e,headquarters=row[7],size=row[8],founded=row[9],ownership_type=row[10],industry=row[11],revenue=row[13],competitor=row[14])
        location, created = Location.objects.get_or_create(name=row[6])
        job, created = Job.objects.get_or_create(title=row[1], employer=employer, location=location, salary_l=sl, salary_h=sh,rating=r,description=des,sector=row[12],easy_apply=ea)

        employer.save()
        location.save()
        job.save()

