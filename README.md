SunsetClock.py
==============

Python script to count down until sundown

Sunset Clock was developed to answer the question "How long until sunset?" Sunset is a big deal at my house, we like to sit on the back porch and watch as the sun drops into the Gulf of Mexico...weather permitting.

The program can be modified to display time until any astronomical event such as sunrise, moon rise, meridian passage, RA of Aries, etc. Enter your latitude in decimal format on line 40 and your longitude on line 41.

I use a Raspberry Pi running Raspian with Python 2.7 and it works quite well. The program is written for both versions of Python and can be changed by commenting/uncommenting the appropriate lines. The code is thoroughly documented and should be easy to follow.

The dependencies are PyEphem and python-dev for either Python 2.7 or 3.x, whichever is installed on your system.

The most recent version of PyEphem may be obtained from:

http://pypi.python.org/pypi/pyephem

To install the PyEphem packages for Python 2.7 or 3.x respectively, you must first have the python-dev or python3-dev respectively installed,

Step-by-step in Terminal

1) for Python 2: sudo apt-get install python-dev

for Python 3: sudo apt-get install python3-dev

2) download the PyEphem package, Python2: http://pypi.python.org/pypi/pyephem/#downloads Python3: http://pypi.python.org/pypi/ephem/#downloads

unzip to your /tmp directory, then cd to that directory and

for Python 2.7 type: sudo python setup.py install

for Python 3.x type: sudo python3 setup.py install

Now you’re ready to use PyEphem.

To start SunsetClock;

open a Terminal cd to the folder that contains SunsetClock.py and clock1.ppm 

type: python SunsetClock.py

Note: The size of the image determines the size of the window. If the window does not fit your display, then resize the image with GIMP or ImageMagik. If you cannot see the numbers of the clock then remove some of the \n characters in line 55

This program is free, but the images may not be. You can use the image provided in this repo because it is mine and I am allowing it to be used. If you substitute the image in line 63 be sure you have the permission of the copyright holder to use their image.
