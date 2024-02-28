from setuptools import find_packages, setup


setup(
    name="datastoresender",
    packages=find_packages(include=['datastoresender']),
    version="0.1.0",
    description="Библиотека для отправки записей в сервис проверок datastore-checker для их последующего изменения в datastore-master-part. Записи прошедшие проверку добавляются в тестовую группу. Позволяет получить информацию о внесенных изменениях.",
    author="kodeyeen",
    install_requires=['aiohttp==3.9.3', 'pydantic==2.6.1'],
    tests_require=['pytest==7.4.4'],
    test_suite='tests',
)
