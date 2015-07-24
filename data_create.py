__author__ = 'Sylvestre'
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from user_profile.models import UserProfile
from rfp.models import RfpCampaign,Project,Review,ProposedReviewer,BudgetLine

import time
import datetime
import random

def date_convert(date):
    t = time.strptime(date, "%m/%d/%Y")
    return datetime.date(year=t.tm_year, month=t.tm_mon, day=t.tm_mday)

def pick_random_pi():
    g = Group.objects.get(name='Principal_Investigator')
    users = g.user_set.all()
    list_of_id = list()
    for u in users:
        list_of_id.append(u.id)
    l = len(list_of_id)
    n = random.randrange(1,l,1)
    return User.objects.get(id=list_of_id[n])

def pick_random_reviewer():
    g = Group.objects.get(name='Reviewer')
    users = g.user_set.all()
    list_of_id = list()
    for u in users:
        list_of_id.append(u.id)
    l = len(list_of_id)
    n = random.randrange(1,l,1)
    return User.objects.get(id=list_of_id[n])

def pick_random_rfp():
    rfp_list = RfpCampaign.objects.all()
    list_of_id = list()
    for rfp in rfp_list:
        list_of_id.append(rfp.id)
    l = len(list_of_id)
    n = random.randrange(1,l,1)
    return RfpCampaign.objects.get(id=list_of_id[n])

def pick_random_project():
    project_list = Project.objects.all()
    list_of_id = list()
    for p in project_list:
        list_of_id.append(p.id)
    l = len(list_of_id)
    n = random.randrange(1,l,1)
    return Project.objects.get(id=list_of_id[n])

def random_type():
    type = (
        ('ADMIN_PROPOSED','Proposed by Admin'),
        ('USER_PROPOSED', 'Proposed by User'),
        ('USER_EXCLUDED', 'Excluded Reviewer'),
        ('BOARD_SUGGESTED', 'Proposed by Board Member')
    )

    i = random.randrange(0,len(type) ,1)
    return type[i][0]

def create_users():
    username = 'user' + str(random.randrange(1,850,1))
    email = username + str('@mail.com')
    pwd = 'FRC@2015'
    first_name = 'first_' + str(username)
    last_name = 'last_' + str(username)

    if not User.objects.filter(username = username).exists():
           user = User.objects.create_user(username,email,pwd)
           user.first_name = first_name
           user.last_name = last_name
           user.save()

           up = UserProfile.objects.get(user=user)
           up.organization = 'Univeristy of Science'
           up.insitute_research_unit = 'Institute of Chemistry'
           up.address = '123 Main Street'
           up.city = 'The City'
           up.state = 'NJ'
           up.zip = '07302'
           up.country = 'USA'
           up.save()

           i = random.randrange(1,3,1)
           if i == 1:
                   g = Group.objects.get(name='Principal_Investigator')
                   g.user_set.add(user)
                   print('Added to PI group')
           else:
                   g = Group.objects.get(name='Reviewer')
                   g.user_set.add(user)
                   print('Added to Reviewer group')

           return user
    else:
        create_users()

def create_rfp(filename):
    with open(filename,'r') as file:
        data = file.readline()

        if data.startswith('#'):
           data= file.readline()

        for data in file:
           data = data.split(',')
           rfp = RfpCampaign(name=data[0],
                             category=data[1],
                             year=data[2],
                             starting_date = date_convert(data[3]),
                             deadline = date_convert(data[4]),
                             status = data[5],
                             instructions=data[6],
                             project_questions = data[7],
                             review_questions = data[8],)
           rfp.save()

def create_reviews(project,status):
    """
    Create a review for the specified project with the indicated status.
    :param project: Project
    :param status: str
    :param n: int
    :return: Review
    """
    user = pick_random_reviewer()
    if status == 'completed':
        rating = 'A'
        note = random.randrange(0,6,1)
        custom_0 = 'Very nice project!!!'
        review = Review( user = user,
            project = project,
            rating = rating,
            status = status,
            custom_0 = custom_0,
            note = note,
        )
    else:
        rating = ''
        custom_0 = ''
        review = Review( user = user,
            project = project,
            rating = rating,
            status = status,
            custom_0 = custom_0,
        )

    review.save()
    create_proposed_reviewer(review)

    return review

def create_proposed_reviewer(r):
    """
    Create the Proposed Reviewer correspionding to the Reviews for a Project.
    Type of Reviewer is selected randomly amon Type_choices on ProposedReviewer Model.
    :param review: Review
    :return: ProposedReviewer
    """
    type = random_type()
    pr = ProposedReviewer(
                         first_name = r.user.first_name,
                         last_name = r.user.last_name,
                         project= r.project,
                         email = r.user.email,
                         institution = r.user.userprofile.organization,
                         address = r.user.userprofile.address,
                         city = r.user.userprofile.city,
                         state = r.user.userprofile.state,
                         postcode = r.user.userprofile.zip,
                         country = r.user.userprofile.country,
                         type = type
                         )
    pr.save()
    return pr

def create_project(status,rfp,pi):
    """
    Create a project for the with PI as author and rfp as Request for Proposel).
    :param status: str
    :param rfp: RfpCampaign
    :param pi: User
    :param granted: Bool
    :return: Project
    """

    project_name = 'Project' + str(random.randrange(1,250000,10))
    project_start_date = '01/01/2015'
    project_duration = 36
    ending_date = '01/01/2018'
    requested_amount = random.randrange(20000,250000,100)
    if status == 'granted':
        awarded_amount = random.randrange(10000,requested_amount,10)
    else:
        awarded_amount = 0
    keywords = 'Keywords1 Keywords-2 Keywords,%45&*)'
    abstract = 'Abstract'
    status = status

    # Create the project
    p = Project(
                                rfp=rfp,
                                name=project_name,
                                user=pi,
                                starting_date=date_convert(project_start_date),
                                project_duration=project_duration,
                                ending_date=date_convert(ending_date),
                                requested_amount=requested_amount,
                                awarded_amount=awarded_amount,
                                keywords=keywords,
                                abstract=abstract,
                                status=status,
                              )
    p.save()

    if p.rfp.status == 'closed':                                   #If Request for porposal is closed:

        for i in range(1,5,1):                              #Create 4 completed reviews
            create_reviews(p,'completed')

        for i in range(1,3,1):                              #Create 2 pending reviews
            create_reviews(p,'pending')

        for i in range(1,3,1):                              #Create 2 refused reviews
            create_reviews(p,'refused')

        for i in range(1,4,1):                              #Create 2 accepted reviews
            create_reviews(p,'accepted')

    else:                                                    #If Request for porposal is open:
         for i in range(1,5,1):                              #Create 4 completed reviews
            create_reviews(p,'pending')

         for i in range(1,5,1):                              #Create 4 accepted reviews
            create_reviews(p,'accepted')

                                                                    #Create 6 BL per project
    item = 'Test_item'
    category_list = ('HR', 'EQ', 'OC')

    for j in range(1,7,1):
            i = random.randrange(0,len(category_list),1)
            category = category_list[i]                             #Pick up a BL category

            if i == 0:                                               #If HR
                duration = 36
                monthly_salary = 2500
                amount = duration * monthly_salary
            else:                                                    #If EQ or OC
                duration = 0
                monthly_salary = 0
                amount = random.randrange(10000,1000000,1000)
            bl = BudgetLine(
                project = p,
                item = item,
                category = category,
                duration = duration,
                monthly_salary = monthly_salary,
                amount = amount,
            )
            bl.save()

    print('Project created : ')
    print p
    return p

def create_group():
    group_list = ('Principal_Investigator','Reviewer','Scientific_board')
    for g in group_list:
        group = Group.objects.create(name=g)
        print(group)

def ini_data():
    """
    Create Users,RfpCampaign,Project,Review,ProposedReviewer.
    :return:
    """
    print("Let's populate this app!")
    filename = 'rfp_data.csv'

    create_group()
    create_rfp(filename)

    for i in range(1,200,1):
        u = create_users()
        print(u)

    g = Group.objects.get(name='Principal_Investigator')
    pi_list = g.user_set.all()
    rfp_list = RfpCampaign.objects.all()
                                                                    #Create the Porjects
    for pi in pi_list:
        for rfp in rfp_list:
            if rfp.status == 'closed':
                create_project('draft',rfp,pi)

                i = random.randrange(1,3,1)
                if i < 2 :
                    create_project('granted',rfp,pi)
                else:
                    create_project('not_granted',rfp,pi)

            if rfp.status == 'open':
                 create_project('draft',rfp,pi)
                 create_project('submitted',rfp,pi)

    print('Popualted!')

#ini_data()

create_group()