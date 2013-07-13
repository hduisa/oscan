from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Bugs(models.Model):
    btype = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    level = models.IntegerField()
    suggestion = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.btype)

    

class Tasks(models.Model):
    userid = models.IntegerField()
    taskname = models.CharField(max_length=200)
    starttime = models.DateTimeField()
    finishtime = models.DateTimeField()
    status = models.CharField(max_length=200)
    numberofurl = models.IntegerField()

    def __unicode__(self):
        return str(self.taskname)
    

class Results(models.Model):
    task = models.ForeignKey(Tasks)
    numberintask = models.IntegerField()
    bugtype = models.CharField(max_length=200)
    detail = models.CharField(max_length=200)
    bugid = models.IntegerField()
    
    def __unicode__(self):
        return str(self.task) + str(self.bugid)


