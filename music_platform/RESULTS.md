```

## List down all artists sorted by stage name
List down all artists sorted by stage name with the following commands:
```
from artists.models import Artist
queryset = Artist.objects.all().order_by('stage_name')
for artist in queryset:
    print(artist.id, artist.stage_name, artist.social_link)
```
## Results(id, stage name, social link)
```
6 aspl https://www.facebook.com/aspl
10 gctw https://www.facebook.com/gctw
14 hhel https://www.facebook.com/hhel
15 hrbz https://www.facebook.com/hrbz
3 ilcy https://www.facebook.com/ilcy
20 jfpu https://www.facebook.com/jfpu
4 kaiw https://www.facebook.com/kaiw
19 lhps https://www.facebook.com/lhps
13 lqga https://www.facebook.com/lqga
12 ouuq https://www.facebook.com/ouuq
16 pbfo https://www.facebook.com/pbfo
7 pyte https://www.facebook.com/pyte
8 rkka https://www.facebook.com/rkka
2 roop https://www.facebook.com/roop
9 rrqu https://www.facebook.com/rrqu
1 ryrt https://www.facebook.com/ryrt
11 uzsj https://www.facebook.com/uzsj
17 yptb https://www.facebook.com/yptb
5 zpit https://www.facebook.com/zpit
18 zyev https://www.facebook.com/zyev
```

# List down all artists whose stage name starts with 'a'
List down all artists whose stage name starts with 'a' with the following commands:
```
from artists.models import Artist
queryset = Artist.objects.all().filter(stage_name__startswith='a')
for artist in queryset:
    print(artist.id, artist.stage_name, artist.social_link)
```

## Results(id, stage name, social link)
```
6 aspl https://www.facebook.com/aspl
```
