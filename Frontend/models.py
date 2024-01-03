from django.db import models

# Create your models here.
class RegisterDB(models.Model):
    Email = models.CharField(max_length=50,null=True,blank=True)
    Username = models.CharField(max_length=50,null=True,blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)
    ConformPassword = models.CharField(max_length=50,null=True,blank=True)

class UserProfileDB(models.Model):
    boolChoice = (
        ("E", "Experienced"), ("F", "Fresher")
    )
    Name = models.CharField(max_length=50,null=True,blank=True)
    FullName = models.CharField(max_length=50,null=True,blank=True)
    Email = models.CharField(max_length=50,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    ProfileImage = models.ImageField(upload_to="ProfileImage",null=True,blank=True)
    Resume = models.FileField(upload_to="document",null=True,blank=True)
    WorkStatus = models.CharField(max_length=1,choices=boolChoice)
    CurrentCompanyName = models.CharField(max_length=50, null=True, blank=True)
    Designation = models.CharField(max_length=50, null=True, blank=True)
    JoiningDate = models.DateField(max_length=50, null=True, blank=True)
    CurrentSalary = models.CharField(max_length=50, null=True, blank=True)
    NoticePeriod = models.CharField(max_length=50, null=True, blank=True)
    Education = models.CharField(max_length=50, null=True, blank=True)
    University = models.CharField(max_length=50, null=True, blank=True)
    PassoutYear = models.DateField(max_length=50, null=True, blank=True)
    Skills = models.CharField(max_length=50, null=True, blank=True)


class ContactDB(models.Model):

    Message = models.CharField(max_length=50,null=True,blank=True)
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.CharField(max_length=50,null=True,blank=True)
    Subject = models.CharField(max_length=50,null=True,blank=True)


class ApplicationDB(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    FullName = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Resume = models.FileField(upload_to="Resume",null=True,blank=True)
    JobTitle = models.CharField(max_length=50,null=True,blank=True)
    CompanyName = models.CharField(max_length=50,null=True,blank=True)



