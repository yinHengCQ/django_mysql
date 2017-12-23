from django.conf.urls import include, url
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_mysql.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^showAll/$',views.showAll),
    url('^answer/$',views.answer)
]