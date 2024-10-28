from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('news/all/', views.all_news_page, name='all_news_page'),
    path('news/detail/<int:pk>/', views.news_detail_page, name='news_detail_page'),
    path('news/tag/<slug:slug>/', views.tags_news_page, name='tags_news_page'),
    path('news/search/', views.search_page, name='search_page'),
    path('news/search/results/', views.search_results_page, name='search_results_page'),
    path('admin/login/', views.admin_login_page, name='admin_login_page'),
    path('admin/dashboard/', views.admin_dashboard_page, name='admin_dashboard_page'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('admin/tags/', views.admin_tags_list, name='admin_tags_list'),
    path('admin/tags/create/', views.admin_tags_create, name='admin_tags_create'),
    path('admin/tags/update/<int:pk>/', views.admin_tags_update, name='admin_tags_update'),
    path('admin/tags/delete/<int:pk>/', views.admin_tags_delete, name='admin_tags_delete'),
    path('admin/news/', views.admin_news_list, name='admin_news_list'),
    path('admin/news/create/', views.admin_news_create, name='admin_news_create'),
    path('admin/news/update/<int:pk>/', views.admin_news_update, name='admin_news_update'),
    path('admin/news/delete/<int:pk>/', views.admin_news_delete, name='admin_news_delete'),
]