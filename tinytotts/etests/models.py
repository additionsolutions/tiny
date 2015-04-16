from django.db import models

# Defines Test Sets
class TestSet(models.Model):
    testname = models.CharField(max_length=100, blank=False, null=False)
    startdate = models.DateField()
    enddate = models.DateField()

    def __unicode__(self):
        return self.testname

# Defines Test Sets Lines => filename for the test
class TestSetLine(models.Model):
    filename = models.CharField(max_length=250, blank=False, null=False)
    testset = models.ForeignKey(TestSet)
    srno = models.IntegerField(unique=True)

    def __unicode__(self):
        return self.filename
