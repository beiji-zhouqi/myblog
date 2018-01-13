from django.conf.urls import include, url
from django.contrib import admin
from DjangoUeditor import urls as djud_urls
from django.conf import settings
import blog.urls as  blog_url

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/', include(djud_urls)),
    url(r'^blog/', include(blog_url)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
