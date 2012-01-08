#EXAMPLE
#from main.models import *
#from django.contrib import admin

#class WorkoutInline(admin.StackedInline):
    #model = WorkoutInstance
    #extra = 3

#class ProfileAdmin(admin.ModelAdmin):
    #pass
    ##fieldsets = [
        ##(None, {'fields':['event']}),
        ##('Birthday', {'fields':['birthday'], 'classes':['collapse']}),
    ##]

#class CycleAdmin(admin.ModelAdmin):
    #list_display = ('name', 'date_start', 'date_stop', 'user')
#class MicroCycleAdmin(CycleAdmin):
    #pass
#class MesoCycleAdmin(CycleAdmin):
    #pass
#class MacroCycleAdmin(CycleAdmin):
    #pass

#class WorkoutInstanceAdmin(admin.ModelAdmin):
    #list_display = ('name', 'metric', 'metric_unit', 'datetime_start', 'datetime_stop')




#admin.site.register(UserProfile, ProfileAdmin)
#admin.site.register(Block)
#admin.site.register(Workout)
#admin.site.register(WorkoutInstance, WorkoutInstanceAdmin)
#admin.site.register(MacroCycle, MacroCycleAdmin)
#admin.site.register(MesoCycle, MesoCycleAdmin)
#admin.site.register(MicroCycle, MicroCycleAdmin)
