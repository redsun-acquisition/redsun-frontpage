# Other projects

This document presents a (not-so) curated list of open-source projects related to hardware control via software.

Other projects are listed in the [Smart Microscopy] website.

We're separating projects into two categories:

- "Applications": projects that provide the full functionality of a software application, comprehensive of an user interface and a set of hardware interfaces.
- "Libraries": projects that provide a set of tools for controlling hardware devices, either via scripting or via a customly developed user interface.

This list should include only projects that have been actively developed in the last 5 years.

We'll update this list as we go.

Any contribution is welcome.

## Applications

- [microscope-cockpit]: an user interface for the [microscope] library.
- [PyMoDAQ]: a Python package for controlling hardware devices via a custom user interface.
   - PyMoDAQ leverages the concept of plugins (called "modules" in PyMoDAQ), but it is tied to the Qt framework.

## Libraries

- [bluesky]: event-driven, unopinionated framework for experiment control in Python.
    - *We use this!*
- [microscope]: a Python library for control of local and remote microscope devices.
- [qudi-core]: a framework for modular multi-instrument and multi-computer measurement applications.
    - qudi-core leverages a similar approach to RedSun concept of plugins (called "addons" in qudi), but it is tied to the Qt framework.


[microscope]: https://github.com/micro-manager/microscope
[qudi-core]: https://github.com/Ulm-IQO/qudi-core
[PYME]: https://www.python-microscopy.org/
[PyMoDAQ]: https://github.com/pymodaq/pymodaq
[microscope-cockpit]: https://github.com/microscope-cockpit/cockpit
[bluesky]: https://blueskyproject.io/
[Smart Microscopy]: https://smartmicroscopy.org/resources/