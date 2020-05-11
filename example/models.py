from django.db import models


KIND_CHOICES = (
    ("초등학교", "초등학교"),
    ("중학교", "중학교"),
    ("고등학교", "고등학교"),
)

class School(models.Model):
    kind = models.CharField(max_length=4, choices=KIND_CHOICES,)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=5)
    school = models.ForeignKey(
        School, 
        related_name="students", 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name