from django.urls import path
from Frontend import views
from django.contrib.auth import views as auth_views

urlpatterns = [path('homePage/',views.homePage,name="homePage"),
                path('joblisting/',views.joblisting,name="joblisting"),
                path('SingleJob/<int:dataid>/',views.SingleJob,name="SingleJob"),
                path('singleCompany/<int:dataid>/',views.singleCompany,name="singleCompany"),
                path('loginPage/',views.loginPage,name="loginPage"),
                path('saveRegistration/',views.saveRegistration,name="saveRegistration"),
                path('',views.UserLogin,name="UserLogin"),
                path('UserLogout/',views.UserLogout,name="UserLogout"),
                path('contactPage/',views.contactPage,name="contactPage"),
                path('aboutPage/',views.aboutPage,name="aboutPage"),
                path('Jobfiltered/<jobtype>/',views.Jobfiltered,name="Jobfiltered"),
                path('profile/',views.profile,name="profile"),
                path('saveProfile/',views.saveProfile,name="saveProfile"),
                path('displayProfile/<int:dataid>/',views.displayProfile,name="displayProfile"),
                path('editProfile/<int:dataid>/',views.editProfile,name="editProfile"),
                path('updateProfile/<int:dataid>/',views.updateProfile,name="updateProfile"),
                path('search_by_two_fields/',views.search_by_two_fields,name="search_by_two_fields"),
                path('contactSave/',views.contactSave,name="contactSave"),
                path('companyList/',views.companyList,name="companyList"),
                path('saveApplication/',views.saveApplication,name="saveApplication"),
                path('filterJobCategory/<cat_name>/',views.filterJobCategory,name="filterJobCategory"),
                path('search_company/',views.search_company,name="search_company"),

               ]