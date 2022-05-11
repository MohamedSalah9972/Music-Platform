# Djnago Training - 5. Django REST Framework

## Grade 100/100

## Task
2. Create a class-based view at the path `/artists/` that returns a list of artists in JSON format for `GET` requests, the artist data should include the following fields. 
3. The same view above should accept `POST` requests and accept all the fields on the artist model (excluding the id)
* **Tip: You can also use IsAuthenticatedOrReadOnly permission class to achieve the same permission logic with less code:**
```
class ArtistViewSet(generics.GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArtistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

```
