=========================
 TeaTime - Mind the tea!
=========================

TeaTime is a small application that informs you if a specified time is
over.

.. contents::

Requirements
============

You need wxPython to run TeaTime.

Install
=======

You can get and install TeaTime with `easy_install
<http://peak.telecommunity.com/DevCenter/EasyInstall>`_ ::

    $ easy_install TeaTime

Or you can get a copy of the source branch using `bzr
<http://bazaar.canonical.com/>`_ by running ::

    $ bzr branch lp:teatime

and install it with ::

    $ python setup.py install

WxPython_ is required. It has been tested with WxPython_ 2.8.10.1 on
Ubuntu Lucid Lynx.

Usage
=====

Simply start teatime via the teatime script. Use the slider set the
number of seconds when you want to get reminded.

You can click in the scrolling area to increase in steps of 30
seconds. If you want to reset the timer simply slide to zero seconds.

Contributing
============

Please submit `bugs and patches
<https://bugs.launchpad.net/teatime>`_. All contributors will be
acknowledged. Thanks!

License
=======

TeaTime is released under the GNU General Public license (GPL). See
the file ``gpl.txt`` in the distribution for details.

The icon is licensed unter a Creative Commons Attribution-Share Alike
3.0 License. I've got it from `aha-soft <www.aha-soft.com>`_.

Changelog
=========

- 0.1

  - Initial release.

To do
=====

- Windows launcher

- Self made icon

- Sit in the traybar

- Reminder through traybar popup instead of modal dialog

- Show time tea is overdue in reminder dialog

.. _WxPython: http://www.wxpython.org/
