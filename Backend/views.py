from django.shortcuts import render,redirect
from Backend.models import CompanyDB,JobDB,JobCategoryDB
from Frontend.models import UserProfileDB,ApplicationDB,RegisterDB
from django.core.files.storage.filesystem import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.
def indexPage(request):
    return render(request,"index.html")

def companyReg(request):
    return render(request,"companyRegistration.html")

def saveCompany(request):
    if request.method == "POST":
        cn = request.POST.get("cname")
        mb = request.POST.get("mobile")
        em = request.POST.get("email")
        pwd = request.POST.get("password")
        ln = request.POST.get("location")
        des = request.POST.get("description")
        img = request.FILES["image"]
        ad = request.POST.get("address")
        we = request.POST.get("website")
        do = request.POST.get("domain")
        obj = CompanyDB(CompanyName=cn,ContactNumber=mb,CompanyEmail=em,CompanyPassword=pwd,CompanyLocation=ln,Description=des,Image=img,Address=ad,Website=we,Domain=do)
        obj.save()
        messages.success(request,"Company Saved successfully..")
        return redirect(companyReg)

def addJob(request):
    comp = CompanyDB.objects.all()
    cat = JobCategoryDB.objects.all()
    return render(request,"addJob.html",{'comp':comp,'cat':cat})

def saveJob(request):
    if request.method == "POST":
        cn = request.POST.get("cname")
        jn = request.POST.get("jname")
        em = request.POST.get("email")
        pd = request.POST.get("posted")
        cg = request.POST.get("closing")
        bd = request.POST.get("description")
        ps = request.POST.get("skills")
        lo = request.POST.get("location")
        jt = request.POST.get("jobtype")
        ex = request.POST.get("experience")
        va = request.POST.get("vacancy")
        sa = request.POST.get("salary")
        web = request.POST.get("website")
        cat = request.POST.get("catname")
        img = request.FILES["image"]
        obj = JobDB(CompanyName=cn, JobTitle=jn, CompanyEmail=em, PostedOn=pd, ClosingOn=cg, BriefDescription=bd, PreferredSkills=ps,Image=img,
                    Location=lo,JobType=jt,Experience=ex,Salary=sa,Vacancy=va,Website=web,JobCategory=cat)
        obj.save()
        messages.success(request, "Job Saved successfully..")
        return redirect(addJob)

def displayCompany(request):
    comp = CompanyDB.objects.all()
    return render(request,"displayCompany.html",{'comp':comp})

def displayJob(request):
    job = JobDB.objects.all()
    return render(request,"displayJobs.html",{'job':job})

def editCompany(request,dataid):
    data = CompanyDB.objects.get(id=dataid)
    return render(request,"editCompany.html",{'data':data})

def updateCompany(request,dataid):
    if request.method == "POST":
        cn = request.POST.get("cname")
        mb = request.POST.get("mobile")
        em = request.POST.get("email")
        pwd = request.POST.get("password")
        ln = request.POST.get("location")
        des = request.POST.get("description")
        ad = request.POST.get("address")
        we = request.POST.get("website")
        do = request.POST.get("domain")
        try:
            img = request.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CompanyDB.objects.get(id=dataid).Image
        CompanyDB.objects.filter(id=dataid).update(CompanyName=cn, ContactNumber=mb, CompanyEmail=em, CompanyPassword=pwd, CompanyLocation=ln,
                  Description=des, Image=file,Address=ad,Website=we,Domain=do)
        messages.success(request, "Company updated successfully..")
        return redirect(displayCompany)

def deleteCompany(request,dataid):
    data = CompanyDB.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Company delete successfully..")
    return redirect(displayCompany)

def editJob(request,dataid):
    data = JobDB.objects.get(id=dataid)
    comp = CompanyDB.objects.all()
    cat = JobCategoryDB.objects.all()
    return render(request,"editJobs.html",{'data':data,'comp':comp,'cat':cat})

def updateJob(request,dataid):
    if request.method == "POST":
        cn = request.POST.get("cname")
        jn = request.POST.get("jname")
        em = request.POST.get("email")
        pd = request.POST.get("posted")
        cg = request.POST.get("closing")
        bd = request.POST.get("description")
        ps = request.POST.get("skills")
        lo = request.POST.get("location")
        jt = request.POST.get("jobtype")
        ex = request.POST.get("experience")
        va = request.POST.get("vacancy")
        sa = request.POST.get("salary")
        web = request.POST.get("website")
        cat = request.POST.get("catname")
        try:
            img = request.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = JobDB.objects.get(id=dataid).Image
        JobDB.objects.filter(id=dataid).update(CompanyName=cn, JobTitle=jn, CompanyEmail=em, PostedOn=pd, ClosingOn=cg, BriefDescription=bd, PreferredSkills=ps,Image=file,
                                               Location=lo,JobType=jt,Experience=ex,Salary=sa,Vacancy=va,Website=web,JobCategory=cat)
        messages.success(request, "Job updated successfully..")
        return redirect(displayJob)

def deleteJob(request,dataid):
    data = JobDB.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Job deleted successfully..")
    return redirect(displayJob)

def adminLoginPage(requset):
    return render(requset,"adminLogin.html")

def adminLogin(request):
    if request.method == "POST":
        un =request.POST.get("name")
        pwd =request.POST.get("password")
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pwd)
            if user is not None:
                login(request,user)
                request.session['username'] = un
                request.session['password'] = pwd
                messages.success(request, "Login sucessfully")
                return redirect(indexPage)
            else:
                messages.error(request, "Invalid username or password")
                return redirect(adminLoginPage)
        else:
            return redirect(adminLoginPage)

def adminLogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout successfully..")
    return redirect(adminLoginPage)

def jobCategory(request):
    return render(request,"addJobCategory.html")

def saveJobCategory(request):
    if request.method == "POST":
        na = request.POST.get("name")
        im = request.FILES["image"]
        obj = JobCategoryDB(JobCategory=na,CategoryImage=im)
        obj.save()
        messages.success(request, "saved successfully..")
        return redirect(jobCategory)

def applicant_list(request):
    data = UserProfileDB.objects.all()
    return render(request,"list_applicant.html",{'data':data})

def deleteApplicant(request,dataid):
    data = UserProfileDB.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "applicant deleted successfully..")
    return redirect(applicant_list)


def company_login(request):
    return render(request,"company_login.html")


def CompanyLogin(request):
    if request.method == "POST":
        un = request.POST.get('name')
        pwd = request.POST.get('password')
        if CompanyDB.objects.filter(CompanyName=un,CompanyPassword=pwd).exists():
            request.session['CompanyName'] = un
            request.session['CompanyPassword'] = pwd
            messages.success(request,"Login successfully")
            return redirect(indexPage)
        else:
            messages.error(request, "Invalid username or password ")
            return redirect(company_login)
    return redirect(company_login)

def CompanyLogout(request):
    del request.session['CompanyName']
    del request.session['CompanyPassword']
    return redirect(CompanyLogin)

def displayJobApplictions(request):
    comp = CompanyDB.objects.all()
    job = ApplicationDB.objects.all()
    return render(request,"display_jobapplications.html",{'comp':comp,'job':job})


def deleteApplication(request,dataid):
    data = ApplicationDB.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "applicant deleted successfully..")
    return redirect(displayJobApplictions)

def filterJobApplicants(request):
    data = ApplicationDB.objects.all()
    job = ApplicationDB.objects.all()
    return render(request,"filter_jobapplicants.html",{'data':data,'job':job})

def deletefilterjobs(request,dataid):
    data =ApplicationDB.objects.filter(id=dataid)
    data.delete()
    return redirect(filterJobApplicants)

def filterCompany(request):
    data = CompanyDB.objects.all()
    return render(request,"filterCompany.html",{'data':data})

def companyJob(request):
    job = JobDB.objects.all()
    return render(request,"companyJob.html",{'job':job})

def displayRegisteredJobseeker(request):
    data = RegisterDB.objects.all()
    return render(request,"display_registered_jobseeker.html",{'data':data})

def editRegisteredApplicant(request):
    return render(request,"editApplicant.html")

def updateRegisteredApplicant(request):
    if request.method == "POST":
        st = request.POST.get("status")
        RegisterDB(status=st)
        return redirect(displayRegisteredJobseeker)


