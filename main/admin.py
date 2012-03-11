from main.models import *
from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
    pass

##class WorkoutInline(admin.StackedInline):
    ###list_display('name', 'metric')
    ##model = WorkoutInstance
    ##extra = 3

#class ProfileAdmin(admin.ModelAdmin):
    #pass
    ##fieldsets = [
        ##(None, {'fields':['event']}),
        ##('Birthday', {'fields':['birthday'], 'classes':['collapse']}),
    ##]

#class CycleAdmin(admin.ModelAdmin):
    #list_display = ("name", "date_start", "date_stop", "date_diff")

#class MicroCycleAdmin(CycleAdmin):
    #pass
#class MesoCycleAdmin(CycleAdmin):
    #pass
#class MacroCycleAdmin(CycleAdmin):
    #pass
#class WorkoutAdmin(admin.ModelAdmin):
    #list_display = ('name', 'metric')
#class WorkoutInstanceAdmin(admin.ModelAdmin):
    #list_display = ("workout", "date_start", "date_stop", 'value_unit', 'ordering')




#admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Course)
admin.site.register(ProblemSet)
admin.site.register(Question)
admin.site.register(QuestionStats)

