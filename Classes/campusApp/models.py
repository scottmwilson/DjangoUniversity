from django.db import models

class UniversityCampus(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    campus_id = models.IntegerField()

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "University Campuses"

    def __str__(self):
        return self.name
