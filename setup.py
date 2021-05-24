from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name="ninteru-mkdocs-theme",
    version="0.0.1",
    url='https://github.com/ninteru/ninteru_mkdocs_theme',
    license='MIT',
    description='',
    author='ninteru',
    author_email='nino.teruya@embedded.systems',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'ninteru = ninteru_mkdocs_theme',
        ]
    },
    zip_safe=False
)