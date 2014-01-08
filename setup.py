from distutils.core import setup

setup(
    name='django-oauth2-tastypie',
    version='0.1.0',
    package_dir={'': 'src'},
    py_modules=['authentication'],
    install_requires=[
        "django-tastypie==0.11.0",
        "django-oauth2-provider==0.2.6",
    ]
)