from django.db import models

# user registration
class userregistrationmodel(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class struture_of_teams(models.Model):
    name = models.CharField(max_length=100)
    logo=models.FileField(upload_to='pics', null=True, blank=True)
    club_state=models.CharField(max_length=100)

class structure_of_players(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    jersy_number=models.IntegerField()
    country=models.CharField(max_length=100)
    total_matches=models.IntegerField()
    total_runs=models.IntegerField()
    highest_score=models.IntegerField()
    fiftys=models.IntegerField()
    hundreds=models.IntegerField()
    man_of_the_matches=models.IntegerField()
    winner_of_matches=models.IntegerField()
    image = models.FileField(upload_to='pics', null=True, blank=True)
    flag = models.FileField(upload_to='pics', null=True, blank=True)

class matches_between_teams(models.Model):
    team_a=models.CharField(max_length=100)
    team_b=models.CharField(max_length=100)
    match_date=models.DateField()

class points_between_teams(models.Model):
    team_a = models.CharField(max_length=100)
    team_b = models.CharField(max_length=100)
    match_date = models.DateField()
    winner_of_match=models.CharField(max_length=100)
    points_of_team=models.IntegerField()
    total_points=models.IntegerField()

class pointstable(models.Model):

    team=models.CharField(max_length=100)
    match=models.IntegerField()
    won=models.IntegerField()
    lost=models.IntegerField()
    n_r=models.IntegerField()
    points=models.IntegerField()
    nrr=models.FloatField()