from django.urls import path
from . import views

urlpatterns=[

    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('education/',views.education,name='education'),
    path('skills/',views.skills,name='skills'),
    path('certificates/',views.certificates,name='certificates'),
    path('contact/',views.contact,name='contact'),
]