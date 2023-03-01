from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Gaming World"
admin.site.site_title = "Gaming World Admin"
admin.site.index_title = "Welcome!"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
