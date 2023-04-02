from rest_framework import mixins, viewsets


class PostViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Viewset only for POST"""
