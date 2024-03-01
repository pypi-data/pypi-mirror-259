from setuptools import setup, find_packages

setup(
    name='nonconvexoptimzationfunclib',
    version='0.0.1',
    author='Dr.Thanos{CSU Fresno} and Satyam Mittal{CSU Fresno}',
    author_email='satyam101905@gmail.com',
    packages=find_packages(),
    description='A library of non-convex optimization functions containing continuous and non-conitnuous functions implemented in higher dimensions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'License :: OSI Approved :: MIT License',
    ],
)
