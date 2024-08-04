# Radix Sort Implementation in Python

This repository contains an implementation of the Radix Sort algorithm in Python. Radix Sort is a non-comparative integer sorting algorithm that sorts data by processing individual digits of the numbers.

## Table of Contents
- [Overview](#overview)
- [Algorithm Details](#algorithm-details)
- [Complexity](#complexity)
- [Usage](#usage)
- [Code](#code)
- [Performance Test](#performance-test)

## Overview

Radix Sort is an efficient sorting algorithm that works by sorting numbers digit by digit, starting from the least significant digit to the most significant digit. It is particularly useful for sorting large lists of integers or fixed-length strings.

## Algorithm Details

The Radix Sort algorithm works as follows:

1. **Determine the maximum number of digits (k) in the largest number**: This determines the number of passes the algorithm will make over the list of numbers.
2. **Initialize digit position**: Start with the least significant digit (LSD).
3. **Sort by current digit**:
    - Use a stable sorting algorithm like counting sort to sort the array of numbers based on the current digit.
4. **Move to the next significant digit**: After sorting based on the current digit, move to the next significant digit and repeat the process.
5. **Repeat the process for each digit position**: Continue this process until all digit positions have been processed.

## Complexity

- **Time Complexity**: O(nk), where n is the number of elements, and k is the number of digits in the largest number.
- **Space Complexity**: O(n + k), accounting for the temporary storage used by the stable sorting algorithm.

## Usage

To use the Radix Sort implementation, you can simply call the `radix_sort` function with a list of integers as shown below:

```python
from radix_sort import radix_sort

items = [4, 1, 5, 3, 2]

sortItems = radix_sort(items)
print(items)  # Output: [4, 1, 5, 3, 2]
print(sortItems)  # Output: [1, 2, 3, 4, 5]

