import numpy as np
from math import exp
import matplotlib.pyplot as plt

class Modello:
    def __init__(
            self,
            T: int = 50,
            S_0: float = 400,
            P_0: float = 100,
            I_0: float = 0,
            M_0: float = 0,
            F_f_0: float = 0,
            F_p_0: float = 0,

            alpha: float = 0.8,
            pi: float = 1/3,
            rho: float = 0.1,
            beta_S: float = 0.1,
            beta_P: float = 0.15,
            beta_I: float = 0.3,
            beta_M: float = 0.2,
            gamma_S: float = 0.005,
            gamma_P: float = 0.02,
            gamma_M: float = 0.05,
            A_max: float = 800,

            #mu
            omega_mu: float = 10,
            sigma_mu: float = 0.2,

            # nu
            sigma_nu: float = 0.2,

            # lambda
            omega_f: float = 0.5,
            omega_p: float = 0.3,
            omega_d: float = 0.2,
            b_lambda: float = 2,

            # r
            omega_r: float = 1,
            sigma_r: float = 0.2
        ):
        self.T = T

        self.S = np.zeros(T + 1, dtype = float)
        self.S[0] = S_0
        self.P = np.zeros(T + 1, dtype = float)
        self.P[0] = P_0
        self.I = np.zeros(T + 1, dtype = float)
        self.I[0] = I_0
        self.M = np.zeros(T + 1, dtype = float)
        self.M[0] = M_0
        self.F_f = np.zeros(T + 1, dtype = float)
        self.F_f[0] = F_f_0
        self.F_p = np.zeros(T + 1, dtype = float)
        self.F_p[0] = F_p_0

        self.N0 = S_0 + P_0 + I_0 + M_0

        self.alpha = alpha
        self.pi = pi
        self.rho = rho
        self.beta_S = beta_S
        self.beta_P = beta_P
        self.beta_I = beta_I
        self.beta_M = beta_M
        self.gamma_S = gamma_S
        self.gamma_P = gamma_P
        self.gamma_M = gamma_M
        self.A_max = A_max

        # mu
        self.omega_mu = omega_mu
        self.sigma_mu = sigma_mu

        # nu
        self.sigma_nu = sigma_nu

        # lambda
        self.omega_f = omega_f
        self.omega_p = omega_p
        self.omega_d = omega_d
        self.b_lambda = b_lambda

        # r
        self.sigma_r = sigma_r
        self.omega_r = omega_r


    def mu(self, x) -> float:
        return self.omega_mu * exp(- (x ** 2) / (2 * (self.sigma_mu ** 2)))

    def nu(self, t, beta = 0.5) -> float:
        return beta * exp(- ((t - 1) ** 2) / (2 * (self.sigma_nu ** 2)))

    def lam(self, f_f, f_p, d, gamma) -> float:
        return gamma / (1 + exp(- self.omega_f * f_f - self.omega_p * f_p - self.omega_d * d + self.b_lambda))

    def c(self, t) -> float:
        if t % 3 == 0:
            return 1
        elif t % 3 == 1:
            return 0.5
        else:
            return 0

    def r(self, t) -> float:
        return 2 * self.omega_r / (1 + exp(self.sigma_r * t))

    def S_step(self, t):
        self.S[t] = self.S[t - 1] \
            + self.alpha * self.mu((t - 1) / self.T) \
            - self.nu((t - 1) / self.T, self.beta_S) * self.S[t - 1] \
            - self.lam(self.F_f[t - 1], self.F_p[t - 1], (self.S[t - 1] + self.P[t - 1] + self.M[t - 1]) / self.A_max, self.gamma_S) * self.S[t - 1]

    def P_step(self, t):
        self.P[t] = self.P[t - 1] \
            + (1 - self.alpha) * self.mu((t - 1) / self.T) \
            - self.nu((t - 1) / self.T, self.beta_P) * self.P[t - 1] \
            - self.lam(self.F_f[t - 1], self.F_p[t - 1], (self.S[t - 1] + self.P[t - 1] + self.M[t - 1]) / self.A_max, self.gamma_P) * self.P[t - 1]

    def I_step(self, t):
        self.I[t] = self.I[t - 1] \
            + self.pi * self.lam(self.F_f[t - 1], self.F_p[t - 1], (self.S[t - 1] + self.P[t - 1] + self.M[t - 1]) / self.A_max, self.gamma_S) * self.S[t - 1] \
            + self.pi * self.lam(self.F_f[t - 1], self.F_p[t - 1], (self.S[t - 1] + self.P[t - 1] + self.M[t - 1]) / self.A_max, self.gamma_P) * self.P[t - 1] \
            + self.pi * self.lam(self.F_f[t - 1], self.F_p[t - 1], (self.S[t - 1] + self.P[t - 1] + self.M[t - 1]) / self.A_max, self.gamma_M) * self.M[t - 1] \
            - self.rho * self.I[t - 1] \
            - self.nu((t - 1) / self.T, self.beta_I) * self.I[t - 1]
        
    def M_step(self, t):
        self.M[t] = self.M[t - 1] \
            + (1 - self.pi) * self.lam(self.F_f[t - 1], self.F_p[t - 1], (self.S[t - 1] + self.P[t - 1] + self.M[t - 1]) / self.A_max, self.gamma_S) * self.S[t - 1] \
            + (1 - self.pi) * self.lam(self.F_f[t - 1], self.F_p[t - 1], (self.S[t - 1] + self.P[t - 1] + self.M[t - 1]) / self.A_max, self.gamma_P) * self.P[t - 1] \
            - self.pi * self.lam(self.F_f[t - 1], self.F_p[t - 1], (self.S[t - 1] + self.P[t - 1] + self.M[t - 1]) / self.A_max, self.gamma_M) * self.M[t - 1] \
            + self.rho * self.I[t - 1] \
            - self.nu((t - 1) / self.T, self.beta_M) * self.M[t - 1]

    def F_f_step(self, t):
        self.F_f[t] = self.F_f[t - 1] \
            + self.c(t - 1) \
            - self.r(t - 1) * self.F_f[t - 1]
        
    def F_p_step(self, t):
        self.F_p[t] = self.F_p[t - 1] \
            + self.c(t - 1) \
            - self.r(t - 1) * self.F_p[t - 1]

    def compute(self):
        for t in range(1, self.T + 1):
            self.S_step(t)
            self.P_step(t)
            self.I_step(t)
            self.M_step(t)
            self.F_f_step(t)
            self.F_p_step(t)

            if self.S[t] < 0 or self.P[t] < 0 or self.I[t] < 0 or self.M[t] < 0 or self.F_f[t] < 0 or self.F_p[t] < 0:
                raise ValueError("Negative values in the model state variables.")

