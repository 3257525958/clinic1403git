from django.contrib import admin

from reserv_app.models import reservemodel,leavemodel,reservemodeltest,neursemodel,neursetestmodel

admin.site.register(reservemodel)
admin.site.register(reservemodeltest)
admin.site.register(leavemodel)
admin.site.register(neursemodel)
admin.site.register(neursetestmodel)
