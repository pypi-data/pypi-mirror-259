from setuptools import setup, find_packages

setup(
    name='cs_p2p',
    version='0.1.1.1',
    packages=find_packages(),
    install_requires=[
        "loguru",
        "python-dotenv",
        "pyzmq",
    ],
    author='Enrico Zanardo',
    author_email='enrico.zanardo101@gmail.com',
    description='P2P library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/enricozanardo/cs_p2p.git',
    license='AGPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
