from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('save/', views.save_data),
    path('delete/<int:id>', views.delete_employee),
    path('update/<int:id>', views.update_employee),
]
