from django.db import models
from django.contrib.auth.models import User, Group

# Defines Test Sets
class TestSet(models.Model):
    testname = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    startdate = models.DateField()
    enddate = models.DateField()
    groups = models.ManyToManyField(Group)

    def __unicode__(self):
        return self.testname

# Defines Test Sets Lines => filename for the test
class TestSetLine(models.Model):
    filename = models.CharField(max_length=250, blank=False, null=False)
    testset = models.ForeignKey(TestSet)
    srno = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        unique_together = ('filename', 'testset',)
        unique_together = ('srno', 'testset',)

    def __unicode__(self):
        return self.filename
        
# Records answers to Questions in Test Sets Lines
class answer(models.Model):
    marks = models.IntegerField()
    question = models.ForeignKey(TestSetLine)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.question
