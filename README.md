# About

django-tastypie-two-legged-oauth is a simple 2-legged OAuth authentication model for Django Tastypie.

This nearly an exact copy of
[gregbayer/django-piston-two-legged-oauth](https://github.com/gregbayer/django-piston-two-legged-oauth),
an OAuth connector for django-piston.

# Dependencies: 
* [django tastypie](https://github.com/toastdriven/django-tastypie)
* [python-oauth2](https://github.com/simplegeo/python-oauth2)


# Adapted from example:  
* [two-legged-oauth-in-python](http://philipsoutham.com/post/2172924723/two-legged-oauth-in-python)


# Related discussions:
* [Beginner’s Guide to OAuth – Part II : Protocol Workflow](http://hueniverse.com/2007/10/beginners-guide-to-oauth-part-ii-protocol-workflow/)

# Example

\# resources.py

	from tastypie.resources import ModelResource
	from tastypie.authorization import DjangoAuthorization
	from django.contrib.auth.models import User
	from authentication import TwoLeggedOAuthAuthentication

	class UserResource(ModelResource):
    	class Meta:
       		queryset = User.objects.all()
        	resource_name = 'users'
        	excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        	authorization = DjangoAuthorization()
        	authentication = TwoLeggedOAuthAuthentication()

