from . import views
from django.urls import path
urlpatterns=[
        path('sightings/',views.all_squirrel),
        path('sightings/<squirrel_id>',views.edit_squirrel),
        path('sightings/add',views.add_squirrel),
]

