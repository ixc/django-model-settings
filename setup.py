from __future__ import print_function

import setuptools
import sys

# Convert README.md to reStructuredText.
if {'bdist_wheel', 'sdist'}.intersection(sys.argv):
    try:
        import pypandoc
    except ImportError:
        print('WARNING: You should install `pypandoc` to convert `README.md` '
              'to reStructuredText to use as long description.',
              file=sys.stderr)
    else:
        print('Converting `README.md` to reStructuredText to use as long '
              'description.')
        long_description = pypandoc.convert('README.md', 'rst')

setuptools.setup(
    name='django-model-settings',
    use_scm_version={'version_scheme': 'post-release'},
    author='Interaction Consortium',
    author_email='studio@interaction.net.au',
    url='https://github.com/ixc/django-model-settings',
    description='Editable settings via polymorphic models with a dict-like '
                'interface and template tags.',
    long_description=locals().get('long_description', ''),
    license='MIT',
    packages = setuptools.find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        'django-classy-tags',
        'django-polymorphic',
    ],
    setup_requires=['setuptools_scm'],
    extras_require={
      "test": ["coverage==4.2"]
    }
)
