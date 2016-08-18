import setuptools

setuptools.setup(
    name='django-model-settings',
    use_scm_version={'version_scheme': 'post-release'},
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=[
        'django-classy-tags',
        'django-polymorphic',
    ],
    setup_requires=['setuptools_scm'],
    extras_require={
      "test": ["coverage==4.2"]
    }
)
