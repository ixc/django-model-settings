from model_settings import VERSION
import setuptools

setuptools.setup(
    name='django-model-settings',
    version=VERSION,
    packages=setuptools.find_packages(),
    install_requires=[
    	'django-classy-tags',
        'django-polymorphic',
    ]
)
