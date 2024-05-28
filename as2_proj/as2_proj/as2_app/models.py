from django.db import models



from django.db import models

class Supervisor(models.Model):
    supervisor_id = models.IntegerField(primary_key=True, unique=True )
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ThesisProject(models.Model):
    
    topic_num = models.IntegerField(primary_key=True, unique=True )
    title = models.CharField(max_length=300)
    description = models.TextField()
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name='theses_supervised')
    relv_desc = models.CharField(max_length=250)


    def __str__(self):
        return self.title

    


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    student_id = models.IntegerField(primary_key=True, unique=True)
    major = models.CharField(max_length=100)
    thessis = models.ManyToManyField(ThesisProject, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"