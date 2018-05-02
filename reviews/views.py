# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy, reverse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Review, ReviewPhoto
from .forms import AddReviewForm
from price_list.models import PriceList


class ReviewsListView(TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'reviews/reviews_list.html'
        try:
            reviews = Review.objects.all()
        except ObjectDoesNotExist:
            reviews = []
        try:
            price = PriceList.objects.get(version=True)
        except ObjectDoesNotExist:
            print(u'Ни один из прайсов не имеет отметки \'отображать на сайте\'')
            try:
                price = PriceList.objects.all().first()
            except ObjectDoesNotExist:
                print(u'В системе управления отсутствуют прайсы')
        except MultipleObjectsReturned:
            print(u'Несколько прайсов имеют отметку \'отображать на сайте\'')
            price = PriceList.objects.all().first()


        context = {
            'reviews': reviews,
            'price': price,
        }

        return render(request, template_name, context)


class AddReviewView(FormView):
    form_class = AddReviewForm
    template_name = 'reviews/add_review.html'
    success_url = '/reviews/'

    def get(self, request, *args, **kwargs):
        form = AddReviewForm()
        try:
            price = PriceList.objects.get(version=True)
        except ObjectDoesNotExist:
            print('Ни один из прайсов не имеет отметки \'отображать на сайте\'')
            try:
                price = PriceList.objects.all().first()
            except ObjectDoesNotExist:
                print('В системе управления отсутствуют прайсы')
        except MultipleObjectsReturned:
            print('Несколько прайсов имеют отметку \'отображать на сайте\'')
            price = PriceList.objects.all().first()

        context = {
            'form': form,
            'price': price,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = AddReviewForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            is_haircut = form.cleaned_data['is_haircut']
            is_shave = form.cleaned_data['is_shave']
            is_moustache = form.cleaned_data['is_moustache']

            review = Review.objects.create(name=name, description=description, is_haircut=is_haircut, is_shave=is_shave, is_moustache=is_moustache)

            review.save()

            for image in form.cleaned_data['images']:
                review_photo = ReviewPhoto.objects.create(image=image, review=review)
                review_photo.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})



