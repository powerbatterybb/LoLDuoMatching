from django.urls import path

from . import views

app_name = "post"
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("register/", views.post_register, name="post_register"),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search_results, name='search_results'),
]
