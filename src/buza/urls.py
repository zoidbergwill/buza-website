import django.contrib.auth.urls
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views import generic

from buza import views


urlpatterns = [
    path('', generic.RedirectView.as_view(pattern_name='question-list'), name='home'),

    # Admin paths
    url(r'^admin/', admin.site.urls),

    # user related paths
    url(r'^register/$', views.UserCreate.as_view(), name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    path(r'users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    # subject related paths
    path('subjects/<int:pk>/', views.SubjectDetail.as_view(), name='subject-detail'),
    path(
        'subjects/my-subjects/<int:pk>/',
        views.UserSubjectsView.as_view(),
        name='my-subject-list',
    ),
    path('subjects/', views.SubjectList.as_view(), name='subject-list'),

    # question related paths
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(), name='question-detail'),
    path('questions/ask/', views.QuestionCreate.as_view(), name='question-create'),
    path(
        'questions/<int:pk>/edit/',
        views.QuestionUpdate.as_view(),
        name='question-update',
    ),

    # answer related paths
    path(
        'answers/<int:pk>/edit/',
        views.AnswerUpdate.as_view(),
        name='answer-update',
    ),
    path(
        'questions/<int:question_pk>/answer/',
        views.AnswerCreate.as_view(),
        name='answer-create',
    ),

    path('auth/', include(django.contrib.auth.urls)),

    # social log
    url(r'^oauth/', include('social_django.urls', namespace='social')),

]
