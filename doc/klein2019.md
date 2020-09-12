# The Stroke Correspondence Problem, Revisited
Notes on [2019 paper](https://arxiv.org/abs/1909.11995) by Dominik Klein. This paper tackles the [problem introduced in 1996](file:///Users/atsukoshimizu/Downloads/e79-d_5_529.pdf) by Wakahara.

## The Stroke Correspondence Problem
This section discusses the original 1996 problem statement.
* A *stroke* is a set of `(x,y)` points
* *w.l.o.g*: without loss of generality (means it is ok to assume a value for a variable to solve this problem)
* At a high level, we are trying to find a pair of kanji, the input and a *template kanji* among many possible template kanji, with minimal *distance* (they define the distance function).
    * The comparison is done between input and template kanji with the same number of strokes
    * **Limitations of this approach**
        * Input and template must have same number of strokes. However, people can draw the same kanji differently, such as merging strokes for speed.
* *bijective function*: one-to-one function, "each element of one set is paired with exactly one element of the other set, and each element of the other set is paired with exactly one element of the first set"
    * The *minimizing function* should be bijective and should be independent of stroke order
* *surjective function*: onto function, for every element in the output, there is an input. Two different inputs can have the same outputs.
    * In this paper, the bijective requirement is relaxed with a surjective function

### Stroke Distance Functions 1996
* Old distance functions used in the 1996 paper:
    * *Endpoint*: add up the differences between x and y coordinates between two strokes.
    * *Initial Stroke*: similar to Endpoint but you multiply the sum by `n/m` (where stroke 1 has `n` points, and stroke 2 has `m` points)
    * *Whole-whole Stroke*: changes the value that the x cooridinate is subtracted with
* **Limitations of above functions** are that there was no notion of *direction*, which is helpful to distinguish kanjis with very few strokes.

### Directional Stroke Distance 2019
* Adds subtracting the x coordinate with the previous x coordinate witin the same stroke (and taking the absolute value of the results).

## Normalization Methods
*Image normalization*: fitting an image of with width `w_1` and height `h_1` into a predefined size `w_2` and `h_2`.
    * Defines kanji as a *binary image* (an imagine with only two colors) function `f(x,y)`
* *Linear*: `x' = x*w_2/w_1` (also do this for y coordinate, except with height instead of width). So basically multiply by the target dimension, and divide by the original dimension
    * This preserves the *aspect ratio*
    * (Stopped at Linear Normalization, Sept 12, 2020)
