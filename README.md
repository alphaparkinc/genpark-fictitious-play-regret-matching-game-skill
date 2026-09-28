# Regret Matching Learning Dynamics Skill

Hart-Mas-Colell adaptive no-regret learning algorithm converging to the set of correlated equilibria in multi-agent games.

```mermaid
flowchart TD
    Action["Sample Action According to Positive Regret Weights"] --> Play["Observe Realized & Counterfactual Payoffs"]
    Play --> Regret["Accumulate Regrets: R_t(a) = R_{t-1}(a) + u(a) - u(a_t)"]
    Regret --> Prop["Proportional Next Strategy Assignment σ_{t+1}(a) ∝ max(0, R_t(a))"]
    Prop --> Avg["Empirical Time-Average Converges to Correlated Equilibrium"]
```

## Features
- **100% Python Standard Library**: Online \(O(1)\) state updates.
- **No-Regret Guarantee**: Average external regret approaches 0 almost surely.
- **Correlated Equilibrium Convergence**: Decentralized multi-agent coordination.
