
# sortByTanvir

sortByTanvir is a Python package that provides various sorting algorithms for educational purposes. It includes the following sorting algorithms:

- Bubble Sort
- Counting Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Radix Sort
- Selection Sort

## Table of Contents
- [sortByTanvir](#sortbytanvir)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Sorting Algorithms](#sorting-algorithms)
  - [Contributing](#contributing)
  - [License](#license)

## Installation
You can install sortByTanvir via pip:

```
pip install sortByTanvir
```

## Usage
Here's an example of how to use the bubble sort algorithm:

```
from sortByTanvir import bubble_sort

arr = [12, 11, 13, 5, 6, 7]
bubble_sort(arr)
print(arr)  # sorted array
```
Here's an example of how to use the Counting sort algorithm:
```
from sortByTanvir import Counting_sort

arr = [12, 11, 13, 5, 6, 7]
Counting_sort(arr)
print(arr)  # sorted array
```

## Sorting Algorithms
Here's a brief description of each sorting algorithm:

- **Bubble Sort**: A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- **Counting Sort**: A sorting algorithm that sorts a collection of objects according to the count of a particular key value.
- **Insertion Sort**: A simple sorting algorithm that builds the final sorted array one item at a time.
- **Merge Sort**: An external algorithm based on divide and conquer strategy.
- **Quick Sort**: A divide and conquer algorithm.
- **Radix Sort**: A sorting algorithm that sorts data with integer keys by grouping keys by the individual digits that share the same significant position and value.
- **Selection Sort**: A simple sorting algorithm that sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning.

## Contributing
We welcome contributions from the community. Please submit a pull request if you have any improvements or new features to add.

## License
sortByTanvir is released under the MIT License.

