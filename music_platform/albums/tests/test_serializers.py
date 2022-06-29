import pytest

from albums.serializers import AlbumPostSerializer, AlbumSerializer


class TestAlbumSerializers:
    @pytest.mark.django_db
    def test_post_serializer_valid(self, artist):
        valid_serializer_data = dict(artist=1, name='Album', release_datetime='2022-05-29', cost='5.00',
                                     is_approved=False)
        serializer = AlbumPostSerializer(data=valid_serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        valid_serializer_data['id'] = serializer.data['id']  # Add id
        assert serializer.data == valid_serializer_data

    @pytest.mark.django_db
    def test_post_serializer_invalid(self, artist):
        valid_serializer_data = dict(name='Album', release_datetime='2022-05-29', cost='5.00', is_approved=False)
        serializer = AlbumPostSerializer(data=valid_serializer_data)
        assert not serializer.is_valid()

    # you're passing artisit and don't use it
    @pytest.mark.django_db
    def test_get_serializer_valid(self, artist):
        valid_serializer_data = dict(artist=1, name='Album', release_datetime='2022-05-29', cost='5.00',
                                     is_approved=False)
        serializer = AlbumPostSerializer(data=valid_serializer_data)
        serializer.is_valid(raise_exception=True)
        album_instance = serializer.save()

        deserialized = AlbumSerializer(album_instance)

        print(deserialized.data)
        assert deserialized.data['artist']['id'] == valid_serializer_data['artist']
        assert deserialized.data['name'] == valid_serializer_data['name']
        assert deserialized.data['cost'] == valid_serializer_data['cost']
        assert deserialized.data['release_datetime'] == valid_serializer_data['release_datetime']
