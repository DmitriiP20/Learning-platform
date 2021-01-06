# Problem Tool Todo

- How to specify functions, from coarse to fine: 
    - random :  any random function of Function API
    - random_list: pick randomly from "curated" random list 
    - poly(n): random polynomial of degree n, random integer coeff between -5 and 5
    - poly($a_n, a_{n-1}, ..., a_0$): random polynomial of degree n, coeff for $x^k$ integer in $[-a_k,a_k]$

    - It looks like it would be good to have a more complex laguage for this, one that would allow something like ``x * sqrt(quadratic)``. We need to extend our custom parser.

- How can we allow for evaluations in `{{}}` blocks? 
    For example, we have a function `f` and a constant `a`. How can we allow access to `f(a)` in `{{}}`? 

- Allow for conditions in choices of parameters.
    Example: Have defined function `f`, want to to choose constant `a` such that `f(a) > 0`.

- Generate incorrect solutions

- From a solution description in Python (Sympy), how do we generate the necessary parameters to code the problem in WebAssign?