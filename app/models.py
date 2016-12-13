from django.db import models

# Create your models here.
# ConstituentID => number --> INT
# DisplayName => string --> CHAR(NUM)
# ArtistBio => textfield --> TEXT
# Nationality => string --> CHAR(NUM)
# Gender => string --> CHAR(NUM)
# BeginDate => number --> SMALLINT
# EndDate => number --> SMALLINT
# Wiki QID => string --> CHAR(NUM)
# ULAN => string --> CHAR(NUM)

class Artist(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    constituent_id = models.IntegerField()
    display_name = models.CharField(max_length=255)
    artist_bio = models.TextField()
    nationality = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    begin_date = models.IntegerField()
    end_date = models.IntegerField()
    wiki_qid = models.CharField(max_length=255)
    ulan = models.CharField(max_length=255)
