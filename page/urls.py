from django.urls import path
from .views import (
    # manage
    manage_list,

    # page
    page_list,
    page_create,
    page_update,
    page_delete,

    # carousel
    carousel_form,
    carousel_list,
    carousel_update,
)


urlpatterns = [
    path('carousel/list/', carousel_list, name='carousel_list'),
    path('carousel/form/', carousel_form, name='carousel_form'),
    path('carousel/update/<int:pk>/', carousel_update, name='carousel_update'),

    path('', manage_list, name='manage_list'), #manage/

    path('page/list/', page_list, name='page_list'), #page/
    path('page/create/', page_create, name='page_create'), #page/
    path('page/update/<int:pk>/', page_update, name='page_update'), #page/
    path('page/delete/<int:pk>/', page_delete, name='page_delete'), #page/
]
