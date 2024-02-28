from setuptools import setup,find_packages

setup(name="Mensajes-jrivera",
      version="9.0",
      description="Un paquete para saludar y despedir ",
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      author="Jaime Rivera Chávez ",
      author_email="jrivera@oceansandrivers.pe",
      url="https://www.colocarrepositoriogithub.pe",
      license_files=["LICENSE"],
      packages=find_packages(),
      scripts=[],
      test_suite="test",
      install_requires=[paquetes.strip() for paquetes in open("requirements.txt").readlines()],
      classifiers=['Environment :: Console','Intended Audience :: Developers','License :: OSI Approved :: MIT License',
                  'Operating System :: OS Independent','Programming Language :: Python','Programming Language :: Python :: 3.11',
                  'Topic :: Utilities']
      
)






