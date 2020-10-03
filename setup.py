from setuptools import setup, find_packages

setup(name='antistasi_phonebook_tool',
      version='0.1',
      description='',
      url='https://github.com/Giddius/Antistasi_PhoneBook_tool',
      author=['Giddi', 'Jul1a'],
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'pyperclip',
          'PyQt5'
      ],
      include_package_data=True
      )
