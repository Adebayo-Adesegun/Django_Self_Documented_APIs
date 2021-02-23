from django.conf.urls import url
from management import views



urlpatterns = [
    #Define urls for Catalogue Operations
    url(r'^api/catalogues$', views.catalogue_list),
    url(r'^api/catalogues/(?P<pk>[0-9]+)$', views.catalogue_detail),
 
    #Define urls for Book Operations
    url(r'^api/books$', views.book_list),
    url(r'^api/books/(?P<pk>[0-9]+)$', views.book_detail)
]
