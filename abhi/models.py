from django.db import models

# # Create your models here.

#employee information

class filturm(models.Model):
    filturmid=models.IntegerField(primary_key=True)
    fname=models.CharField(max_length=200)
    mname = models.CharField( max_length=200 )
    lname = models.CharField( max_length=200 )
    dob = models.DateField()
    birthplace = models.CharField( max_length=200 )
    birthplacetaluka = models.CharField( max_length=200 )
    bpd= models.CharField( max_length=200 )
    age = models.CharField( max_length=200 )
    languageknown = models.CharField( max_length=200 )
    gender = models.CharField( max_length=20 )
    maristetus = models.CharField( max_length=200 )
    bloodgroup = models.CharField( max_length=20 )
    nationality = models.CharField( max_length=200 )
    religion = models.CharField( max_length=20 )
    cast = models.CharField( max_length=200 )
    category=models.CharField(max_length=50,default=0)
    emailid = models.CharField( max_length=255)
    contactno = models.CharField( max_length=200 )
    emergencycontactno = models.CharField( max_length=20 )
    ak = models.CharField( max_length=200 )
    adharimage =models.ImageField()
    pancardno = models.CharField( max_length=200 )
    panimage =models.ImageField()
    pad=models.CharField( max_length=100 )
    pincode = models.CharField( max_length=20 )
    permanentaddress = models.CharField( max_length=200 )
    perpincode = models.CharField( max_length=20 )
    Eii = models.ImageField()
    ssc = models.CharField( max_length=200, default=0 )
    sscbord = models.CharField( max_length=200, default=0 )
    sscpersentage = models.CharField( max_length=200, default=0 )
    sscpassingyear = models.CharField( max_length=200, default=0 )
    ssccertificate = models.ImageField( default=0 )
    hsc = models.CharField( max_length=200, default=0 )
    hsccbord = models.CharField( max_length=200, default=0 )
    hsccpersentage = models.CharField( max_length=200, default=0 )
    hscpassingyear = models.CharField( max_length=200, default=0 )
    hsccertificate = models.ImageField( default=0 )
    diploma = models.CharField( max_length=200, default='' )
    diplomabord = models.CharField( max_length=200, default='' )
    diplomapersentage = models.CharField( max_length=200, default='' )
    diplomapassingyear = models.CharField( max_length=200, default='' )
    diplomacertificate = models.ImageField( default=0 )
    gradution = models.CharField( max_length=200, default='' )
    gradutionbord = models.CharField( max_length=200, default='' )
    gradutionpersentage = models.CharField( max_length=200, default='' )
    gradutionpassingyear = models.CharField( max_length=200, default='' )
    gradutioncertificate = models.ImageField( default=0 )
    postgradution = models.CharField( max_length=200, default='' )
    postgradutionbord = models.CharField( max_length=200, default='' )
    postgradutionpersentage = models.CharField( max_length=200, default='' )
    postgradutionpassingyear = models.CharField( max_length=200, default='' )
    postgradutioncertificate = models.ImageField( default=0 )
    other = models.CharField( max_length=200, default='' )
    institude = models.CharField( max_length=200, default='' )
    corsename = models.CharField( max_length=200, default=0 )
    corsepersentage = models.CharField( max_length=200, default=0 )
    corsecertificate = models.ImageField( default='' )
    father = models.CharField( max_length=200 ,default=0)
    fdob = models.DateField(default=0)
    fage = models.CharField( max_length=200,default=0 )
    fgen = models.CharField( max_length=200 ,default=0)
    frelation = models.CharField( max_length=200 ,default=0)
    mather = models.CharField( max_length=200 ,default=0)
    mdob = models.DateField(default=0)
    mage = models.CharField( max_length=200 ,default=0)
    mgen = models.CharField( max_length=200 ,default=0)
    mrelation = models.CharField( max_length=200 ,default=0)
    cihldren1 = models.CharField( max_length=200 ,default=0)
    c1dob = models.DateField(default=0)
    c1age = models.CharField( max_length=200,default=0)
    c1gen = models.CharField( max_length=200,default=0 )
    c1relation = models.CharField( max_length=200,default=0 )
    children2 = models.CharField( max_length=200 ,default=0)
    c2dob = models.DateField(default=0)
    c2age = models.CharField( max_length=200,default=0 )
    c2gen = models.CharField( max_length=200,default=0 )
    c2relation = models.CharField( max_length=200 ,default=0)
    companyname = models.CharField( max_length=200 ,default=0)
    durationfrom = models.DateField(default=0)
    durationto = models.DateField(default=0)
    joiningctc = models.CharField( max_length=200,default=0 )
    lctc = models.CharField( max_length=200 ,default=0)
    twe = models.CharField( max_length=200,default=0 )
    def __str__(self):
        return str(self.filturmid)
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username
class em(models.Model):
    ids=models.CharField(primary_key=True,max_length=50,unique=True)
    employeename=models.CharField(max_length=50)
    pas=models.CharField(max_length=50)
    def __str__(self):
        return self.ids
class EmpLeave(models.Model):
    filturmid=models.ForeignKey(filturm,on_delete=models.CASCADE)
    appdate = models.DateField()
    appname = models.CharField(max_length=250)
    leavetype = models.CharField(max_length=250)
    datefrom = models.DateField()
    dateto = models.DateField()
    resumeon = models.DateField()
    leaveday = models.CharField(max_length=50)
    leavebalance = models.CharField(max_length=50)
    leavereason = models.CharField(max_length=50)
    def __str__(self):
        return (self.filturmid.fname)



from django.db import models
from django.contrib.auth.models import User

class TimeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)


    def total(self):
        totaltime = 0
        totalprice = self.start_time - self.end_time
        return totaltime


    # def __str__(self):
    #     return self.user

