from django.urls import path
from Backend import views
from django.contrib.auth import views as auth_views

urlpatterns = [
                path('indexPage/',views.indexPage,name="indexPage"),
                path('companyReg/',views.companyReg,name="companyReg"),
                path('saveCompany/',views.saveCompany,name="saveCompany"),
                path('addJob/',views.addJob,name="addJob"),
                path('saveJob/',views.saveJob,name="saveJob"),
                path('displayCompany/',views.displayCompany,name="displayCompany"),
                path('displayJob/',views.displayJob,name="displayJob"),
                path('editCompany/<int:dataid>/',views.editCompany,name="editCompany"),
                path('updateCompany/<int:dataid>/',views.updateCompany,name="updateCompany"),
                path('deleteCompany/<int:dataid>/',views.deleteCompany,name="deleteCompany"),
                path('editJob/<int:dataid>/',views.editJob,name="editJob"),
                path('updateJob/<int:dataid>/',views.updateJob,name="updateJob"),
                path('deleteJob/<int:dataid>/',views.deleteJob,name="deleteJob"),
                path('adminLoginPage/',views.adminLoginPage,name="adminLoginPage"),
                path('adminLogin/',views.adminLogin,name="adminLogin"),
                path('adminLogout/',views.adminLogout,name="adminLogout"),
                path('jobCategory/',views.jobCategory,name="jobCategory"),
                path('saveJobCategory/',views.saveJobCategory,name="saveJobCategory"),
                path('applicant_list/',views.applicant_list,name="applicant_list"),
                path('deleteApplicant/<int:dataid>/',views.deleteApplicant,name="deleteApplicant"),
                path('company_login/',views.company_login,name="company_login"),
                path('CompanyLogin/',views.CompanyLogin,name="CompanyLogin"),
                path('CompanyLogout/',views.CompanyLogout,name="CompanyLogout"),
                path('displayJobApplictions/',views.displayJobApplictions,name="displayJobApplictions"),
                path('deleteApplication/<int:dataid>/',views.deleteApplication,name="deleteApplication"),
                path('filterJobApplicants/',views.filterJobApplicants,name="filterJobApplicants"),
                path('deletefilterjobs/<int:dataid>/',views.deletefilterjobs,name="deletefilterjobs"),
                path('filterCompany/',views.filterCompany,name="filterCompany"),
                path('companyJob/',views.companyJob,name="companyJob"),


               path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"), name='password_reset'),
               path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
               path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
                    name='password_reset_confirm'),
               path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
               ]