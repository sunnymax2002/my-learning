# Basics

Below references explain about systolic arrays and Google TPU, Nvidia Tensor Core

1. [Simple and Best Animation](https://www.youtube.com/watch?v=cmy7LBaWuZ8) - here, the inputs are received in reverse order and outputs are locally stored in the PEs, and outputs do NOT propagate to the right and bottom

2. [By Ankur Mohan](https://telesens.co/2018/07/30/systolic-architectures/)

3. [A nice animation explaining the operation](https://www.youtube.com/watch?v=vADVh1ogNo0) - this adds diagram output propagation so that at the end of the operation, the outputs are available at right and bottom PEs

# Sparsity

1. [Unstructured Sparsity](https://www.youtube.com/watch?v=HDYYeDomacM)