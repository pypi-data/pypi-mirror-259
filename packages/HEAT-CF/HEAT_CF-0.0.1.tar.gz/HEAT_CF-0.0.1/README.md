# HEAT-CF

### Inference of Heterogeneous perturbation Effects in single cell CRISPR screening data at single-cell resolution through Adversarial Training and Causal Forests.

### Introduction
In HEAT-CF, we formulated the perturbation analysis in single-cell CRISPR screening data as a problem of treatment effect estimation.

HEAT-CF outputs the estimation and inference of heterogeneous perturbation effects at single-cell resolution by
1. disentangling the perturbation effects from original cell-state variations based on an autoencoder framework with adversarial training;
2. growing causal forests for each perturbation and factor.

At any subpopulation level, HEAT-CF enables us to
* infer potential higher-order gene interactions,
* quantify the similarities between perturbations and prioritize the perturbation targets, either in an overall or a functional factor-specific context.
