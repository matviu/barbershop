from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User


class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.PositiveIntegerField(blank=True, null=True)
	avatar = models.ImageField(upload_to='avatars')

	def __str__(self):
		return self.user.username


# def create_account(sender, **kwargs):
# 	print('***********************kwargs in create_account', kwargs)
# 	user = kwargs['instance']
# 	if kw["created"]:
# 		account = Account(user=user)
# 		account.save()
#
#
# signals.post_save.connect(create_account, sender=auth_models.User)
