from django.contrib import admin

from jobs_app.models import jobsmodel , employeemodel ,workmodel,jobselectormodel
# from jobs_app.models import  servicmodel

admin.site.register(jobsmodel)
admin.site.register(employeemodel)
admin.site.register(workmodel)
admin.site.register(jobselectormodel)
# admin.site.register(servicmodel)
