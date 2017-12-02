from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Photo



class PhotosListView(TemplateView):


	def get(self, request):
		template_name = 'photos/photos_list.html'
		photos = Photo.objects.all()

		context = {
			'photos': photos,
		}

		return render(request, template_name, context)



