from django.contrib import admin
from models import Project,RfpCampaign,Review,File_Test,ProposedReviewer,BudgetLine
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#Register your models here.

#InLine forms
class BudgetLineInline(admin.TabularInline):
    model = BudgetLine

class ProposedReviewerInLine(admin.TabularInline):
    model = ProposedReviewer

class RfpCampaignInline(admin.TabularInline):
    model = RfpCampaign

class ReviewInLine(admin.TabularInline):
    model = Review

class ProjectInLine(admin.TabularInline):
    model = Project

#Change forms
def valid_reviewer(obj,id,stuff):
    print ('OKAY')

def get_user_fullname(obj):
    if obj.user:
        v = (str(obj.user.first_name) + " " + str(obj.user.last_name))
    else:
        v = "No User"
    return v
get_user_fullname.short_description = 'User_Full_Name'

def get_user_email(obj):
    if obj.user:
        v = (str(obj.user.email))
    else:
        v = "No User"
    return v
get_user_email.short_description = "User_Email"

def get_user_institution(obj):
    if obj.user:
        v = (str(obj.user.userprofile.insitute_research_unit))
    else:
        v = "No User"
    return v
get_user_institution.short_description = "User_Research_Unit"

def get_user_rfp_year(obj):
    if obj.user:
        v = (str(obj.rfp.year))
    else:
        v = "No Category"
    return v
get_user_rfp_year.short_description = "Category_year"

def file_link(self):
        if self.document:
            return (self.document.url)
        else:
            return "No attachment"

#Export and import for Project, Review, RFP, BudgetLine and Reviewers
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ["name","requested_amount","rfp",get_user_rfp_year,get_user_fullname, get_user_email]
    search_fields = ["name","rfp"]
    list_filter = ["rfp","user","name","rfp__year","user__email"]

    inlines = [
        BudgetLineInline,
        ProposedReviewerInLine,
        ReviewInLine,
    ]

class ReviewOptions(ImportExportModelAdmin):
    list_display = ["project","user"]
    search_fields = []
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
    list_display = ["year","name"]
    list_filter = ["year"]
    search_fields = ['name']

class BudgetLineAdmin(ImportExportModelAdmin):
    list_display = ["item", "amount", "category", "project"]
    list_filter = ["category", "project"]
    search_fields = ["category", "project"]
    ordering = ["project","category"]

class ProposedReviewerAdmin(ImportExportModelAdmin):
    list_display = ["project", "last_name", "first_name", "email", "institution"]
    list_filter = ["project","institution"]
    search_fields = ["project","email","last_name","first_name"]
    ordering = ["project","last_name"]
    actions = [valid_reviewer]

admin.site.register(BudgetLine,BudgetLineAdmin)
admin.site.register(ProposedReviewer,ProposedReviewerAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(RfpCampaign, RfpCampaignAdmin)
admin.site.register(Review,ReviewOptions )
admin.site.register(File_Test)
