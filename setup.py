from distutils.core import setup

setup(
    name='django-oauth2-tastypie',
    version='0.1.0',
    package_dir={'': 'src'},
    py_modules=['authentication'],
    install_requires=[
        "django-oauth-tastypie",
        "django-oauth2-provider",
    ]
)