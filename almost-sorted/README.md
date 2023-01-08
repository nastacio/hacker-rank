# Problem

[https://www.hackerrank.com/challenges/almost-sorted]

## Algorithm

The algorithm here is based on the understanding that a sorted array has no "drops" (or "decreases") from one element to the next.

In other words, if we detect no adjacent elements where the first element is greater than the next, that means the array is already sorted.

## Detecting a swapped element

if an element in a sorted array was swapped between indexes _l_ and _r_, then arr[_l_] is greater than arr[_l + 1_] and arr[_r - 1_] is greater than arr[_r_].

```txt
Example of what happens when you swap the position of
two elements in a sorted array.

arr[0] arr[1] arr[2] arr[3] arr[4] arr[5] arr[6]

Now swap elements 2 and 5

arr[0] arr[1] arr[5] arr[3] arr[4] arr[2] arr[6]

                            ^^ arr[4] is greater than arr[2], not good either
              ^^ arr[5] is greater than arr[3]

```

If we swap adjacent elements, then _l + 1_ is equal to _r - 1_, which is fine. In that case, there should be only one drop between adjacent elements in the entire array.

If there are 2 (or 1) drop in the array, and the value of arr[_r_] sits between the values of arr[_l - 1_] and arr[_l + 1_] and whether the value of arr[_l_] sits between the values of arr[_r - 1_] and arr[_r + 1_], then we can conclusively say that swapping these two elements will give us a sorted array.

## Detecting a reversed range

if a whole range was reversed, the resulting array has two characteristics we are looking for:

1. Swapping the left-most and the right-most out-of-order elements in the array should result in sorted sequence around them. In other words, the right-most element should sit between the adjacent elements of the left-most element, and vice-versa.
2. The number of "drops" should be the exactly length of the swapped region. If there are other drops outside that region, that means there are other unordered elements outside the swapped region, so that a single operation will not be result in a sorted array.

