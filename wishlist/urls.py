from django.urls import path
from wishlist.views import show_wishlist
# Tutorial Lab02
from wishlist.views import show_xml
from wishlist.views import show_json
from wishlist.views import show_xml_by_id
from wishlist.views import show_json_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    #Tutorial Lab02
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]
