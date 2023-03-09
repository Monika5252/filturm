import re

from django.test import TestCase

# Create your tests here.

#
a="filturm object (200)"
f='Ranjit'
l="Shinde"
fullname=f[0]+l[0]
# print("Original String : " + inp_str)
num =""
for c in a:
    if c.isdigit():
        num = num + c
print("Extracted numbers from the list : " + num)
print(type(num))
eid=fullname+"0"+num
print(eid)
# c="filturm object (42)"
# num1 = ""
# for d in c:
#     if c.isdigit():
#         num1 = num1 +1
# print("Extracted numbers from the list : " + num1)

class Leave( models.Model ):
    # eid = models.AutoField( primary_key=True )
    eid= models.ForeignKey(em, on_delete=models.CASCADE)
    appdate = models.DateField()
    appname = models.CharField( max_length=250 )
    leavetype = models.CharField( max_length=250 )
    datefrom = models.DateField()
    dateto = models.DateField()
    resumeon = models.DateField()
    leaveday = models.CharField( max_length=50 )
    leavebalance = models.CharField( max_length=50 )
    leavereason = models.CharField( max_length=50 )

def leave(request):
    if request.method=="POST":
        la=request.POST['ap']
        ap=request.POST['apn']
        lt=request.POST['lt']
        datefrom=request.POST['df']
        dateto=request.POST['dt']
        resumeon=request.POST['ro']
        leaveday=request.POST['ldd']
        leavebalance=request.POST['lb']
        leavereason=request.POST['lr']
        Leave(appdate=la,appname=ap,leavetype=lt,datefrom=datefrom,dateto=dateto,resumeon=resumeon,leaveday=leaveday,leavebalance=leavebalance,leavereason=leavereason).save()
    return render(request,'apllication.html')