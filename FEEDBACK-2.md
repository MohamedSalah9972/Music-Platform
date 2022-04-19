# Django Training - 2. Django Admin and Managers


## Grade 92/100

## Task
* **(-15) pyproject.toml isn't included in the project files, you didn't use poetry to install and list the project dependencies**

4. Add a help text that would show up under the previously mentioned boolean field on the django admin form, it should state: 
    * bonus: can you add the help text without modifying the boolean field itself? (hint: you'll modify the form) **(+5)**
6. (bonus) Modify the artist queryset so that I can order the list of artists by the number of their approved albums
    * I should be able to do the following `Artist.objects.....order_by("approved_albums")` **(+2) for using annotate**
    * However, your implementation made this feature exclusive only for django admin, instead this should be implemented via a model's custom manager so that the all queryset calls support the customization, whether it'll be used on django admin or not. Here's *one* correct way of doing it:

    ```
    # managers.py
    from django.db import models
    from django.db.models.fields import IntegerField
    from django.db.models.functions import Coalesce
    from django.apps import apps

    class ArtistQuerySet(models.QuerySet):
        def with_approved_albums(self):
            Album = apps.get_model("albums", "Album") # to avoid 'partially initialized module' error
            
            subquery = (
                Album.objects
                .filter(artist=models.OuterRef("pk"))
                .values("artist")
                .annotate(approved_albums_sum=models.Sum("approved"))
                .values("approved_albums_sum")
            ) # the result of this will look something like [{artist1, 0}, {artist2, 15}, {artist3, None}]
            
            # we use Coalesce because the subquery could be `None` for the artists who have no albums
            return self.annotate(approved_albums=Coalesce( 
                models.Subquery(subquery),
                0,
                output_field=IntegerField(),
            ))
    ```
    ---
    ```
    # models.py

    from django.db import models
    from .managers import ArtistQuerySet

    class Artist(models.Model):
        objects = ArtistQuerySet.as_manager()

        stage_name = models.CharField(max_length=200, unique=True, null=False)
        social_link = models.URLField(blank=True, default='')
    ```
    ---
    This will allow you to perform the following queries on a database level:
    ```
    a = Artist.objects.filter(...).with_approved_albums().first()
    a.approved_albums

    # or

    qs = Artist.objects.with_approved_albums().all().order_by("approved_albums")
    ```

## Questions
1. Which is better stackedinline or tabularinline?
    * The difference is visual, see the source code:
    ```
    class StackedInline(InlineModelAdmin):
        template = "admin/edit_inline/stacked.html"


    class TabularInline(InlineModelAdmin):
        template = "admin/edit_inline/tabular.html"
    ```
2. Should I make `ArtistAdmin.approved_albums` static?
    * I tried this and I lost the ability to order the column on the list display
    * This might be because somewhere the admin class or the display decorator expect the method to be an instance method not a static method