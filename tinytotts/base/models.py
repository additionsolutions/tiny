from django.db import models
from django.contrib.auth.models import User,Group

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    
    # The additional attributes we wish to include.
    father_name = models.CharField(max_length=20, blank=False, default='-Not mentioned-')
    mother_name = models.CharField(max_length=20, blank=False, default='-Not mentioned-')
    website = models.URLField(blank=True)
    mobile = models.PositiveIntegerField(blank=False, default=0000000000)
    picture = models.ImageField(upload_to='profile_images', blank=False, default='no_image.png')
    
    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.picture)
    image_thumb.short_description = 'Thumb'
    image_thumb.allow_tags = True
    
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
        
# Defines Phonetics
class Phonetics(models.Model):
    code = models.CharField(max_length=100, unique=True, blank=False, null=False)
    phoneticsname = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    startdate = models.DateField()
    enddate = models.DateField()
    groups = models.ManyToManyField(Group)

    def __unicode__(self):
        return self.code + " - " + self.phoneticsname

class PhoneticsLine(models.Model):
    filename = models.CharField(max_length=250, blank=True, null=True)
    phonetics = models.ForeignKey(Phonetics, on_delete=models.PROTECT)
    srno = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        unique_together = (('srno', 'phonetics'),)
	# unique_together = (('filename', 'testset'), ('srno', 'testset'),)

    def __unicode__(self):
        return self.phonetics.code + " - " + self.filename
