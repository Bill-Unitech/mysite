from django.conf.urls import url
from django.contrib import admin
from mainpage import views as mainpage_views
from blogs import views as blog_views
from courses import views as course_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #mainpage view
	url(r'^$', mainpage_views.index),

    #blogs view
    url(r'^blog/$', blog_views.my_blog_index),
    url(r'^blog/(?P<id>\d+)/$', blog_views.my_blog_post),
    #course view
    url(r'^course/$', course_views.my_course_index),
    #contact view
    url(r'^contact/$', course_views.my_contact),
    #sending email
    url(r'^email/$', course_views.email),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)