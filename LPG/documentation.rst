Installation
============

First of all you will need a healthy `Python 3 <https://www.python.org/>`_ environment. We recommend using
`Anaconda <https://www.anaconda.com/>`_. In addition to some standard `Python 3 <https://www.python.org/>`_ packages,
you will need a specific setup dependent on the Kinect version you are using. In the following we provide detailed
installation instructions.

open_AR_Sandbox package
~~~~~~~~~~~~~~~~~~~~~~~

Download or clone this repository `open_AR_Sandbox <https://github.com/kat-eul/open_AR_Sandbox/tree/lpg_sandbox>`_ from GitHub.

First: Clone the repository::

   git clone https://github.com/kat-eul/open_AR_Sandbox.git

Second: Enter the new downloaded project folder::

    cd open_AR_Sandbox

Third : In the git project, change the used branch ::

    git chechout lpg_sandbox

Fourth: Create a new anaconda environment::

   conda create -n sandbox-env python

Fifth: When you want to use the sandbox and the packages we are about to install you will have to activate the
environment before starting anything::

   conda activate sandbox-env

Following steps
~~~~~~~~~~~~~~~
The following installation step's are the same as the original ones. You can follow the original documentation without cloning the original repository : `Installation documentation <https://github.com/cgre-aachen/open_AR_Sandbox/blob/main/docs/source/getting_started/installation.rst>`_

Desktop Shortcuts
=================
Changing the paths in the .sh scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are 4 files to change : `start_sandbox.sh <https://github.com/kat-eul/open_AR_Sandbox/blob/lpg_sandbox/LPG/start_sandbox.sh>`_, `start_projector_calibration.sh <https://github.com/kat-eul/open_AR_Sandbox/blob/lpg_sandbox/LPG/start_projector_calibration.sh>`_, `start_sensor_calibration.sh <https://github.com/kat-eul/open_AR_Sandbox/blob/lpg_sandbox/LPG/start_sensor_calibration.sh>`_ and `close_server.sh <https://github.com/kat-eul/open_AR_Sandbox/blob/lpg_sandbox/LPG/close_server.sh>`_.
In each .sh scripts, you will need to change <Path to the git project> by the absolute path to the git project.
Also, <Path to the panel command> must be changed by the path to the panel command. You can search it in your personal files, in general, it will be located in the following folder : ~/.config/jupyterlab-desktop/jlab_server/bin/.

Changing the paths in the .desktop scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are 4 files to change : `open_AR_sandbox.desktop <https://github.com/kat-eul/open_AR_Sandbox/blob/lpg_sandbox/LPG/desktop_files/open_AR_sandbox.desktop>`_, `projector_calibration.desktop <https://github.com/kat-eul/open_AR_Sandbox/blob/lpg_sandbox/LPG/desktop_files/projector_calibration.desktop>`_, `sensor_calibration.desktop <https://github.com/kat-eul/open_AR_Sandbox/blob/lpg_sandbox/LPG/desktop_files/sensor_calibration.desktop>`_ and `close_server.desktop <https://github.com/kat-eul/open_AR_Sandbox/blob/lpg_sandbox/LPG/desktop_files/close_server.desktop>`_.
In each .desktop scripts, you will need to change <Path to the git project> by the absolute path to the git project.
You can then move thoses files on your Desktop. Then, you will need to right click on each file and select `Allow execution`.
If you want to change the icon, juste change `None` by the absolute path to your icon.