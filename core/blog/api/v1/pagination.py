from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class SmallPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'pages_size'
    max_page_size = 100
    
    # Use modified pagination
    # def get_paginated_response(self, data):
    #     return Response({
    #         'links': {
    #             'next': self.get_next_link(),
    #             'previous': self.get_previous_link()
    #         },
    #         'total_objects' : self.page.paginator.count,
    #         'total_pages' : self.page.paginator.num_pages,
    #         'result' : data
    #     })