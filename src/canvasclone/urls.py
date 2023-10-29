"""
URL configuration for canvasclone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from home.views import (
    home_screen_view,
    grades_view
)

from sampleclass.views import (
    sample_class_view,
    assignments_view,
    announcements_view,
    modules_view,
    assignment_detail_view,
    module_detail_view,
    class_grades_view,
)

from account.views import (
    registration_view,
    login_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_screen_view, name="home"),
    path("grades/", grades_view, name="grades"),
    path("sampleclass/<str:course_id>", sample_class_view, name="sampleclass"),#here
    path("sampleclass/<str:course_id>/assignments", assignments_view, name="assignments"),
    path("sampleclass/<str:course_id>/assignments/<str:assignment_id>", assignment_detail_view, name="assignment_detail"),
    path("sampleclass/<str:course_id>/announcements", announcements_view, name="announcements"),
    path("sampleclass/<str:course_id>/grades", class_grades_view, name="course_grades"),
    path("sampleclass/<str:course_id>/modules", modules_view, name="modules"),
    path("sampleclass/<str:course_id>/pages/<str:module_name>/<str:module_section_name>", module_detail_view, name="module_detail"),
    path("register/", registration_view, name="register"),
    path("login/", login_view, name="login"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)