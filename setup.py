import setuptools


long_description = open('README.md').read()


setuptools.setup(
    name='ygoprodeck-api-client',
    version='0.0.1',
    description='A simple client to access the https://db.ygoprodeck.com API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Ronald Theodoro',
    author_email='ronald.silva4@fatec.sp.gov.br',
    url='https://github.com/RonaldTheodoro/ygoprodeck-api-client',
    packages=('ygoprodeck',),
    install_requires=('requests',),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
)
