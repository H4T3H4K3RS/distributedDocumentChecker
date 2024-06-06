from rest_framework import pagination
from django.core.cache import cache
from django.utils.functional import cached_property
from django.core.paginator import Paginator, Page, PageNotAnInteger


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 50
