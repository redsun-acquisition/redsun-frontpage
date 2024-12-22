# The mission

The mission of RedSun is to ship not an application, but a framework that can be used to "build" applications with minimal effort.

The name is an hint to the fact that it sits "on top" of Bluesky, and tries to provide the same features:

- modularity: pick only the components you need;
- flexibility: reuse existing code;
- unopinionated: let the user decide what is data and what is metadata;
- cross-scientific: make it easy to use in different contexts.

The main language of choice is Python, specifically CPython; scientists have a high familiarity with it, it's flexible and it's easy to learn.

## Architecture

RedSun architecture is inspired by the Model-View-Controller (MVC) pattern, but with a twist: the "V" now doesn't stand for "View", but for "Virtual".

- The "Model" layer holds the logic for handling hardware controls, where each model object represents a hardware component a set of Bluesky's protocols;
- The "Controller" layer wraps the Bluesky run engine and a set of sub-controllers, where each one can provide different functionalities:
    - they can simply render information to the user interface;
    - they can ship plans that are not tied to any specific hardware component, but to protocols;
    - they can rely on information provided by other controllers or publish information themselves;
- The "Virtual" layer is a layer that sits between the "Model" and the "Controller" layers, and is responsible for handling the communication with the back-end;

This is because in the standard MVC pattern, there's a strong correlation between the Controller and View layers, making it difficult to tie a different front-end to the same back-end.

By providing a virtual layer that decouples these two layers, it is possible to experiment with different front-ends without having to worry about interfacing with the back-end, because the Virtual layer takes care of talking to the back-end for you.

## Modularity via plugins

RedSun aims to be built upon a set of plugins, each one providing a specific feature.

One of the major challenges engaged by microscopists was finding a way to reuse existing code in a consistent manner so that it wouldn't be strongly tied to their own setups. Since Bluesky gives us the possibility to speak the same language accross the whole board, we can combine different pieces of code together with different functionalities together (e.g. a plugin can ship the controls for a specific hardware component, while another plugin can ship a controller that wraps a series of executable plans not tied to any specific hardware component; and the two can be used together without any problem).

## Accross different programming languages

Python has a lot of great features but in some cases it may not compare very well with other languages in terms of performance, especially for multithreaded computations.

But at the same time, it interfaces naturally with languages that are able to provide that kind of performance, like C/C++ or Rust.

Finally, projects like [PythonCall](https://github.com/JuliaPy/PythonCall.jl) make it possible to use Julia code from Python seaminglessly and with no performance penalty in data exchange between the two languages. This can lay down the basis for taking the best of both worlds: the flexibility of Python with the performance of multithreaded Julia.