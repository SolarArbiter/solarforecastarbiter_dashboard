from setuptools import setup, find_packages
import versioneer


setup(
    name='sfa-dash',
    version=verioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description=('Dashboard for interacting with Solar Forecast Arbiter'
                 'Backend'),
    url='https://github.com/SolarArbiter/solarforecastarbiter_dashboard',
    author='Solar Forecast Arbiter Team',
    author_email='info@solarforecastarbiter.org',
    packages=find_packages(),
    install_requires=[
        'flask',
        'requests',
        'pandas',
        'flask-dance',
        'sqlalchemy',
        'flask-sqlalchemy',
        'pymysql',
        'flask-seasurf',
        'python-jose',
        'cryptography',
        'blinker',
        'bokeh',
        'solarforecastarbiter',
        'sentry_sdk',
        'blinker',
        'prometheus-flask-exporter'
    ]
)
