from rest_framework.pagination import PageNumberPagination


class PageNoPagination(PageNumberPagination):
    page_size = 1
