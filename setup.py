import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.PRScomplaint',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='Hello! This app will help you file a Problem Resolution System (PRS) Complaint with the Massachusetts Department of Elementary & Secondary Education (DESE). A PRS Complaint asks the Massachusetts DESE to fix concerns that a person has about a student’s suspension from school.\r\n\r\nA PRS Complaint describes:\r\n\r\nWhat the school did about the suspension;\r\nWhether the parent/guardian was notified about the suspension; and\r\nWhat concerns the person filing the complaint has about the student’s suspension\r\nThe Massachusetts DESE must look at your PRS Complaint and send a letter deciding what should happen to resolve the problem within 60 days.\r\n\r\nThe app will ask some questions to make sure a PRS Complaint is the right form for you to complete. After that, it will ask for basic contact information from you, details about what happened with the student’s suspension, and then create a PRS Complaint for you to send to the Massachusetts DESE.',
      long_description_content_type='text/markdown',
      author="Mike O'Dea",
      author_email='modea@suffolk.edu',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/PRScomplaint/', package='docassemble.PRScomplaint'),
     )

