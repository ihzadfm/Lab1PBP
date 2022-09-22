from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_json #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_json_by_id #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_xml_by_id #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import register #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_json, name='show_json'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), #sesuaikan dengan nama fungsi yang dibuat
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'), #sesuaikan dengan nama fungsi yang dibuat
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    
]
