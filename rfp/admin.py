from django.contrib import admin
from models import Project,RfpCampaign,Review,RequestForProposal,File_Test,ProposedReviewer
# Register your models here.

class RfpCampaignInline(admin.TabularInline):
    model = RfpCampaign

class ReviewInLine(admin.TabularInline):
    model = Review

class ProjectInLine(admin.TabularInline):
    model = Project

class ReviewOptions(admin.ModelAdmin):
    list_display = ["name","project","user"]
    search_fields = ["name"]
    list_filter = ["user","project"]
    change_list_filter_template = "admin/filter_listing.html"

    # define the raw_id_fields
    raw_id_fields = ('user','project',)
    # define the related_lookup_fields
    related_lookup_fields = {
        'user': ['related_user'],
        'project': ['related_project'],
    }


class RfpCampaignAdmin(admin.ModelAdmin):
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
    list_display = ["name","user", "rfp", "requested_amount"]
    search_fields = ["name"]
    inlines = [
        ReviewInLine,
    ]


admin.site.register(ProposedReviewer)
admin.site.register(Project,ProjectAdmin)
admin.site.register(RfpCampaign, RfpCampaignAdmin)
admin.site.register(Review,ReviewOptions )
admin.site.register(RequestForProposal, RequestForProposalAdmin)
admin.site.register(File_Test)
