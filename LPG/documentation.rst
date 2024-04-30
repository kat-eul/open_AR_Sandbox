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

Second : In the git project, change the used branch ::

    git chechout lpg_sandbox

Third: Create a new anaconda environment::

   conda create -n sandbox-env python

Fourth: When you want to use the sandbox and the packages we are about to install you will have to activate the
environment before starting anything::

   conda activate sandbox-env

open_AR_Sandbox package
~~~~~~~~~~~~~~~~~~~~~~~
The following installation step's are the same as the original ones. You can follow the original documentation : `Installation documentation <https://github.com/cgre-aachen/open_AR_Sandbox/blob/main/docs/source/getting_started/installation.rst>`