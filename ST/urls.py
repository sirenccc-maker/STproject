from . import views
from django.urls import path
urlpatterns=[
        path('',views.all_squirrel),
        path('add/',views.add_squirrel),
        path('stats/',views.stats),
        path('<squirrel_id>/',views.edit_squirrel),
]

