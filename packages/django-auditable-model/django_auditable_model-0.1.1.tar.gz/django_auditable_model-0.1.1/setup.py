from setuptools import setup, find_packages
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='django_auditable_model',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',  # Example license
    description='A Django app providing reusable abstract models.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Shubham Sharma',
    author_email='sharma.shubham6522@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)