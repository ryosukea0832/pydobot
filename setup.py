import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mypydobot',
    packages=['mypydobot','mypydobot.enums'],
    version='0.1.0',
    description='Python library for Dobot Magician',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['dobot', 'magician', 'robotics'],
    classifiers=[],
    install_requires=[
        'pyserial==3.4'
    ]
)
