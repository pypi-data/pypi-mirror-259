from setuptools import setup, find_packages

setup(
    name='contextmenuwidget',
    version='1.0.4',
    packages=find_packages(),
    include_package_data=True,
    description='Extended widget with a context menu for tkinter, including Cut, Copy, and Paste commands.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Diablo76',
    author_email='el_diablo76@msn.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='tkinter context-menu cut copy paste',
)
