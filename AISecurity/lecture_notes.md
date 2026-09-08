# Lecture 3 - Adversarial ML
The attacker has the power, because he/she has to find only 1 hole in the security during training or inference times.
The defender has to defend against every imaginable attack.

## Attack types
- **evasion** at inference or training time, ???
- **poisoning** at training time, maximizing loss when varying D
- **privacy attack** at inference time
    - doing model inversion to learn about the training population
    - doing model extraction to obtain the trained model's conclusions / learned cohesion

## Attacking
Can we degrade class performance arbitrarily? -> it is possible to build *"adversarial samples"* which are reasonable in the space of samples and trick the model into doing something strange / not-optimal.

Too much linearity in models gives models that are "easy to trick" because we know or can learn something about the underlying model. In that way we can trick classifiers into the wrong space on the curve by adding / subtracting a $||\delta|| \leq \epsilon$. We choose $\delta = \epsilon * sing(w)$ which gives us a change of size $w^T \delta = \epsilon * \sum_{i=1}^n |w_i| \approx \epsilon * n * m$ -> **pertubation grows linearly with the number of parameters!**.

This is called *fast gradient sign method* - quick step in the general direction of the gradient.
*projected gradient descent* is ??? the same ??? - but here we are a bit more precise and do a random walk with multiple steps in the direction of the gradient.