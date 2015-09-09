from django.db import models

# Create your models here.
class Type(models.Model):
  name = models.CharField(max_length=128, unique=True)
  description = models.CharField(max_length=128)

  def __str__(self):
    return self.name
  
  class Meta:
    ordering = ["name"]

class Series(models.Model):
  name = models.CharField(max_length=128, unique=True)
  short_description = models.CharField(max_length=128, blank=True)
  long_description = models.TextField(blank=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]

class Pastor(models.Model):
  name = models.CharField(max_length=128, unique=True)
  bio = models.TextField(blank=True)
  picture = models.URLField(blank=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]

class Sermon(models.Model):
  sermon_title = models.CharField(max_length=128)
  pastor = models.ForeignKey(Pastor, null=True)
  verse = models.CharField(max_length=128)
  type = models.ForeignKey(Type)
  series = models.ForeignKey(Series, null=True)
  pub_date = models.DateField('Date Preached', blank=True)
  main_thought = models.CharField(max_length=512, blank=True)
  challenge = models.CharField(max_length=512, blank=True)
  url = models.CharField(max_length=1024)
  thumbnail = models.URLField(blank=True)
  video = models.URLField(blank=True)
  sequence_num = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return self.sermon_title

  class Meta:
    ordering = ["-pub_date", "sequence_num"]

class Featured(models.Model):
  featured = models.OneToOneField(Sermon)

  def __str__(self):
    return self.featured.sermon_title
