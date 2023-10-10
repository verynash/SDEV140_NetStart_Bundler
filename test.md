# Testing and Validation

## Imports
The first import is one of Python's testing modules, [unittest].
The second is the source code for my final project.

## Testing
Using unittest, an assertion is made declaring the expected result of each estimate. Each estimate method is given two tests to determine accuracy. The first tests the most cost-effective option for the service package. The second is an expensive option that uses a different value for each available customization to the package.

## Fixes
By testing multiple values for each package, I was able to find multiple instances of incorrect pricing. All were due to incorrect values being placed in the algorithm that calculated the price. Eventually I was able to get rid of all known bugs. 