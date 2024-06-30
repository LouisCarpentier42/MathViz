# Random moving point

Given a four points in a 2D space, of which three points are 
static while the other one will be dynamic. At each iteration, 
one of the three static points is taken at random, and the 
dynamic point is moved towards this point. More specifically, 
a line is drawn between the dynamic point and the randomly 
selected point, and the dynamic point is moved towards the 
center of this line. That's all! We can now iterate this 
process, and see at which locations the dynamic point will be. 
Will there be any fascinating patterns? 

> This visualization was inspired by the following [Numberphile video](https://www.youtube.com/watch?v=kbKtFN71Lfs&t=458s) 

## Variations

The rule itself is actually quiet simple: select a random 
static point, and move that point towards that point. There 
are, however, some parameters that we can play with. First of
all, it is possible to have more than three static points. It
is also possible to select only 2 points, but this will simply
result in a line. Additionally, we can change how far the dynamic
point is moved. Above we said the dynamic point is moved halfway
towards the selected static point. We can also move the point
more towards the static point, or less far. 
