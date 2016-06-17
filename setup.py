from setuptools import setup, find_packages

setup(
        name='graddfil.desktop-app',
        use_scm_version=True,
        description="Desktop app for graddfil.",
        long_description=open('README.md').read(),
        classifiers=[
                    'Programming Language :: Python :: 3',
                    'Topic :: Utilities',
                ],
        keywords='graddfil quantified.self',
        author='graddfil',
        author_email='graddfril@openmailbox.org',
        url='https://github.com/graddfil/desktop-app',
        license='AGPLv3+',
        packages=find_packages(exclude=[]),
        zip_safe=True,
        setup_requires=[
                    'setuptools_scm',
                ],
        install_requires=[
                    'matrix-client == 0.0.3',
                    'confuse == 0.4.0'
                ],
        entry_points={
                    'console_scripts': [
                                    'graddfril = desktop-app.main:main',
                                ],
                })
