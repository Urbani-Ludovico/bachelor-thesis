
Modello esteso
$$
    \begin{cases}
        S_{t+1} = S_t + \delta(t) S_t - \epsilon(t) S_t \\[10pt]
        P_{t+1} = P_t + \hat{\delta}(t) P_t - \beta \epsilon(t) P_t \\[10pt]
        I_{t+1} = I_t + \epsilon(t) S_t + \beta \epsilon(t) P_t - \rho I_t + \tau R_t - \sigma I_t \\[10pt]
        R_{t+1} = R_t + \rho I_t - \tau R_t - \lambda \sigma R_t
    \end{cases}
$$

Modello compatto
$$
    \begin{cases}
        S_{t+1} = S_t \left(1 + \delta(t) - \epsilon(t)\right) \\
        P_{t+1} = P_t \left(1 + \hat{\delta}(t) - \beta \epsilon(t)\right) \\
        I_{t+1} = I_t \left(1 - \rho - \sigma\right) + \epsilon(t) \left(S_t + \beta P_t\right) + \tau R_t \\
        R_{t+1} = R_t \left(1 - \tau - \lambda \sigma\right) + \rho I_t
    \end{cases}
$$