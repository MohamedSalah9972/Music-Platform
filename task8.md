- didn't use the LimitOffsetPagination
- no bonus for the custom manager for album
- you can use the django filters with DRF with more convenient way

```
class AlbumViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = AlbumSerializer
    // or you can get all here and override the get_queryset()
    queryset = Album.objects.approved_albums().all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AlbumFilter


```
- you can use mixins better than generics to add more flexibility
- you need to have filters in a seperate file as serializers and views
- I don't quite understand how your permissions work - so please get back to me to explain- , i see it works but i don't get how and your idea
- you have two create views, can you explain why?
- you can use the decorator `@pytest.mark.django_db` for all the file, no need for every method
- why you use `client.post('/authentication/login/', login_credentials)` in `conftest.py:auth_client` ?? 
- you can use factories, to create instances of objects