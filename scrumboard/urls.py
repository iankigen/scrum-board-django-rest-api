from django.urls import path

from .api import (
    CardApi, ListApi, CreateListApi, DeleteListApi, SingleListApi, UpdateListApi, CreateCardApi, SingleCardApi,
    DeleteCardApi, UpdateCardApi
)

urlpatterns = [
    # list
    path('create-list/', CreateListApi.as_view()),
    path('list/', ListApi.as_view()),
    path('list/<id>', SingleListApi.as_view()),
    path('list/<id>/delete', DeleteListApi.as_view()),
    path('list/<id>/edit', UpdateListApi.as_view()),

    # card
    path('card/', CardApi.as_view()),
    path('create-card/', CreateCardApi.as_view()),
    path('card/<id>', SingleCardApi.as_view()),
    path('card/<id>/delete', DeleteCardApi.as_view()),
    path('card/<id>/edit', UpdateCardApi.as_view()),
]
