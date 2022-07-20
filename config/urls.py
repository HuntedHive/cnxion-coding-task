from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from model_data.views import GenericModelFormView

urlpatterns = [
    re_path(r"^$", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    re_path(
        r"^about/$",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    re_path(settings.ADMIN_URL, admin.site.urls),
    # User management
    re_path(
        r"^users/",
        include("hhcodingtask.users.urls", namespace="users"),
    ),
    re_path(r"^accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    re_path(r'^model_data/', GenericModelFormView.as_view(), name="model_data"),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        re_path(
            r"^400/$",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        re_path(
            r"^403/$",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        re_path(
            r"^404/$",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        re_path(r"^500/$", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [re_path(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
