from django.conf.urls import url
from django.contrib.auth import views
from . import views as acc_views


urlpatterns = [
    url(r'^registration/$', acc_views.AccountsRegistrationView.as_view, name='registration'),

    url(r'^login/$', acc_views.AccountsLoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    url(r'^password_change/$', views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change/done/$', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    url(r'^password_reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]