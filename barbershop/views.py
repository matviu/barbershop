# -*- coding: utf-8 -*-

from django.views import View
from django.shortcuts import render
from reviews.models import Review


class FrontpageView(View):
    template_name = 'frontpage.html'
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
