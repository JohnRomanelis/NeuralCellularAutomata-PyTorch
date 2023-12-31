# Neural Cellular Automata - PyTorch

This work is a notebook PyTorch re-implementation of [Growing Neural Cellular Automata](https://distill.pub/2020/growing-ca/).

## Install

To run the code:

1. Clone the repo

2. CD inside the main directory and run: `pip install -e`

This project is based on [nbdev](https://nbdev.fast.ai/), so please
check their documentation for further information.

## How to read

Inside the nbs there are the notebooks that implement the proposed
method. The notebooks are numbered in ascending ordered and every
notebook uses tools developed in the previous ones.

There are 3 main experiments (using the titles from the original
version).

### 1. Learning to Grow

In this experiment we train the automato to generate from an original
state (seed) to its final form.

![Alt Text](images/grow.gif)

### 2. What Persists, Exists

In this experiment we train the automato to maintain its final form as
time passes.

![Alt Text](images/exist.gif)

### 3. Learning to Regenerate

In this experiment, we train the automaton to recover from specific
types of corruption that may be applied to it.

<div style="display: flex; justify-content: space-between;">

<img src="images/regeneration1.gif" alt="First GIF" style="width: 40%;">
<img src="images/regeneration2.gif" alt="Second GIF" style="width: 40%;">

</div>

## Notes

- In case the loss in experiments 2 or 3 is not dropping restart the
  notebook. It seems that the network converges to a local minima where
  it kills all cells from the first step and thus this state cannot
  change in the process. A possible fix would be to train the network
  solely on the growing task and then use the pool to train the model in
  achieving percistance and regenaration abilities.
