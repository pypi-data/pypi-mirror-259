from setuptools import setup

setup(
    name='dunkin-bot',
    version='1.0.0',
    py_modules=['main'],
    install_requires=[
        'PyPDF2',
        'pyttsx3',
        'SpeechRecognition',
        'nltk',
        'openai',
        'spacy',
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'dunkin-bot=main:create_gui',
        ],
    },
)
