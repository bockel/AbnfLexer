from setuptools import setup, find_packages

setup(
    name='abnflexer',
    packages=find_packages(),
    entry_points="""
[pygments.lexers]
abnflexer = abnflexer:AbnfLexer
"""
)
