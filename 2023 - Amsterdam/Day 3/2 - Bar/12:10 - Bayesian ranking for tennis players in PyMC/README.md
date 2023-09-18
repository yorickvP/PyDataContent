# Bayesian ranking for tennis players in PyMC

by [Francesco Bruzzesi](https://www.linkedin.com/in/francesco-bruzzesi/)

* [Talk info](https://amsterdam2023.pydata.org/cfp/talk/7RENTH/)
* [Code snippet](https://gist.github.com/FBruzzesi/c26a9ea5a40386e704754d95d03c488b)

## Abstract

In this talk, we will explore the Bayesian Bradley Terry model implemented in PyMC. We will focus on its application for ranking tennis players, demonstrating how this probabilistic approach can provide an accurate and robust rankings, arguably better than the ATP ranking itself and the Elo rating system.

By leveraging the power of Bayesian statistics, we can incorporate prior knowledge, handle uncertainty, and make better inferences about player abilities. Join us to learn how to implement the Bayesian Bradley Terry model in PyMC and discover its advantages for ranking tennis players.

## Description

The Bradley Terry model is a powerful model to predict the outcome of a paired comparison, as a by-product we will be able to rank players based on their hidden (latent) ability scores. Traditionally, rankings have been based on simple win-loss records, which may not capture the true abilities of players due to variations in competition quality and sample size. By adopting a Bayesian framework, we can overcome these limitations and obtain more reliable rankings.

In this talk, we will introduce the Bayesian Bradley Terry model and its underlying principles. We will explore how to encode the model in Python using the PyMC library. We will walk through the step-by-step implementation, highlighting key considerations and practical tips.

To illustrate the model's effectiveness, we will showcase its application to ranking tennis players, and compare it with both the official ATP ranking and the ELO ranking system. Tennis provides an ideal domain for this analysis, as it involves head-to-head matches between players, allowing us to directly compare their abilities. By applying the Bayesian Bradley Terry model to historical tennis match data, we can generate rankings that better reflect players' true skills, accounting for factors such as opponent strength and match surface.

Throughout the talk, we will emphasize a hands-on approach, providing code examples and demonstrations. Attendees will gain a solid understanding of the model, learn how to implement it using PyMC, a practical application, possible extensions and maybe a few PyMC tricks along the way.
