from setuptools import setup, find_packages

setup(
    name='math_quiz',             # Replace with your package name
    version='0.1',                # Choose an appropriate version number
    packages=find_packages(),
    install_requires=[
        # List any dependencies your project may have
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.quiz:main',  # Replace with the correct entry point
        ],
    },
    author='Your Name',            # Replace with your name
    author_email='your@email.com', # Replace with your email
    description='A math quiz application',  # Replace with a brief description
    url='https://github.com/samratvaddi/dsss_homework_2',  # Replace with your repository URL
    license='MIT',                # Choose an appropriate license
)
