import setuptools

setuptools.setup(
    name='django-model-settings',
    use_scm_version={'version_scheme': 'post-release'},
    packages=setuptools.find_packages(),
    install_requires=[
        'django-classy-tags',
        'django-polymorphic',
    ],
    setup_requires=['setuptools_scm'],
)
