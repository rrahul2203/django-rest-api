from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get --> list --> Queryset
    get --> retrieve --> Product Instance Detail View
    post --> create --> New Instance
    put --> Update
    patch --> Partial Update
    delete --> Destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    get --> list --> Queryset
    get --> retrieve --> Product Instance Detail View
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

products_v2_list_view = ProductGenericViewSet.as_view({'get':'list'})
products_v2_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})
