from django.db import models

class Entry(models.Model):
	last_name = models.CharField(max_length=100, verbose_name='Фамилия')
	first_name = models.CharField(max_length=100, verbose_name='Имя')
	second_name = models.CharField(max_length=100, verbose_name='Отчество')
	tel_number = models.CharField(max_length=100, verbose_name='Контактный телефон')
	email = models.EmailField(max_length=100, verbose_name='Контактный e-mail')
	add_info = models.CharField(max_length=200, verbose_name='доп. информация')

	BEARD_MODELS = (
		('admiral', 'адмирал'),
		('woodchoper', 'лесоруб'),
		('polar', 'полярник'),
		('merchant', 'боярин'),
		('elder', 'мудрец'),
	)

	beard_model = models.CharField(max_length=100, verbose_name='модель бороды',
	                               choices=BEARD_MODELS)

	is_beard_paint = models.BooleanField(default=False, verbose_name='Подкрасить бороду')
	is_beard_brush = models.BooleanField(default=False, verbose_name='Причесать бороду')
	is_remove_gray = models.BooleanField(default=False, verbose_name='Убрать седину')
	is_moustache_spin = models.BooleanField(default=False, verbose_name='Накрутить усы')
	is_trim = models.BooleanField(default=False, verbose_name='Подровнять виски')
	is_polish_head = models.BooleanField(default=False, verbose_name='отполировать лысину')

	date_added = models.DateTimeField(verbose_name='дата и время создания', auto_now_add=True)
	date_record = models.DateTimeField(verbose_name='дата и время записи')

	class Meta:
		verbose_name = 'запись на прием'
		verbose_name_plural = 'записи на прием'
		ordering = ['-date_record']




