import setuptools

setuptools.setup(
    name='audio-speech-to-sign-language-converter',
    version='1.0',
    description='Python project',
    author='Vaishnavi,Vivek,Akbar',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)
