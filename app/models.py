from django.db import models

class Artist(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    constituent_id = models.IntegerField(null=True)
    display_name = models.CharField(max_length=255)
    artist_bio = models.TextField()
    nationality = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    begin_date = models.IntegerField(null=True)
    end_date = models.IntegerField(null=True)
    wiki_qid = models.CharField(max_length=255)
    ulan = models.CharField(max_length=255)

# Get data from DB
male = 0
female = 0

for a in Artist.objects.all():
    print(a.gender)
    if a.gender == 'M':
        male += 1
    elif a.gender == 'F':
        female += 1

print('M', male)
print('F', female)