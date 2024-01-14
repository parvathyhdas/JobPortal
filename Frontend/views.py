from django.shortcuts import render,redirect
from Backend.models import JobDB,CompanyDB,JobCategoryDB
from Frontend.models import RegisterDB,UserProfileDB,ContactDB,ApplicationDB
from django.contrib import messages
from django.db.models import Q
from django.core.files.storage.filesystem import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import send_mail
from MainProject import settings


# Create your views here.
def homePage(request):
    data = JobDB.objects.all()
    cat = JobCategoryDB.objects.all()
    return render(request,"home.html",{'data':data,'cat':cat})

def joblisting(request):
    data = JobDB.objects.all()
    comp = CompanyDB.objects.all()
    detail = ApplicationDB.objects.all()
    return render(request,"Joblist.html",{'data':data,'detail':detail,'comp':comp})

def SingleJob(request,dataid):
    data = JobDB.objects.filter(id=dataid)
    detail = UserProfileDB.objects.all()
    job = ApplicationDB.objects.all()
    return render(request,"singleJobpage.html",{'data':data,
                                                'detail':detail,'job':job})

def singleCompany(request,dataid):
    data = CompanyDB.objects.filter(id=dataid)
    return render(request,"single_companyPage.html",{'data':data})

def loginPage(request):
    return render(request,"loginPage.html")

def saveRegistration(request):
    if request.method == "POST":
        em = request.POST.get("email")
        un = request.POST.get("username")
        pwd = request.POST.get("pwd")
        cpwd = request.POST.get("cpwd")
        if pwd == cpwd:
            obj = RegisterDB(Email=em,Username=un,Password=pwd,ConformPassword=cpwd)
            obj.save()
            messages.success(request, "Registered successfully")
            return redirect(loginPage)
        else:
            messages.error(request, "Password and confirm password are not matched")
            return redirect(loginPage)

def UserLogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if RegisterDB.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username'] = un
            request.session['Password'] = pwd
            messages.success(request,"Login successfully")
            return redirect(homePage)
        else:
            messages.error(request, "Invalid username or password ")
            return redirect(loginPage)
    return redirect(loginPage)

def UserLogout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Logout successfully")
    return redirect(UserLogin)


def contactPage(request):
    return render(request,"contact.html")

def aboutPage(request):
    return render(request,"about.html")

def Jobfiltered(request,jobtype):
    job = JobDB.objects.filter(JobType=jobtype)
    data = JobDB.objects.all()
    return render(request,"jobfiltered.html",{'job':job,'data':data})

def profile(request):
    detail = UserProfileDB.objects.all()
    return render(request,"profile.html",{'detail':detail})


def saveProfile(request):
    if request.method == "POST":
        na =request.POST.get("name")
        fna =request.POST.get("fulname")
        em =request.POST.get("email")
        mo =request.POST.get("mobile")
        img = request.FILES["image"]
        res =request.FILES["resume"]
        wo =request.POST.get("work")
        cn = request.POST.get("cname")
        des = request.POST.get("des")
        da = request.POST.get("jdate")
        sa = request.POST.get("salary")
        np = request.POST.get("nperiod")
        edu = request.POST.get('edu')
        uni = request.POST.get('uni')
        yr = request.POST.get('yr')
        si = request.POST.get("skills")
        obj = UserProfileDB(Name=na,FullName=fna,Email=em,Mobile=mo,Resume=res,WorkStatus=wo,ProfileImage=img,
                            CurrentCompanyName=cn,Designation=des,JoiningDate=da,CurrentSalary=sa,NoticePeriod=np,
                            Education=edu,University=uni,PassoutYear=yr,Skills=si)
        obj.save()
        return redirect(profile)

def displayProfile(request,dataid):
    pro = UserProfileDB.objects.filter(id=dataid)
    apply = ApplicationDB.objects.all()
    return render(request,"displayProfile.html",{'pro':pro,'apply':apply})

def editProfile(request,dataid):
    data = UserProfileDB.objects.get(id=dataid)
    return render(request, "EditProfile.html", {'data':data})



def updateProfile(request,dataid):
    if request.method == "POST":
        na =request.POST.get("name")
        fna = request.POST.get("fulname")
        em =request.POST.get("email")
        mo =request.POST.get("mobile")

        wo =request.POST.get("work")
        cn = request.POST.get("cname")
        des = request.POST.get("des")
        da = request.POST.get("jdate")
        sa = request.POST.get("salary")
        np = request.POST.get("nperiod")
        edu = request.POST.get('edu')
        uni = request.POST.get('uni')
        yr = request.POST.get('yr')
        si = request.POST.get("skills")
        try:
            img = request.FILES["image"]
            res = request.FILES["resume"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
            resfile = fs.save(res.name,res)
        except MultiValueDictKeyError:
            file = UserProfileDB.objects.get(id=dataid).ProfileImage
            resfile = UserProfileDB.objects.get(id=dataid).Resume
        UserProfileDB.objects.filter(id=dataid).update(Name=na,FullName=fna,Email=em,Mobile=mo,Resume=resfile,WorkStatus=wo,ProfileImage=file,
                                                       CurrentCompanyName=cn, Designation=des, JoiningDate=da,
                                                       CurrentSalary=sa, NoticePeriod=np,
                                                       Education=edu, University=uni, PassoutYear=yr, Skills=si
                                                       )
        return redirect(profile)



def search_by_two_fields(request):
    if request.method == "POST":
        #
        # query = request.POST.get('jobtitle')
        # if query:
        #     results = JobDB.objects.filter(JobTitle=query)
        # else:
        #     results = []
        # return render(request, 'search_results.html', {'results': results})

        search_term = request.POST.get('jobtitle', 'loc')  # Get the search term from the query parameters

        # Use Q objects to create a complex query
        query = Q(JobTitle__icontains=search_term) | Q(Location__icontains=search_term)

        # Use the created query in the filter method
        results = JobDB.objects.filter(query)

        context = {
            'results': results,
            'search_term': search_term,
        }

        return render(request, 'search_results.html', context)

def contactSave(request):
    if request.method == "POST":
        me = request.POST.get("message")
        na = request.POST.get("name")
        em = request.POST.get("email")
        su = request.POST.get("subject")
        obj = ContactDB(Message=me,Name=na,Email=em,Subject=su)
        obj.save()
        messages.success(request, "Message sent successfully")
        return redirect(contactPage)

def companyList(request):
    comp = CompanyDB.objects.all()
    return render(request,"companylist.html",{'comp':comp})


def saveApplication(request):
    if request.method == "POST":
        na = request.POST.get("name")
        fna = request.POST.get("fulname")
        mob = request.POST.get("mob")
        em = request.POST.get("email")
        res = request.FILES["resume"]
        job = request.POST.get("job")
        cn = request.POST.get("cname")
        obj = ApplicationDB(Name=na,FullName=fna,Mobile=mob,Email=em,Resume=res,JobTitle=job,CompanyName=cn)
        # query = request.POST.get('jobtitle')
        search_term = request.POST.get('job')
        search_term1 = request.POST.get('name')
        search_term3 = request.POST.get('cname')

        # results = ApplicationDB.objects.filter(JobTitle__icontains=query)
        query = Q(JobTitle__icontains=search_term) & Q(Name__icontains=search_term1) & Q(CompanyName__icontains=search_term3)
        results = ApplicationDB.objects.filter(query)
        if results.exists():
            messages.error(request, "Application Already Submitted ")
            return redirect(joblisting)
        else:
            obj.save()
            subject = 'Job Submission'
            message = 'Job Submitted Successsfully'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [em]

            send_mail(subject, message, from_email, recipient_list)

            messages.success(request,"Application Submitted  successfully")
            return redirect(joblisting)

def filterJobCategory(request,cat_name):
    category = JobDB.objects.filter(JobCategory=cat_name)
    return render(request,"jobfiltered.html",{'category':category})

def search_company(request):
    if request.method == "POST":

        query = request.POST.get('cname')
        if query:
            results = CompanyDB.objects.filter(CompanyName=query)
        else:
            results = []
        return render(request, 'search_company.html', {'results': results})



