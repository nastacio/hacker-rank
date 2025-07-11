#!/bin/python3

import math
import os

def getMinBatchSize(dataSamples: list, maxBatches: int) -> int:
    """
    Calculate the minimum batch size required to process all data samples.

    data samples from different array elements cannot be mixed with data samples
    from other array elements. Each data sample must be processed in its own batch.

    :param dataSamples: List of integers representing the size of each data sample
    :param maxBatches: Maximum number of batches allowed
    :return: Minimum batch size required to process all data samples
    """

    # First, assume the best case scenario where all batches could be
    # completely filled.
    sampleCount = sum(dataSamples)
    batchMinSize = math.ceil(sampleCount / maxBatches)

    # Second, calculate the number of batches required to send
    # the data samples in each array element, and fill up all those
    # batches
    maxBatchFull = 0
    for ds in dataSamples:
        maxBatchFull += math.ceil(ds / batchMinSize) * batchMinSize
    
    # Now we have the max carrying capacity of all batches, so
    # the actual minimum size is that carrying capacity (accounting
    # for partially empty batches) divided by the maximum number of batches.
    result = math.ceil(maxBatchFull / maxBatches)
    return result


if __name__ == '__main__':
    maxBatches = int(input().strip())
    dsSize = int(input().strip())
    dataSamples = []
    for i in range(dsSize):
        ds = int(input().strip())
        dataSamples.append(ds)

    print(dataSamples)
    result = getMinBatchSize(dataSamples, maxBatches)

    print(result)
