from django.db import models


# Create your models here.

class PointsTable(models.Model):
    team_name = models.CharField(max_length=255, null=False)
    played = models.IntegerField(null=False, default=0)
    won = models.IntegerField(null=False, default=0)
    lost = models.IntegerField(null=False, default=0)
    no_result = models.IntegerField(null=False, default=0)
    points = models.FloatField(null=False, default=0.0)
    nrr = models.FloatField(null=False, default=0)





    def __str__(self):
        return "{}".format(self.team_name)
