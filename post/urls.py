from django.urls import path

from . import views

app_name = "post"
urlpatterns = [
    path("",views.index, name='index'),
    #path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("register/", views.post_register, name="post_register"),
    path("<int:pk>/edit", views.post_edit, name="post_edit"),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]