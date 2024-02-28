from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name='eces_eg_weather_package',  # Your package will have this name
    packages= find_packages(),  # Name the package again
    version='1.1.0',  # To be increased every time you change your library
    license='MIT',  # Type of license. More here: https://help.github.com/articles/licensing-a-repository
    description='Weather forecast data',  # Short description of your library
    author='Ahmed Dawoud',  # Your name
    author_email='ahmed.ismail2013@feps.edu.eg',  # Your email
    url='https://adawoud.com/',  # Homepage of your library (e.g. github or your website)
    keywords=['weather', 'forecast', 'openweather'],  # Keywords users can search on pypi.org
    install_requires=[
        'requests',
        'pandas'
    ],
    long_description=description,
    long_description_content_type="text/markdown"
    
)
