# Problem

[https://www.hackerrank.com/challenges/matrix-rotation-algo]

## Algorithm

The idea is to break down the problem according to the picture in the problem description, one "layer" at a time.

![Example picture from the Hacker Rank problem page](main.png)

The number of layers, or "co-centric" rectangles, is the minimum between the rows and columns divided by two, rounded up.

Then we can rotate the rectangle in that layer.

```txt
Layered (or co-centric) rectangles in a 6 x 7 matrix.

L0 L0 L0 L0 L0 L0 L0
L0 L1 L1 L1 L1 L1 L0
L0 L1 L2 L2 L2 L1 L0
L0 L1 L2 L2 L2 L1 L0
L0 L1 L1 L1 L1 L1 L0
L0 L0 L0 L0 L0 L0 L0
```

With the concept of a rectangle per layer established, we can deal with each rectangle separately.

 I figured it would be tedious and
error prone to try and operate in terms of cartesian coordinates, with all the if-elses and boundary checks, so I devised an algorithm where the rectangle in each layer is serialized into a vector `v` of values, with the first element of the vector starting on the top-left of the rectangle in that layer, filled out by walking through the rectangle's perimeter clockwise, like in the example below for layer "1":

```txt
L0 L0 L0 L0 L0 L0 L0
L0 0   1  2  3  4 L0
L0 13 L2 L2 L2  5 L0
L0 12 L2 L2 L2  6 L0
L0 11 10  9  8  7 L0
L0 L0 L0 L0 L0 L0 L0
```

Now, "rotating" that layer means creating a new vector `v1` with values from vector `v`, where v1[i] with v[i+r].

To avoid wasting memory, the code does not actually create a new vector for each layer, but rather calculates the `row,column` coordinates of each index in the vector.

Once we have the `row,column` coordinates for the original element and its rotated position, we just need to assign the value of the rotated position to the new matrix, then print the final matrix.
