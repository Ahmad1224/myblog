
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('BlogApp.urls')),
    path('wordcount/', include('wordcount.urls')),
    path('account/',include('account.urls')),          # path for new app ...

]
