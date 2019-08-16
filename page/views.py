from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (Carousel, Page)
from .forms import CarouselModelForm, PageModelForm
from django.utils.text import slugify
from django.contrib.admin.views.decorators import staff_member_required
from product.models import Category, Product

STATUS = 'published'


# user
def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(
        status=STATUS).exclude(cover_image='')
    context['products'] = Product.objects.filter(
        status=STATUS
    )[:9]
    # context['images'] = images
    # context['categories'] = Category.objects.filter(
    #     status=STATUS
    # ).order_by('title')
    return render(request, 'home/index.html', context)


def manage_list(request):
    context = dict()
    return render(request, 'manage/manage.html', context)


@staff_member_required
def page_list(request):
    context = dict()
    context['items'] = Page.objects.all().order_by('-pk')
    return render(request, 'manage/page_list.html', context)


def page_create(request):
    context = dict()
    context['title'] = 'Page Form'
    context['form'] = PageModelForm()

    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.slug = slugify(item.title.replace('ı', 'i'))
            item.save()
            messages.success(request, 'Page Oluşturuldu.')
    return render(request, 'manage/form.html', context)


def page_update(request, pk):
    context = dict()
    item = Page.objects.get(pk=pk)
    context['title'] = f"title : '{item.title}' - pk : {item.pk} Carousel Create Form"
    context['form'] = PageModelForm(instance=item)
    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug == '':
                item.slug = slugify(item.title.replace('ı', 'i'))
            item.save()
            messages.success(request, 'Page Güncellendi.')
            return redirect('page_update', pk)

    return render(request, 'manage/form.html', context)


def page_delete(request, pk):
    item = Page.objects.get(pk=pk)
    item.status = 'deleted'
    item.save()
    return redirect('page_list')


# admin
@staff_member_required
def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all().order_by('-pk')
    return render(request, 'manage/carousel_list.html', context)


def carousel_update(request, pk):
    context = dict()
    # kaft_clone.com/manage=carousel/1/edit
    # show
    item = Carousel.objects.get(pk=pk)
    context['title'] = f"title : '{item.title}' - pk : {item.pk} Carousel Create Form"
    context['form'] = CarouselModelForm(instance=item)
    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carousel Güncellendi.')
            return redirect('carousel_update', pk)

    return render(request, 'manage/form.html', context)
# stuff not checked


# def carousel_form_save(request=None, instance=None):
#     if request:
#         form = CarouselModelForm(request.POST,
#                                  request.FILES,
#                                  instance=instance
#                                  )
#     else:
#         form = CarouselModelForm(instance=instance)
#     return form


def carousel_form(request):
    context = dict()
    context['form'] = CarouselModelForm()

    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
    return render(request, 'manage/form.html', context)
