from django.contrib import admin
from models import Project,RfpCampaign,Review,RequestForProposal,File_Test
# Register your models here.

class RfpCampaignInline(admin.TabularInline):
    model = RfpCampaign

class ReviewInLine(admin.TabularInline):
    model = Review

class RfpCampaignAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["year","name","request_for_proposal"]
    list_filter = ["year"]
    search_fields = ['request_for_proposal__name']

class RequestForProposalAdmin(admin.ModelAdmin):
    search_field = ["name"]
    list_display = ["name"]
    inlines = [
       RfpCampaignInline,
    ]

class ProjectAdmin(admin.ModelAdmin):
    search_field = ["name"]
    list_display = ["name","user", "rfp", "requested_amount"]
    inlines = [
        ReviewInLine,
    ]

admin.site.register(Project,ProjectAdmin)
admin.site.register(RfpCampaign, RfpCampaignAdmin)
admin.site.register(Review)
admin.site.register(RequestForProposal, RequestForProposalAdmin)
admin.site.register(File_Test)