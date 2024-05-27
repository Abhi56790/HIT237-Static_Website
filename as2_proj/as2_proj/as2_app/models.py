from django.db import models

class ThesisProject(models.Model):
    id = models.IntegerField(primary_key=True)
    topic_num = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    superviser = models.CharField(max_length=100)
    relv_desc = models.CharField(max_length=250)

    def __str__(self):
        return self.title