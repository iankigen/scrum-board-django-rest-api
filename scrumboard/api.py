from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView

from .serializers import ListSerializer, CardSerializer
from .models import List, Card
from .pagination import PageNoPagination


class ListApi(ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    filter_backends = [SearchFilter]
    search_fields = ['name']

    pagination_class = PageNoPagination


class SingleListApi(RetrieveAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    lookup_field = 'id'


class CreateListApi(CreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class DeleteListApi(DestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    lookup_field = 'id'


class UpdateListApi(RetrieveUpdateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    lookup_field = 'id'


class CardApi(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    filter_backends = [SearchFilter]

    search_fields = ['title', 'description']

    pagination_class = PageNoPagination


class CreateCardApi(CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class SingleCardApi(RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    lookup_field = 'id'


class DeleteCardApi(DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    lookup_field = 'id'


class UpdateCardApi(RetrieveUpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    lookup_field = 'id'
