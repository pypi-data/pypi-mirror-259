# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['social_auth_gsis', 'social_auth_gsis.pipeline']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.2.0',
 'social-auth-app-django>=4.0.0,<5.0.0',
 'social-auth-core>=4.0.2,<5.0.0']

setup_kwargs = {
    'name': 'social-auth-gsis',
    'version': '0.3.1',
    'description': 'Social Auth backend for GSIS',
    'long_description': '# Social Auth GSIS\n\n[Python Social Auth](https://python-social-auth.readthedocs.io/en/latest/) backend for the OAuth 2.0 for [GSIS](https://gsis.gr/en), intended for use in [Django applications](https://python-social-auth.readthedocs.io/en/latest/configuration/django.html).\n\n## Requirements\n\n- Python 3.8, or newer\n- Django 3.2, or newer\n\n## Installation\n\nInstall the [`social-auth-gsis` from PyPI](https://pypi.org/project/social-auth-gsis/) using your favorite package manager.\n\n### pip\n\n```console\npipi install social-auth-gsis\n```\n\n### Poetry\n\n```console\npoetry add social-auth-gsis\n```\n\n## Usage\n\nTo get the GSIS authentication package working with a Django application, both settings and URLs need to be configured.\n\n### Settings\n\nThe best place to get started with integrating Social Auth GSIS in a Django project is the settings.\n\nFirst, the `social_django` app needs to be added in the [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) setting of your Django application:\n\n```py\nINSTALLED_APPS = [\n    # ...the rest of installed apps\n    "social_django",\n]\n```\n\nNext, `social_django.middleware.SocialAuthExceptionMiddleware` needs to be included in [`MIDDELWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE), right below the `django.middleware.clickjacking.XFrameOptionsMiddleware`:\n\n```py\nMIDDLEWARE = [\n    # ...the rest of middleware\n    "django.middleware.clickjacking.XFrameOptionsMiddleware",\n    "social_django.middleware.SocialAuthExceptionMiddleware",\n]\n```\n\nIn order to only allow creation of users through the social auth pipeline, the [`SOCIAL_AUTH_PIPELINE`](https://python-social-auth.readthedocs.io/en/latest/configuration/django.html#personalized-configuration) Django Social Auth setting needs to be set to the following value:\n\n```py\nSOCIAL_AUTH_PIPELINE = (\n    "social_core.pipeline.social_auth.social_details",\n    "social_core.pipeline.social_auth.social_uid",\n    "social_core.pipeline.social_auth.auth_allowed",\n    "social_auth_gsis.pipeline.social_auth.social_user",\n    "social_core.pipeline.social_auth.associate_user",\n    "social_core.pipeline.social_auth.load_extra_data",\n    "social_core.pipeline.user.user_details",\n)\n```\n\nTo configure the credentials and redirect URLs of a Social Auth GSIS backend the appropriate settings need to be set as well:\n\n```py\nSOCIAL_AUTH_GSIS_KEY = "oauth2_client_key"\nSOCIAL_AUTH_GSIS_SECRET = "oauth2_client_secret"\nSOCIAL_AUTH_GSIS_REDIRECT_URL = "https://yourapp.local/authorize/gsis/"\n```\n\nFinally, the intended backends should be included in the [`AUTHENTICATION_BACKENDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-AUTHENTICATION_BACKENDS) setting:\n\n```py\nAUTHENTICATION_BACKENDS = (\n    "social_auth_gsis.backends.GSISOAuth2",\n    # ...the rest of backends included\n)\n```\n\n### URLs\n\nThe URLs of Django Social Auth are required to be included also, in order to authenticate users redirected from GSIS\' auth:\n\n```py\nfrom django.urls import include, path\nfrom social_django import views as social_django_views\n\n\nurlpatterns = [\n    path("auth/", include("social_django.urls", namespace="social")),\n    # ...the rest of URL patterns\n]\n```\n\nThe ability to explicitly set the backend to be used in a URL for authentication, is also possible:\n\n```py\nurlpatterns = [\n    path(\n        "authorize/gsis/",\n         social_django_views.complete,\n        kwargs={"backend": "ktimatologio_gsis"},\n        name="authorize",\n    ),\n    # ...the rest of URL patterns\n]\n```',
    'author': 'Paris Kasidiaris',
    'author_email': 'paris@withlogic.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
