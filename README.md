# Learning-platform
This repository contains code me and my teammates wrote for the Penn State's on-line learning platform. The goal was to build a flexible system for generating homework assignments in Calculus (and for other subjects in the future) with output in Jupyter notebook and WebAssign.

## Python classes for Calculus
Please navigate to the `lib` folder to see code examples. In particular, `lib/f_functionclass.py` is the main class that provides flexible calls to various features and attributes of mathematical functions  (e.g. derivatives, tangent lines, min/max, etc.) needed for problems in Calculus. This class was initially built as a wrapper of many SymPy built-in methods, but we added a lot of extra functionality needed for a Calculus course.

## Parser and problem generator
We have also started developing a parser that given the plain text specifications (using a specified grammar) of a new problem in calculus would use the above Python math-function classes to automatically generate the problem in Jupyter notebook and WebAssign with a decent UI so that freshmen could easily work with it. Please navigate to `Specification_Parser_Jupiter_Loader/Parser_Compiler.ipynb` for a code example. This is currently work in progress.
