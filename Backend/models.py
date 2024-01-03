from django.db import models

# Create your models here.
class CompanyDB(models.Model):
    CompanyName = models.CharField(max_length=100,null=True,blank=True)
    ContactNumber = models.IntegerField(null=True,blank=True)
    CompanyEmail = models.CharField(max_length=100,null=True,blank=True)
    CompanyPassword = models.CharField(max_length=100,null=True,blank=True)
    CompanyLocation = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=1500,null=True,blank=True)
    Image = models.ImageField(upload_to="Images",null=True,blank=True)
    Address = models.CharField(max_length=500, null=True, blank=True)
    Website = models.CharField(max_length=50, null=True, blank=True)
    Domain = models.CharField(max_length=50, null=True, blank=True)

class JobDB(models.Model):
    CompanyName = models.CharField(max_length=100, null=True, blank=True)
    JobTitle = models.CharField(max_length=100, null=True, blank=True)
    CompanyEmail = models.CharField(max_length=100, null=True, blank=True)
    PostedOn = models.CharField(max_length=100, null=True, blank=True)
    ClosingOn = models.CharField(max_length=100, null=True, blank=True)
    BriefDescription = models.TextField(null=True, blank=True)
    PreferredSkills = models.TextField(null=True, blank=True)
    Image = models.ImageField(upload_to="CompImages", null=True, blank=True)
    Location = models.CharField(max_length=100, null=True, blank=True)
    JobType = models.CharField(max_length=100, null=True, blank=True)
    Experience = models.CharField(max_length=100, null=True, blank=True)
    Salary = models.CharField(max_length=100, null=True, blank=True)
    Vacancy = models.IntegerField(null=True, blank=True)
    Website = models.CharField(max_length=50, null=True, blank=True)
    JobCategory = models.CharField(max_length=100, null=True, blank=True)

class JobCategoryDB(models.Model):
    JobCategory = models.CharField(max_length=100, null=True, blank=True)
    CategoryImage = models.ImageField(upload_to="CategoryImage", null=True, blank=True)