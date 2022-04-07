#Shell queries

Use the following command to use the shell
```
python3 manage.py shell
```
## Create some random artists

After run the shell command, create some random artists with the following commands:
```python
from artists.models import Artist
import string
import random
for i in range(20):
    letters = string.ascii_lowercase
    stage_name = ''.join(random.choice(letters) for _ in range(4))
    social_link = "https://www.facebook.com/" + stage_name
    Artist.objects.create(stage_name=stage_name, social_link=social_link)
```   
### results of the query
````
<Artist: Artist object (1)>
<Artist: Artist object (2)>
<Artist: Artist object (3)>
<Artist: Artist object (4)>
<Artist: Artist object (5)>
<Artist: Artist object (6)>
<Artist: Artist object (7)>
<Artist: Artist object (8)>
<Artist: Artist object (9)>
<Artist: Artist object (10)>
<Artist: Artist object (11)>
<Artist: Artist object (12)>
<Artist: Artist object (13)>
<Artist: Artist object (14)>
<Artist: Artist object (15)>
<Artist: Artist object (16)>
<Artist: Artist object (17)>
<Artist: Artist object (18)>
<Artist: Artist object (19)>
<Artist: Artist object (20)>
````
## List down all artists

List down all artists with the following commands:
```python
from artists.models import Artist
queryset = Artist.objects.all()
for artist in queryset:
    print(artist.id, artist.stage_name, artist.social_link)
```

### Results (id, stage name, social link)


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

## List down all artists whose stage name starts with 'a'

List down all artists whose stage name starts with 'a' with the following commands:

```python
from artists.models import Artist
queryset = Artist.objects.all().filter(stage_name__startswith='a')
for artist in queryset:
    print(artist.id, artist.stage_name, artist.social_link)
```

### Results(id, stage name, social link)

```
6 aspl https://www.facebook.com/aspl
```


## Create some albums and assign them to any artists (1st way)
```python
from artists.models import Artist
from albums.models import Album
import datetime
for i in range(20):
    rand_artist = Artist.objects.order_by('?').first()
    rand_artist.albums.create(
    name="album"+str(i),
    release_datetime=datetime.date(2020, 1, i+1),
    cost = 123/(i+1)
    )
```

### Result of query:
```shell
<Album: Album object (61)>
<Album: Album object (62)>
<Album: Album object (63)>
<Album: Album object (64)>
<Album: Album object (65)>
<Album: Album object (66)>
<Album: Album object (67)>
<Album: Album object (68)>
<Album: Album object (69)>
<Album: Album object (70)>
<Album: Album object (71)>
<Album: Album object (72)>
<Album: Album object (73)>
<Album: Album object (74)>
<Album: Album object (75)>
<Album: Album object (76)>
<Album: Album object (77)>
<Album: Album object (78)>
<Album: Album object (79)>
<Album: Album object (80)>
```

## Create some albums and assign them to any artists (2nd way)
```python
from artists.models import Artist
from albums.models import Album
for i in range(20):
    rand_artist = Artist.objects.order_by('?').first()
    Album.objects.create(
        artist=rand_artist,
        name="album"+str(i),
        release_datetime=datetime.date(2020, 1, i+1),
        cost = 123/(i+1)
    )
```

### Result of query:
```shell
<Album: Album object (81)>
<Album: Album object (82)>
<Album: Album object (83)>
<Album: Album object (84)>
<Album: Album object (85)>
<Album: Album object (86)>
<Album: Album object (87)>
<Album: Album object (88)>
<Album: Album object (89)>
<Album: Album object (90)>
<Album: Album object (91)>
<Album: Album object (92)>
<Album: Album object (93)>
<Album: Album object (94)>
<Album: Album object (95)>
<Album: Album object (96)>
<Album: Album object (97)>
<Album: Album object (98)>
<Album: Album object (99)>
<Album: Album object (100)>
```

## Get the latest released album
Get the latest released album with the following commands:

```python
from albums.models import Album
obj = Album.objects.all().latest('release_datetime')
print(obj.id, obj.name, obj.release_datetime, obj.cost)
```
### results(id, name, released date, cost):
```shell
80 album19 2020-01-20 6.15
```

## Get all albums released before today
Get all albums released before today with the following commands:

```python
from albums.models import Album
import datetime
queryset = Album.objects.filter(release_datetime__lt=datetime.date.today())

for i in queryset:
    print(i.id, i.name, i.release_datetime)
```
### Results
```shell
61 album0 2020-01-01
62 album1 2020-01-02
63 album2 2020-01-03
64 album3 2020-01-04
65 album4 2020-01-05
66 album5 2020-01-06
67 album6 2020-01-07
68 album7 2020-01-08
69 album8 2020-01-09
70 album9 2020-01-10
71 album10 2020-01-11
72 album11 2020-01-12
73 album12 2020-01-13
74 album13 2020-01-14
75 album14 2020-01-15
76 album15 2020-01-16
77 album16 2020-01-17
78 album17 2020-01-18
79 album18 2020-01-19
80 album19 2020-01-20
81 album0 2020-01-01
82 album1 2020-01-02
83 album2 2020-01-03
84 album3 2020-01-04
85 album4 2020-01-05
86 album5 2020-01-06
87 album6 2020-01-07
88 album7 2020-01-08
89 album8 2020-01-09
90 album9 2020-01-10
91 album10 2020-01-11
92 album11 2020-01-12
93 album12 2020-01-13
94 album13 2020-01-14
95 album14 2020-01-15
96 album15 2020-01-16
97 album16 2020-01-17
98 album17 2020-01-18
99 album18 2020-01-19
100 album19 2020-01-20
```

## Get all albums released today or before but not after today
Get all albums released today or before but not after today with the following commands:

```python
from albums.models import Album
import datetime
queryset = Album.objects.filter(release_datetime__lte=datetime.date.today())

for i in queryset:
    print(i.id, i.name, i.release_datetime)
```

### Results
```shell
61 album0 2020-01-01
62 album1 2020-01-02
63 album2 2020-01-03
64 album3 2020-01-04
65 album4 2020-01-05
66 album5 2020-01-06
67 album6 2020-01-07
68 album7 2020-01-08
69 album8 2020-01-09
70 album9 2020-01-10
71 album10 2020-01-11
72 album11 2020-01-12
73 album12 2020-01-13
74 album13 2020-01-14
75 album14 2020-01-15
76 album15 2020-01-16
77 album16 2020-01-17
78 album17 2020-01-18
79 album18 2020-01-19
80 album19 2020-01-20
81 album0 2020-01-01
82 album1 2020-01-02
83 album2 2020-01-03
84 album3 2020-01-04
85 album4 2020-01-05
86 album5 2020-01-06
87 album6 2020-01-07
88 album7 2020-01-08
89 album8 2020-01-09
90 album9 2020-01-10
91 album10 2020-01-11
92 album11 2020-01-12
93 album12 2020-01-13
94 album13 2020-01-14
95 album14 2020-01-15
96 album15 2020-01-16
97 album16 2020-01-17
98 album17 2020-01-18
99 album18 2020-01-19
100 album19 2020-01-20
```

## Count the total number of albums released so far
Count the total number of albums released so far with the following commands:

```python
from albums.models import Album
Album.objects.count()
```
### Results
```shell
40
```
