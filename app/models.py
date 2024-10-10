from django.db import models

# Create your models here.
class content(models.Model):
    topic_name = models.CharField(primary_key=True,max_length=100)
    def __str__(self):
        return self.topic_name
class data1(models.Model):
    topic_name = models.ForeignKey(content,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()
    def __str__(self):
        return self.name
    def __str__(self):
        return self.url
class data2(models.Model):
    course = models.CharField(max_length=100)
    def __str__(self):
        return self.course

