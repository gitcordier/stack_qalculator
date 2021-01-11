# TODOs

## Context
This application is merely developped as a *Proof of Concept*. 
We believe doing so was the best trade-off, given the small amount time we had at our disposal.

In terms of design, this meant favoring empirical hints of robustness to formal/in-depth proofs and tests. We assumed the end-user was "nice" with the software and rational.
The so "spared" time could then be injected in web interface programming: Delivering a visual and expressive product from the beginning is a key factor, which is worth the "sacrifice" of keeping (for now) a pretty rough backend.


## Further improvements.
1. start a proper and rigorous documentation of the undelying design beneath the code.
    A customary network of exceptions, if relevant, should naturally derive from the formal design.
2. Testing and improving the API "friendliness";
3. Properly define and bound the user's behavior, so that we can entirely specify the application ouputs: 
    i.in theory, through formalisation;
    ii. and practice, thanks to testing (unittest)

## Note about the Web interface
The current web interface is flawed but already provides evidence that multi-stack calculators can be delivered online with a tiny amount of code; 
which is the "**Proof of Concept** part". Furthermore, we have not a reliable API yet. So this why we would recommend the frontend developement as a second step.





