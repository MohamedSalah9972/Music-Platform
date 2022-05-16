# Django Training - 6. Django Extensions, Knox Token Authentication

## Grade 65/100

## Task
3. In the `users` app, extend Django's user model to include an optional `bio` `CharField` with a max length of 256 characters
    * On django admin, this field should be displayed as a `TextArea` **(-10)**
5. In the `authentication` app, support a `POST authentication/register/` endpoint that creates users.
    * Think about the suitable permission class(es) for this endpoint.
        * **There's no need to override a view's `get_permissions()` method if you're not defining the permissions dynamically, use the `permission_classes` class attribute directly**
    * This endpoint must accept the following fields formatted in JSON:
        * **(-5) `RegisterSerializer` raises an error when `bio` is missing, and it isn't a required field in the registration**
        * **(-10) `RegisterSerializer` doesn't raise a validation error when `email` is missing from the request body, that's because the `email` field is defined as optional on django's user model `email = models.EmailField(_("email address"), blank=True)`. This can be fixed by adding `email` to `extra_kwargs` and setting the `required` attribute or making this field required on your `CustomUser` class**
        ```
        class Meta:
            model = CustomUser
            fields = ('id', 'username', 'email', 'password', 'confirmation_password', 'bio')        
            extra_kwargs = 
            {
                'password': {'write_only': True}, 
                'email': {"required": True}
            }
        ```
7. In the `users` app, create a user detail endpoint `/users/<pk>` that supports the following requests:
    * Support updating the `bio`, `username`, and `email` fields via the following requests:
        * `PUT` This is exactly the same as when creating a user except that an ID of an existing user is
    provided in the URL, and that the request will overwrite the user's data with that given ID.
        * `PATCH` This is exactly the same as when updating a user except none of the fields are required,
and that only fields given a value will be updated. (hint: see `partial_update` in serializers)
        * Allow update requests if the user making the request is the user in the `<pk>` of the url.
            * **(-5) Permissions should be handled in a [permission class](https://www.django-rest-framework.org/api-guide/permissions/) not in the view's serializer**

            ```
            users/permissions.py

            class IsUserInstanceOwner(permissions.BasePermission):
                def has_object_permission(self, request, view, obj):
                    return request.user == obj
            ```
            ```
            users/views.py
            class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
                permission_classes = [IsAuthenticatedOrReadOnly, IsUserInstanceOwner]
            ```

            * **(-5) `id` field shouldn't be looked up or required in the requests's body since it's already in included as a url kwarg`**      