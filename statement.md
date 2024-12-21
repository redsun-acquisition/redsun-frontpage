# Statement of need

Scientific computing is a complex field with many different tools and libraries.
An even more complex topic is orchestrating the acquisition of custom-built hardware setups for cutting-edge scientific projects.
The desire to have a flexible framework for building custom applications for microscopy is strong in the community, but there is yet no way to find a reacheable consensus
among interested parties to develop such framework.

## History

When it comes down to hardware control for microscopes, one of the most popular choices is [Micro-Manager].

Micro-Manager is a plugin for [ImageJ] that allows to control one or multiple hardware devices to control a custom-built microscope.

In time, Micro-Manager has accumulated more than 200 device interfaces (called "device adapters") that allow to control a wide range of hardware devices.

The downside is that Micro-Manager is written in Java, and in the latest years Python has become the preferred language for scientists to work with,
especially in the field of Artificial Intelligence.

In time, a number of other projects have emerged to try and address this problem, each with their own strengths and weaknesses. You can find a (not-so) comprehensive list of projects on the [Smart Microscopy] website, together with other projects that are not listed there in this [section].

### Software for Microscopy workshop

An interesting white paper was published in april 2020, following the 


[Micro-Manager]: https://micro-manager.org/
[ImageJ]: https://imagej.net/ij/
[Smart Microscopy]: https://smartmicroscopy.org/resources/
[section]: #project-list
