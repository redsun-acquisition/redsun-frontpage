# Bluesky

The [Bluesky framework] is described as:

> a collection of Python libraries that are co-developed but independently useful and may be adopted *a la carte*.

It was developed at the National Synchrotron Light Source II (NSLS-II), in the Brookhaven National Laboratories, Uptown, New York, USA. The goal is to provide carefully defined software interfaces, where any given piece may be used, extended or replaced. They achieve this by leveraging the concept of structural duck typing in Python, to minimize the coupling between different components.

There are many useful features that Bluesky offers:

- Bluesky leaves the details of implementing hardware controls to lower level logic, while the higher level interface provides a flexible approach to recycle and reuse existing code.
- Bluesky provides a formal schema to store data and metadata in a manner defined as "unopinionated", meaning that it makes no assumption on the type of data to store, its metadata, nor the type of storage involved. This schema gives scientists the freedom to specify what is data and what is metadata without having to worry about the underlying implementation of the actual data storage format to use.
- Bluesky's run engine - a.k.a. the acquisition engine - is written upon a message protocol that allows for implement a custom run engine (which in the end is nothing more than a Python class).
- Finally, the execution of experiments is collected in so-called "plans", which are simple Python functions describing the sequence of operations to be performed via a set of Bluesky's messages; such messages are defined in a manner to be interpreted by different hardware components elegantly and easily.

Just from the description above, it is clear that Bluesky offers a list of key features highly desirable for microscopists:

- a framework that can speak the same language accross multiple groups of people;
- a modular framework that can be extended and reused;
- a framework that allows to pack workflows in a manner that can be understand both by scientists and software developers.

Furthermore, although developed in the context of beamline accelerators, Bluesky sells itself as cross-scientific, since by default it's not designed to be tied by any kind of special data structure or set of hardware components.

The question is: how can we bring this framework to the microscopy community?

[bluesky framework]: https://blueskyproject.io/