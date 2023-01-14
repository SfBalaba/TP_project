from django.contrib import admin
from .models import Home, Demand, Skills, Geography

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    pass

@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    pass

@admin.register(Geography)
class GeographyAdmin(admin.ModelAdmin):
    pass

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass
