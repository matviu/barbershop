from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views as acc_views


urlpatterns = [
    url(r'^registration/$', acc_views.AccountsRegistrationView.as_view(), name='registration'),
    url(r'^profile/$', acc_views.AccountsProfileView.as_view(), name='profile'),

    url(r'^login/$', acc_views.AccountsLoginView.as_view(), name='login'),
    url(r'^logout/$', acc_views.AccountsLogoutView.as_view(), name='logout'),

    #url(r'^password_change/$', acc_views.AccountsPasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change/done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]