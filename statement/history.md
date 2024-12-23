# History

## State of the art

For open-source projects, when it comes down to hardware control for microscopes, one of the most popular choices is [Micro-Manager] [^1].

Micro-Manager is a plugin for [ImageJ] [^2] that allows to control one or multiple hardware devices to control a custom-built microscope, and offers a great amount of plugins to extend its functionalities to combine data acquisition with real-time processing.

In time, Micro-Manager has accumulated more than 200 device interfaces (called "device adapters") that allow to control a wide range of hardware devices. You can view the full selection of available devices in the  [mmCoreAndDevices] repository.

One of the downsides is that Micro-Manager is written in Java, and in the latest years Python has become the preferred language for scientists to work with,
especially in the field of Artificial Intelligence.

In time (particularly in the last few years), a number of other projects have emerged to try and address this problem, each with their own strengths and weaknesses, and some of them tied in some capacity to Micro-Manager: either via [pymmcore], the Python bindings for the C++ backend of Micro-Manager, or [Pycro-Manager], a Python library that provides direct communication with the Micro-Manager application via IPC (Inter-Process Communication). It's not uncommon that when a new software project is released, users tend to ask the question "can I use this with Micro-Manager?", and the answer determines the appeal the project will have.


You can find a (not-so) comprehensive list of projects on the [Smart Microscopy] website, together with other projects that are not listed there in this [section].

## Software for Microscopy workshop

In April 2020, a [white paper] [^3] was published following the Software for Microscopy workshop organized at the Janelia Research Campus, Virginia, USA. A group of research experts in the field of microscopy gathered together to discuss the current state of the art in microscopy software, evaluating its current challenges and limitations.

```{note}
TLDR:

- There is a need for a modular framework that can be used to build custom applications for microscopy.
- The framework should be easy to use and understand, and should be able to be used by different groups of experts.
- The framework should be able to be used to control a wide range of hardware devices.
- The framework should be able to be used to build custom applications for microscopy.
- The framework should allow easy creation and customization of execution workflows.
- The framework should be able to be used from multiple programming languages to ensure longevity of the software.
```

An excerpt of the white paper reports the considerations made by the participants in relation to the current state of the art of available hardware control software:

> An overwhelming majority of the participants were unhappy with their current approach. General sentiments were that it is often easier to build the hardware of a new microscope system compared to writing the software. Therefore, software development is often seen as a necessary burden to accomplish the goal of creating a new microscope system. In many cases sharing the software code proves difficult due to:
> 1. licensing issues, 
> 2. code that was written with a very specific microscope system in mind, thus being tightly coupled to specific hardware, 
> 3. a need to use different programming languages, 
> 4. existing code being difficult to understand, maintain and/or extend.

Continuing, the white paper reports the desires of the participants:

> At least three distinct groups of experts are involved in custom-build microscopes: optics experts building the microscope hardware, software developers creating the control software and UI, and the scientists using the systems in their research. 
> - There is an overarching desire for tools that are easy to use and understand to each of these groups. 
> - This brings the need for modular tools; components with limited scope that can be used in isolation and that are well described and well-documented. 
>   - Hardware developers need building blocks that can communicate to all commonly used hardware components, must be able to specify hardware based synchronization of components, execute different orders of component state changes, acquire images through cameras, point scanners, or small area detectors, view images, and loop analysis results back into the acquisition engine. 
>   - Software developers will need to develop, test, document, and support these tools, while the scientists using these tools will provide invaluable feedback to make the control software more versatile and robust.
>   - Scientists using the microscope systems highly benefit from User Interfaces that clearly guide them along the most optimal workflows. These workflows may be different depending on the microscope system and the specific experiments they are conducting. In addition, they need easy tools to change the workflow, for instance by scripting or visual programming tools. 

Furthermore, concerning programming languages, the white paper reports the following:

> We are in the midst of a diversification of programming languages used by imaging software tool developers. Whereas previously much development occurred in Java, currently Python (among others like Julia) is gaining traction. [...] Therefore, the to-be-developed modular software building blocks for microscope control should be usable from multiple programming languages to ensure longevity of these tools.

## References

[^1]: Arthur D Edelstein, Mark A Tsuchida, Nenad Amodaj, Henry Pinkard, Ronald D Vale, and Nico Stuurman (2014), Advanced methods of microscope control using μManager software. *Journal of Biological Methods* 2014 [doi:10.14440/jbm.2014.36](https://doi.org/10.14440/jbm.2014.36)
[^2]: Schneider, C., Rasband, W. & Eliceiri, K. NIH Image to ImageJ: 25 years of image analysis. *Nat Methods 9*, 671–675 (2012). [doi:10.1038/nmeth.2089](https://doi.org/10.1038/nmeth.2089)
[^3]: Software for Microscopy workshop (2020), White paper. [arXiv:2005.00082](https://doi.org/10.48550/arXiv.2005.00082)

[Micro-Manager]: https://micro-manager.org/
[mmcoreanddevices]: https://github.com/micro-manager/mmCoreAndDevices
[ImageJ]: https://imagej.net/ij/
[Smart Microscopy]: https://smartmicroscopy.org/resources/
[section]: #../project-list
[pymmcore]: https://github.com/micro-manager/pymmcore
[pycro-manager]: https://github.com/micro-manager/pycro-manager
[white paper]: https://arxiv.org/abs/2005.00082

