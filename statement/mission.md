# The mission

The mission of Redsun is to ship not an application, but a framework that can be used to "build" applications with minimal effort.

The name is an hint to the fact that it sits "on top" of Bluesky, and tries to provide the same features:

- modularity: pick only the components you need;
- flexibility: reuse existing code;
- unopinionated: let the user decide what is data and what is metadata;
- cross-scientific: make it easy to use in different contexts.

The main language of choice is Python, specifically CPython; scientists have a high familiarity with it, it's flexible and it's easy to learn.

## Architecture

Redsun architecture is inspired by the Model-View-Controller (MVC) pattern, but with a twist: the "V" now doesn't stand for "View", but for "Virtual".

- The "Model" layer holds the logic for handling hardware controls, where each model object represents a hardware component a set of Bluesky's protocols;
- The "Controller" layer wraps the Bluesky run engine and a set of sub-controllers, where each one can provide different functionalities:
    - they can simply render information to the user interface;
    - they can ship plans that are not tied to any specific hardware component, but to protocols;
    - they can rely on information provided by other controllers or publish information themselves;
- The "Virtual" layer sits between the user interface and the two layers described above, and is responsible for handling the in-between communication.

This is because in the standard MVC pattern, there's a strong correlation between the Controller and View layers, making it difficult to tie a different front-end to the same back-end.

By decoupling this correlation, it is possible to experiment with different front-ends without having to worry about interfacing with the backend, because the Virtual layer takes care of talking to the backend for you.

## Modularity via plugins

Redsun aims to be built upon a set of plugins, each one providing a specific feature.

One of the major challenges engaged by microscopists was finding a way to reuse existing code in a consistent manner so that it wouldn't be strongly tied to their own setups. Since Bluesky gives us the possibility to speak the same language accross the whole board, we can combine different pieces of code together with different functionalities together (e.g. a plugin can ship the controls for a specific hardware component, while another plugin can ship a controller that wraps a series of executable plans not tied to any specific hardware component; and the two can be used together without any problem).

## Accross different programming languages

Python has a lot of great features but in some cases it may not compare very well with other languages in terms of performance, especially for multithreaded computations. For more information about the limitations of multithreading in Python, you can visit this [Real Python] article about the topic.

At the same time, Python interfaces naturally with languages that are able to provide that kind of performance, like C/C++ or Rust:

- For C, CPython offers the possibility to natively develop [C extensions] that can interact as a normal Python package;
- For C++, projects like [pybind11] (and most recently, [nanobind]) allow to create Python packages that provide higher performance for computational tasks;
- For Rust, the pyo3 project allows to create bindings to ship Python packages powered by Rust, which is becoming a strong and valuable alternative to the previously described languages.
- For Julia, projects like [PythonCall] make it possible to use Julia code from Python seaminglessly and with no performance penalty in data exchange between the two languages. This can lay down the basis for taking the best of both worlds: the flexibility of Python with the performance of multithreaded Julia.
- For GPU projects involving [CUDA], projects like [CuPy] allow to seaminglessly write Python code with the same syntax of NumPy, but with the benefit of being run on nVidia GPUs natively.

The list goes on and on, but the main concept to bring home is to use Redsun to "glue" all these languages together, whether it is for implementing a real-time processing task or to develop a device interface in a language that can go beyond the capabilities of Python itself.

[Real Python]: https://realpython.com/python-gil/
[C extensions]: https://docs.python.org/3/extending/extending.html
[pybind11]: https://pybind11.readthedocs.io/en/stable/index.html
[nanobind]: https://nanobind.readthedocs.io/en/latest/
[CUDA]: https://developer.nvidia.com/cuda-toolkit
[cupy]: https://cupy.dev/
[PythonCall]: https://github.com/JuliaPy/PythonCall.jl