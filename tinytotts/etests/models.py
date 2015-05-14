from django.db import models
from django.contrib.auth.models import User, Group

# Defines Test Sets
class TestSet(models.Model):
    code = models.CharField(max_length=100, unique=True, blank=False, null=False)
    testname = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    no_ans = models.IntegerField(default=1, blank=False, null=False)
    startdate = models.DateField()
    enddate = models.DateField()
    groups = models.ManyToManyField(Group)
    submit_flag = models.BooleanField(default=False, blank=False, null=False)

    def __unicode__(self):
        return self.code + " - " + self.testname

# Defines Test Sets Lines => filename for the test
class TestSetLine(models.Model):
    filename = models.CharField(max_length=250, blank=False, null=False)
    testset = models.ForeignKey(TestSet, on_delete=models.PROTECT)
    srno = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        unique_together = (('filename', 'testset'), ('srno', 'testset'),)

    def __unicode__(self):
        # return self.testset.code + " - " + self.filename
        return self.filename
        
# Records answers to Questions in Test Sets Lines
class Answer(models.Model):
    marks = models.IntegerField()
    question = models.ForeignKey(TestSetLine, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __unicode__(self):
        return unicode(self.question)
