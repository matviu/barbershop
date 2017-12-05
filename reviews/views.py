from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Review

from PIL import Image
import os
from django.conf import settings


class ReviewsListView(TemplateView):


	def get(self, request):
		template_name = 'reviews/reviews_list.html'
		reviews = Review.objects.all()

		context = {
			'reviews': reviews,
		}

		return render(request, template_name, context)



