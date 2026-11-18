from math import exp
import numpy as np


def carico_periodico(t):
    """Carico 1, 0.5, 0 ripetuto ogni tre sedute."""
    return ((2 - t) % 3) / 2


def nessuna_prevenzione(t):
    """Controllo nullo"""
    return 0


class Modello:
    def __init__(
        self,
        T = 50,

        # condizioni iniziali
        S_0 = 400,
        P_0 = 100,
        I_0 = 0,
        M_0 = 0,
        F_f_0 = 0,
        F_p_0 = 0,

        # parametri del modello (valori a priori)
        alpha = 0.8,
        pi = 0.4,
        rho = 0.05,
        beta_S = 0.005,
        beta_P = 0.01,
        beta_M = 0.05,
        beta_I = 0.1,
        gamma_S = 0.02,
        gamma_P = 0.04,
        gamma_M = 0.08,
        A_max = 800,

        # parametri delle funzioni
        omega_mu = 5,
        sigma_mu = 0.15,
        sigma_nu = 0.15,
        omega_f = 0.5,
        omega_p = 0.3,
        omega_d = 0.2,
        b_lambda = 1,
        omega_r = 1,
        sigma_r = 0.05,

        # carichi
        c_f = carico_periodico,
        c_p = carico_periodico,
        # controllo: efficacia della prevenzione, tra 0 (nessuna) e 1 (perfetta)
        u = nessuna_prevenzione,
    ):
        self.T = T
        self.alpha, self.pi, self.rho = alpha, pi, rho
        self.beta_S, self.beta_P, self.beta_M, self.beta_I = beta_S, beta_P, beta_M, beta_I
        self.gamma_S, self.gamma_P, self.gamma_M = gamma_S, gamma_P, gamma_M
        self.A_max = A_max
        self.omega_mu, self.sigma_mu = omega_mu, sigma_mu
        self.sigma_nu = sigma_nu
        self.omega_f, self.omega_p, self.omega_d, self.b_lambda = omega_f, omega_p, omega_d, b_lambda
        self.omega_r, self.sigma_r = omega_r, sigma_r
        self.c_f, self.c_p = c_f, c_p
        self.u = u

        # variabili di stato per t = 0, ..., T
        self.S = np.zeros(T + 1)
        self.P = np.zeros(T + 1)
        self.I = np.zeros(T + 1)
        self.M = np.zeros(T + 1)
        self.F_f = np.zeros(T + 1)
        self.F_p = np.zeros(T + 1)
        self.S[0], self.P[0], self.I[0], self.M[0] = S_0, P_0, I_0, M_0
        self.F_f[0], self.F_p[0] = F_f_0, F_p_0

        # nuovi infortuni in ogni seduta
        self.infortuni = np.zeros(T)

    # Funzioni del modello
    def mu(self, x):
        return self.omega_mu * exp(- x ** 2 / (2 * self.sigma_mu ** 2))

    def nu(self, x, beta):
        return beta * exp(- (x - 1) ** 2 / (2 * self.sigma_nu ** 2))

    def lam(self, f_f, f_p, d, gamma):
        return gamma / (1 + exp(- self.omega_f * f_f - self.omega_p * f_p - self.omega_d * d + self.b_lambda))

    def r(self, t):
        return 2 * self.omega_r / (1 + exp(self.sigma_r * t))

    def rischio(self, t):
        """Rischio relativo lambda / gamma"""
        return self.lam(self.F_f[t], self.F_p[t], (self.S[t] + self.P[t] + self.M[t]) / self.A_max, 1)

    # Simulazione
    def compute(self):
        for t in range(self.T):
            S, P, I, M = self.S[t], self.P[t], self.I[t], self.M[t]

            rischio = (1 - self.u(t)) * self.rischio(t)

            inf_S = self.gamma_S * rischio * S
            inf_P = self.gamma_P * rischio * P
            inf_M = self.gamma_M * rischio * M
            self.infortuni[t] = inf_S + inf_P + inf_M

            self.S[t + 1] = S + self.alpha * self.mu(t / self.T) - self.nu(t / self.T, self.beta_S) * S - inf_S
            self.P[t + 1] = P + (1 - self.alpha) * self.mu(t / self.T) - self.nu(t / self.T, self.beta_P) * P - inf_P
            self.I[t + 1] = I + self.pi * (inf_S + inf_P + inf_M) - self.rho * I - self.nu(t / self.T, self.beta_I) * I
            self.M[t + 1] = M + (1 - self.pi) * (inf_S + inf_P) - self.pi * inf_M + self.rho * I - self.nu(t / self.T, self.beta_M) * M
            self.F_f[t + 1] = self.F_f[t] + self.c_f(t) - self.r(t) * self.F_f[t]
            self.F_p[t + 1] = self.F_p[t] + self.c_p(t) - self.r(t) * self.F_p[t]

            if min(self.S[t + 1], self.P[t + 1], self.I[t + 1], self.M[t + 1]) < 0:
                raise ValueError(f"Popolazione negativa al tempo {t + 1}.")
        return self

    @property
    def N(self):
        """Popolazione totale."""
        return self.S + self.P + self.I + self.M
