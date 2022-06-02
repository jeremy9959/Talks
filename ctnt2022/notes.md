===
"classical L2 fourier analysis"

G is the circle group (complex numbers of norm 1 for example) e^(i theta) for theta in [0,2pi)  H(G) is the L2 hilbert space of complex valued functions on G.
Inner product <f,g> given by integration of fgbar
H*(G) is the dual of this Hilbert space; any linear form is dot product with a function k.

continuous Characters of G are the functions e^{in theta} for n in Z, so the "character group" is the group Z.

An element of the dual H^* gives a function on the character group by

hat(lambda)(n) = lambda(chi_n).

Since lambda(f) = <f,\lambda> we see that the fourier coefficients are the "function" on the character group.

===
"finite groups"

G an abelian group.  hat{G} = Hom(G, C^*) space of characters, also a group; same number of elements as G.
F(G) the complex functions on G.
Dual of F(G) yields functions on hat(G).
element of F(G) is linear combination of characters

===
p-adic case

G is the group Zp
We are interested in the space of continuous Qp valued functions on G (or possibly K valued functions where K is a complete extension of Qp).
Inside this space we have the continuous homomorphisms (or characters) from Zp to K^*
We want to study the continuous dual of this space, called the space of p-adic measures.

====
continuous Qp-valued functions on Zp: C(Zp, Qp).
examples:
    - locally constant functions
    - polynomial functions
    - locally polynomial functions
norm given by the "sup norm".
This is a Qp-vector space with a norm and it is *complete* (a p-adic Banach space). (This is a general fact from 
the theory of metric spaces: if X is a compact metric space and Y is a complete metric space then the space of continuous functions from X to Y,
with the sup norm, is complete. Sketch: 
- compactness means continous functions are bounded so the sup norm for any function is attained
- cauchy sequence f_n converges pointwise to f by completeness of Y
- cauchy property implies convergence of f_n to f is uniform, so f is continuous
- uniform convergence is the same as convergence in the sup norm so f is the limit of f_n in the sup norm as well.
)

Distributions are the continuous linear maps C(Zp,Qp) to Qp
Characters are the continuous homomorphisms Zp to Qp^*

===========
Mahler's Theorem

- binomial polynomials x;n
- integer values on Z
- p-adic integer values on Zp

finite differences:
f:Z\to Z
Del(f)=f(x+1)-f(x)
Del(f)_0 = f(1)-f(0)
Del^2(f)_0 = f(x+2)-2f(x+1)+f(x)|x=0 = f(2)-2f(1)+f(0)
Del^3(f)_0 = f(3)-3f(2)+3f(1)-f(0)
...

Del(x;n) = (x+1;n)-(x;n)=(x;n-1)
(1+Delta)f_0 = f(1)
(1+Delta)^Nf_0=f(N)
Theorem (originally Newton)
f(x) = sum Delta^i(f(x))_(x=0)(x;i)

p-adic version

f=sum Delta^i_0 f(x) (x;i), coefficients go to zero

Proof: 
-  sup of Delta^i f smaller than sup of Delta^(i-1)f
-  consider Delta^(p^r)f(x)

Explicit picture of C(Zp,Qp) as a space of sequences of a_n going to zero p-adically.
====
Distributions

Continuous linear functional determined by its values on (x;n); must be bounded; by continuity 
the space of distributions are the bounded sequences.
====
Characters

Hom(Zp,Qp*) continous determined by where 1 goes.  1 has to go to a value a where  a^n is bounded and "makes sense" for n in Zp.
Only works if a is congruent to 1 mod p.

On the other hand, we have padic logarithm and exponential

f(n) = exp(n log a)
a congruent to 1 means log(a) divisible by p so n log a divisible by p so exp(n log a) makes sense
Alternatively
a=1+x
(1+x)^n = sum (n;i)x^i
is a continuous function on Zp provided |x|<1.

Characters of Zp are therefore 1+pZp.

If lambda is a distribution then lambda((1+x)^n) = lambda(sum (n;i)x^i)=sum(x^i lambda(n;i)) which we can think of as evaluation of a power series sum a_n T^n with bounded coefficients.

If f(x)=x, then the value of the distribution is the coefficient of T, which is dF/dT at T=0.
If f(x)=x^2, then x^2=(x;2)
===
The Iwasawa Algebra

distributions on a group form a ring under convolution.
The ring here is the ring of formal power series with bounded coefficients.
Evaluation a function f(T) at a point x  in pZp corresponds to "integrating the character (1+x)^n against the distribution"

Dirac distribution: Fourier transform of a Dirac distribution at a is the series (1+T)^a 

\int_{Zp} a^n d\lambda(a) = ((1+T)\partial/\partial T)^n F_{\lambda}(T)|_{T=0}


====
Applications: Kubota-Leopoldt zeta function

Mellin Transform

G=Zp^*
X = Hom(Zp^*, Qp^*)

Zp^* = mu_{p-1} \times 1+pZp

1+pZp isomorphic to pZp=Zp via logarithm/exponential






















