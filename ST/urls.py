from django.urls import path
from. import views
 urlpatterns=[
        path('sightings/',views.all_squirrel),
        path('sightings/<squirrel_id>',views.edit_squirrel),
        path('sightings/add',views.add_squirrel),
]

