from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from cards.views import language_sets, create_language_set
from .views import create_language_set


from django.urls import path

from . import views

urlpatterns = [
    path("", views.CardListView.as_view(), name="card-list"),
    path("new", views.CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
    path("box/<int:box_num>", views.BoxView.as_view(), name="box"),
    path('admin/', admin.site.urls),
    path('language-sets/', language_sets, name='language_sets'),
    path('create-language-set/', create_language_set, name='create_language_set'),
    path('language-set/create/', create_language_set, name='create_language_set'),
]
