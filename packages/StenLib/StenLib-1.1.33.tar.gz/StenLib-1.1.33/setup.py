from setuptools import find_packages, setup

setup(
    name='StenLib',
    version='1.1.33',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license=open('LICENSE.md').read(),
    url='https://github.com/Structura-Engineering/StenLib',
    project_urls={
        'Bug Tracker': 'https://github.com/Structura-Engineering/StenLib/issues'
    },
    install_requires=open('requirements.txt').read().splitlines(),
    packages=find_packages(),
    python_requires='==3.12.2',
    package_data={'*': ['*.py'], '': ['py.typed']},
    data_files=[('', ['LICENSE.md', 'README.md', 'requirements.txt'])],
    zip_safe=False,
)
