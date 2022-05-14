from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path("", view=views.index),
    path("<slug:slug>",view=views.book_detail, name="book-detail")
]
