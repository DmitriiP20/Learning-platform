# Learning-platform
This repository contains code me and my teammates wrote for the Penn State's on-line learning platform. The goal was to build a flexible system for generating homework assignments in Calculus (and for other subjects in the future) with output in Jupyter notebook and WebAssign.

## Calculus objects in Python
Please navigate to the `lib` folder to see code examples. In particular, `lib/f_functionclass.py` is the main class that allows for a flexible calling of various function features and attributes (e.g. derivatives, tangent lines, etc.) needed for problems in Calculus. This object was initially built as a wrapper of many SymPy built-in methods, but we added a lot of extra functionality needed for a Calculus course.

## Parser and problem generator
We have also started developing a parser that given the specifications of a new problem in calculus would automatically generate a new Python object capable of generating the problem in Jupyter notebook and WebAssign with a decent UI so that freshmen could easily work with it. Please navigate to `Specification_Parser_Jupiter_Loader/Parser_Compiler.ipynb` for a code example. This is currently work in progress.
