from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Bugs(models.Model):
    type = models.CharField(max_length=200,primary_key=True)
    name = models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    level = models.IntegerField()
    suggestion = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.btype)

class Tasks(models.Model):
    taskid=models.IntegerField(primary_key=True)
    userid= models.IntegerField()
    starttime = models.DateTimeField()
    finishtime = models.DateTimeField()
    status = models.CharField(max_length=200)
    numberofurl = models.IntegerField()

    def __unicode__(self):
        return str(self.taskname)

class Results(models.Model):
    taskid = models.ForeignKey(Tasks)
    numberintask = models.IntegerField(primary_key=True)
    bugtype = models.ForeignKey(Bugs)
    detail = models.CharField(max_length=200)
    
    def __unicode__(self):
        return str(self.task) + str(self.bugid)


    