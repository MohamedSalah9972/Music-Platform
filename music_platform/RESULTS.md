# Shell queries
Use the following command to use the shell
```
python3 manage.py shell
```
## Create some random artists
After run the shell command, create some random artists with the following commands:
```
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
```
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
