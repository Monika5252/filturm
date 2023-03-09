from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
# from django.http import Httpresponce
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import get_object_or_404

from .models import *
from django.http import HttpResponse
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime

import csv
# from datetime import datetime
# from abhi.models import f
# Create your views here.
def send_email_from_app():
    pass



def fun1(request):
    if request.method == "POST":
        global fullname
        global laname
        global num
        global fn
        global user
        firstname = request.POST.get('fname')
        middlename = request.POST['mname']
        # midname = request.POST.get('mname')

        lastname = request.POST['lname']
        laname=request.POST.get('lname')
        dateofbirth = request.POST['DOB']
        birthplace = request.POST['bplace']
        birthplacetaluka = request.POST['bptaluka']
        bpd = request.POST['bpd']
        age = request.POST['age']
        languageknown = request.POST['lknown']
        gender = request.POST['gender']
        marritalstatus = request.POST['mstetus']
        bloodgroup = request.POST['bgroup']
        nationality = request.POST['nlity']
        religion = request.POST['religion']
        cast = request.POST['cast']
        category = request.POST['category']
        emailid = request.POST['emailid']
        user=request.POST.get('emailid')
        contactno = request.POST['contactno']
        emergencycontactno = request.POST['eno']
        ak=request.POST['ak']
        adharimage = request.POST['adharimage']
        pancardno = request.POST['panno']
        panimage = request.POST['panimage']
        pad=request.POST['pad']
        pincode = request.POST['pincode']
        permanentaddress = request.POST['peraddress']
        perpincode = request.POST['percode']
        employeeimage=request.POST['adhura']
        ssc = request.POST['SSC']
        sscbord = request.POST['sscbord']
        sscpersentage = request.POST['sscpersentage']
        sscpassingyear = request.POST['sscpassingyear']
        ssccertificate = request.POST['ssccer']
        hsc = request.POST['hsc']
        hsccbord = request.POST['hsccbord']
        hsccpersentage = request.POST['hscpersentage']
        hscpassingyear = request.POST['hscpassingyear']
        hsccertificate = request.POST['hsccer']
        diploma = request.POST['diploma']
        diplomabord = request.POST['diplomabord']
        diplomapersentage = request.POST['diplomapersentage']
        diplomapassingyear = request.POST['diplomapassingyear']
        diplomacertificate = request.POST['diploma']
        gradution = request.POST['gradution']
        gradutionbord = request.POST['gradutionbord']
        gradutionpersentage = request.POST['gradutionpersentage']
        gradutionpassingyear = request.POST['gradutionpassingyear']
        gradutioncertificate = request.POST['gradutioncer']
        postgradution = request.POST['postgradution']
        postgradutionbord = request.POST['postgradutionbord']
        postgradutionpersentage = request.POST['postgradutionpersentage']
        postgradutionpassingyear = request.POST['postgradutionpassingyear']
        postgradutioncertificate = request.POST['postgradutioncer']
        other = request.POST['other']
        institude = request.POST['institute']
        corsename = request.POST['corsename']
        corsepersentage = request.POST['corsepersentage']
        corsecertificate = request.POST['corsecer']
        father = request.POST['father']
        fdob = request.POST['fdob']
        fage = request.POST['fage']
        fgen = request.POST['ffgen']
        frelation = request.POST['frelstion']
        mather = request.POST['mather']
        mdob = request.POST['mdob']
        mage = request.POST['mage']
        mgen = request.POST['mgen']
        mrelation = request.POST['mrelstion']
        cihldren1 = request.POST['children1']
        c1dob = request.POST['c1dob']
        c1age = request.POST['c1age']
        c1gen = request.POST['c1gen']
        c1relation = request.POST['c1relstion']
        children2 = request.POST['children2']
        c2dob = request.POST['c2dob']
        c2age = request.POST['c2age']
        c2gen = request.POST['c2gen']
        c2relation = request.POST['c2relstion']
        companyname = request.POST['companyname']
        durationfrom = request.POST['durationfrom']
        durationto = request.POST['durationto']
        joiningctc = request.POST['joiningctc']
        lctc = request.POST['lctc']
        twe = request.POST['twe']
        fullname=firstname[0]+laname[0]
        fn=firstname+" "+laname
        print(type(fullname))
        filturm(fname=firstname, mname=middlename,lname=lastname,dob=dateofbirth,birthplace=birthplace,
                 birthplacetaluka=birthplacetaluka,bpd=bpd,age=age,languageknown=languageknown,
                 gender=gender,maristetus=marritalstatus,bloodgroup=bloodgroup,nationality=nationality,religion=religion,
                 cast=cast,category=category,emailid=emailid,contactno=contactno,emergencycontactno=emergencycontactno,
                 ak=ak,adharimage=adharimage,pancardno=pancardno,panimage=panimage,pad=pad,
                 pincode=pincode,
              permanentaddress=permanentaddress,
              perpincode=perpincode,
              Eii=employeeimage,ssc=ssc, sscbord=sscbord, sscpersentage=sscpersentage, sscpassingyear=sscpassingyear,
              ssccertificate=ssccertificate,
              hsc=hsc, hsccbord=hsccbord, hsccpersentage=hsccpersentage, hscpassingyear=hscpassingyear,
              hsccertificate=hsccertificate,
              diploma=diploma, diplomabord=diplomabord, diplomapersentage=diplomapersentage,
              diplomapassingyear=diplomapassingyear, diplomacertificate=diplomacertificate
              , gradution=gradution, gradutionbord=gradutionbord, gradutionpersentage=gradutionpersentage,
              gradutionpassingyear=gradutionpassingyear, gradutioncertificate=gradutioncertificate,
              postgradution=postgradution, postgradutionbord=postgradutionbord,
              postgradutionpersentage=postgradutionpersentage,
              postgradutionpassingyear=postgradutionpassingyear,
              postgradutioncertificate=postgradutioncertificate,
              other=other, institude=institude, corsename=corsename, corsepersentage=corsepersentage,
              corsecertificate=corsecertificate,
                father=father, fdob=fdob, fage=fage, fgen=fgen, frelation=frelation, mather=mather, mdob=mdob,
                mage=mage, mrelation=mrelation,
                cihldren1=cihldren1,c1dob=c1dob,c1age=c1age,c1gen=c1gen,children2=children2,c2dob=c2dob,c2gen=c2gen,c2relation=c2relation,
                companyname=companyname,
                durationfrom=durationfrom,
                durationto=durationto,
                joiningctc=joiningctc,
                lctc=lctc,
                twe=twe).save()

        b=filturm.objects.latest('id')
        a=str(b)

        # print("Original String : " + inp_str)
        num =""
        for d in a:
            if d.isdigit():
                num = num + d
        print("Extracted numbers from the list : " + num)
        num=fullname+"0"+num
        print(num)
        # print(type(num1))

        import reportlab  # import the library
        from reportlab.pdfgen import canvas  # import modules
        p = canvas.Canvas( '2.pdf' )
        # Init a PDF object

        p.drawString( 200, 200, "My name is"+ firstname )  # Draw a simple String
        p.showPage()  # Create the PDF
        c=p.save()

        html_tpl_path = 'pdfpage.html'
        context_data = {'name': request.POST.get( 'fname' ), 'midname': request.POST.get( 'mname' ),
                        'lastname': request.POST.get( 'lname' ), 'dob': request.POST.get( 'DOB' ),
                        'birthplace': request.POST.get( 'bplace' ),
                        'birthplacetaluka': request.POST.get( 'bptaluka' ), 'bpd': request.POST.get( 'bpd' ),
                        'age': request.POST.get( 'age' ), 'languageknown': request.POST.get( 'lknown' ),
                        'gender': request.POST.get( 'gender' ), 'marritalstatus': request.POST.get( 'mstetus' ),
                        'bloodgroup': request.POST.get( 'bgroup' ), 'nationality': request.POST.get( 'nlity' ),
                        'religion ': request.POST.get( 'religion' ), 'cast': request.POST.get( 'cast' ),
                        'category': request.POST.get( 'category' ), 'emailid': request.POST.get( 'emailid' ),
                        'user': request.POST.get( 'emailid' ), 'contactno': request.POST.get( 'contactno' ),
                        'emergencycontactno': request.POST.get( 'eno' ),
                        'ak': request.POST.get( 'ak' ), 'adharimage': request.POST.get( 'adharimage' ),
                        'pancardno': request.POST.get( 'panno' ), 'panimage': request.POST.get( 'panimage' ),
                        'pad': request.POST.get( 'pad' ), 'pincode': request.POST.get( 'pincode' ),
                        'permanentaddress': request.POST.get( 'peraddress' ),
                        'perpincode': request.POST.get( 'percode' ), 'employeeimage': request.POST.get( 'adhura' ),
                        'ssc': request.POST.get( 'SSC' ),
                        'sscbord': request.POST.get( 'sscbord' ), 'sscpersentage': request.POST.get( 'sscpersentage' ),
                        'sscpassingyear': request.POST.get( 'sscpassingyear' ),
                        'ssccertificate': request.POST.get( 'ssccer' ), 'hsc': request.POST.get( 'hsc' ),
                        'hsccbord': request.POST.get( 'hsccbord' ),
                        'hsccpersentage': request.POST.get( 'hscpersentage' ),
                        'hscpassingyear': request.POST.get( 'hscpassingyear' ),
                        'hsccertificate': request.POST.get( 'hsccer' ), 'diploma': request.POST.get( 'diploma' ),
                        'diplomabord': request.POST.get( 'diplomabord' ),
                        'diplomapersentage': request.POST.get( 'diplomapersentage' ),
                        'diplomapassingyear': request.POST.get( 'diplomapassingyear' ),
                        'diplomacertificate': request.POST.get( 'diploma' ),
                        'gradution': request.POST.get( 'gradution' ),
                        'gradutionbord': request.POST.get( 'gradutionbord' ),
                        'gradutionpersentage': request.POST.get( 'gradutionpersentage' ),
                        'gradutionpassingyear': request.POST.get( 'gradutionpassingyear' ),
                        'gradutioncertificate': request.POST.get( 'gradutioncer' ),
                        'postgradution': request.POST.get( 'postgradution' ),
                        'postgradutionbord': request.POST.get( 'postgradutionbord' ),
                        'postgradutionpersentage': request.POST.get( 'postgradutionpersentage' ),
                        'postgradutionpassingyear': request.POST.get( 'postgradutionpassingyear' ),
                        'postgradutioncertificate': request.POST.get( 'postgradutioncer' ),
                        'other': request.POST.get( 'other' ),
                        'institude': request.POST.get( 'institute' ),
                        'corsename': request.POST.get( 'corsename' ),
                        'corsepersentage': request.POST.get( 'corsepersentage' ),
                        'corsecertificate': request.POST.get( 'corsecer' ),
                        'father': request.POST.get( 'father' ),
                        'fdob': request.POST.get( 'fdob' ),
                        'fage': request.POST.get( 'fage' ),
                        'fgen': request.POST.get( 'ffgen' ),
                        'frelation': request.POST.get( 'frelstion' ),
                        'mather': request.POST.get( 'mather' ),
                        'mdob': request.POST.get( 'mdob' ),
                        'mage': request.POST.get( 'mage' ),
                        'mgen': request.POST.get( 'mgen' ),
                        'mrelation': request.POST.get( 'mrelstion' ),
                        'cihldren1': request.POST.get( 'children1' ),
                        'c1dob': request.POST.get( 'c1dob' ),
                        'c1age': request.POST.get( 'c1age' ),
                        'c1gen': request.POST.get( 'c1gen' ),
                        'c1relation': request.POST.get( 'c1relstion' ),
                        'children2': request.POST.get( 'children2' ),
                        'c2dob': request.POST.get( 'c2dob' ),
                        'c2age': request.POST.get( 'c2age' ),
                        'c2gen': request.POST.get( 'c2gen' ),
                        'c2relation': request.POST.get( 'c2relstion' ),
                        'companyname': request.POST.get( 'companyname' ),
                        'durationfrom': request.POST.get( 'durationfrom' ),
                        'durationto': request.POST.get( 'durationto' ),
                        'joiningctc': request.POST.get( 'joiningctc' ),
                        'lctc': request.POST.get( 'lctc' ),
                        'twe': request.POST.get( 'twe' )}
        email_html_template = get_template( html_tpl_path ).render( context_data )
        # receiver_email = user
        receiver_email = ['filtrumautocomp0214@gmail.com','abhishekkokate072@gmail.com','hr@filtrum.co.in','ranjitshinde9404@gmail.com']
        email_msg = EmailMessage( 'Welcome to Filtrumautocomp Pvt Ltd',
                                  email_html_template,
                                  settings.APPLICATION_EMAIL,
                                  receiver_email,
                                  reply_to=[settings.APPLICATION_EMAIL]
                                  )
        email_msg.content_subtype = 'html'
        email_msg.send( fail_silently=False )

        # verifymail1(user,c)
        return HttpResponse("data save success as well as send mail successfully")
    return render(request,'form.html')


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filturm'+ '.csv'
    writer = csv.writer(response)
    writer.writerow(['FirstName', 'MiddleName','LastName','Date of Birth','Birth Place','Birth Place Taluka','Birth place District','Age',
                     'Language Known','Gender','Marital Status','Blood Group','Nationality','Religion','Caste','Category','Email Id','Contact No',
                     'Emergency Contact No','Aadhar Card No','Pan Card No','Present Address','Pin Code','Permanent Address','pin code','SSC Bord',
                     'ssc bord','SSC School','ssc percentage','SSC passing year','HSC Bord','HSC school','HSC Percentage','HSC Passing Year','Diploma Stream',
                     'Diploma College','Diploma Percentage','Diploma passing year','Graduation Stream','Graduation college','Graduation Percentage','Gradution Passing Year',
                     'PostGraduation Stream','PostGraduation college','PostGraduation Percentage','PostGradution Passing Year',
                     'Other Courses','institude','Percentage','passing year',
                     'Father /In Laws','Father DOb','Father Age','Father Gender','Relation With Employee',
                     'Mother /In Laws','Mother DOb','Mother Age','Mother Gender','Relation With Employee'
                     'Children 1','Children1 DOb','Children1 Age','Children1 Gender','c1 With Employee',
                     'Children 2','Children2 DOb','Children2 Age','Children2 Gender','c2 With Employee',
                     'Company Name','Duration (From)','Duration (To)','Joining CTC','Last CTC','Total Work Experience'])

    expenses = filturm.objects.all()

    for x in expenses:
        writer.writerow([x.fname,x.mname,x.lname,x.dob,x.birthplace,x.birthplacetaluka,x.bpd,x.age,x.languageknown,x.gender,
                         x.maristetus,x.bloodgroup,x.nationality,x.religion,x.cast,x.category,x.emailid,x.contactno,x.emergencycontactno,
                         x.ak,x.pancardno,x.pad,x.pincode,x.permanentaddress,x.perpincode,x.ssc,x.sscbord,x.sscpersentage,x.sscpassingyear,
                         x.hsc,x.hsccbord,x.hsccpersentage,x.hscpassingyear,x.diploma,x.diplomabord,x.diplomapersentage,x.diplomapassingyear,x.gradution,x.gradutionbord,
                         x.gradutionpersentage,x.gradutionpassingyear,x.postgradution,x.postgradutionbord,x.postgradutionpersentage,x.postgradutionpassingyear,x.other,x.institude
                         ,x.corsename,x.corsepersentage,x.father,x.fdob,x.fage,x.fgen,x.frelation,x.mather,x.mdob,x.mage,x.mgen,x.mrelation,x.cihldren1,x.c1dob,x.c1age,x.c1gen,x.c1relation,
                         x.children2,x.c2dob,x.c2age,x.c2gen,x.c2relation,x.companyname,x.durationfrom,x.durationto,x.joiningctc,x.lctc,x.twe])
    return response

def logdata(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if Login.objects.filter(username=username,password=password).exists():
            return redirect('form1')
        else:
            return HttpResponse("username and password is not match")
    return render(request,'login.html')

def dashbord(request):
    return render(request,'d.html')

def approve(request):
    fulname = fn
    empid=num
    print(empid)
    if request.method=="POST":
        # filturm_id=request.POST.get(pk=id)
        flname = request.POST.get( 'ename' )
        emid = request.POST.get( 'eid' )
        pwd = request.POST.get( "pass" )
        print( flname, emid, pwd )
        em(employeename=flname, ids=emid, pas=pwd).save()

        html_tpl_path = 'userlogin.html'
        context_data = {'name': emid,'pass': pwd}
        email_html_template = get_template( html_tpl_path ).render( context_data )

        receiver_email = user
        email_msg = EmailMessage( 'Welcome to Filtrumautocomp Pvt Ltd',
                                  email_html_template,
                                  settings.APPLICATION_EMAIL,
                                  [receiver_email],
                                  reply_to=[settings.APPLICATION_EMAIL]
                                  )
        email_msg.content_subtype = 'html'
        email_msg.send( fail_silently=False )

        return HttpResponse("send mail to employee with username and password")


    return render(request,'ids.html',{'fname':fulname,'employeeid':empid})

def elogin(request):
    if request.method=="POST":
        eid=request.POST.get('username')
        ename=em.objects.filter(ids=eid).values_list('employeename', flat=True).first()
        print(ename)
        epass=request.POST.get('password')
        if em.objects.filter(ids=eid,pas=epass).exists():
            return render(request,'d.html',{'name':ename})
        else:
            return HttpResponse( ' Id And Not Match' )
    return render(request,'employeelogin.html')

# @permission_classes(permissions.IsAuthenticated,)
def empLeave(request):
    # user=filturm.objects.filter(filturmid=id)
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
        filturm(filturmid=id,appdate=la,appname=ap,leavetype=lt,datefrom=datefrom,dateto=dateto,resumeon=resumeon,leaveday=leaveday,leavebalance=leavebalance,leavereason=leavereason).save()
        return HttpResponse("data save success")
    return render(request,'leavepage.html')


    # user = get_object_or_404(filturm, id=id)//get all DATA
    # user = filturm.objects.filter(id=filturm.filturmid)
    # user = filturm.objects.get(id=filturmid)
    # user=filturm.objects.get(pk=request.filturm.id)
    # print(user)
    # filturm = filturm.objects.get(pk=this_object_id)
    # comment = get_object_or_404(filturm, pk=filturm_id)
    # em = filturm.objects.get(id=em_id)  # getting input from django urls (<int:company_id>)
    # user = filturm.objects.filter(filturm=filturm_id)




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TimeEntry
from django.utils import timezone

@login_required
def punch_in(request):
    if request.method == 'POST':
        TimeEntry.objects.create(user=request.user, start_time=timezone.now())
        return render(request,'punchpage.html')
    return render(request, 'punchpage.html')

@login_required
def punch_out(request):
    if request.method == 'POST':
        time_entry = TimeEntry.objects.filter(user=request.user, end_time__isnull=True).order_by('-start_time').first()
        time_entry.end_time = timezone.now()
        time_entry.save()
        return redirect('login')
    return render(request, 'punchpage.html')


def punchList(request):
    a=TimeEntry.objects.all()
    context={
        'a':a
    }
    return render(request,'punchList.html',context)
