
# Modello

Modellizzazione di un periodo di allenamento di atleti di judo. Si hanno le seguenti ipotesi iniziali:

- Il tempo è limitato su $[0, T]$ e si suppone che gli allenamenti $t$ siano circa distribuiti omogeneamente nel tempo.
- La popolazioni di atleti è omogenea.
- Si parla prevalentemente di atleti non alle prime armi, quindi con possibili infortuni pregressi $P$.
- Il carico di allenamento non è costante: può essere nullo (es. sessione di recupero), inferiore al massimo (es. lavoro tecnico), oppure overtraining.
- Essendo il tempo limitato, si suppone che non ci sia abbastanza tempo affinché un atleta malconcio possa tornare in $S$ o in $P$.


Modello esteso
$$
    \left\lbrace\begin{align*}
        S(t+1) &= S(t) \\
            &+ \alpha \mu\left(\frac{t}{T}\right) \\
            &- \nu\left(\frac{t}{T}, \beta_S\right) S(t) \\
            &- (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_S\right) S(t) \\

        P(t+1) &= P(t) \\
            &+ (1 - \alpha) \mu\left(\frac{t}{T}\right) \\
            &- \nu\left(\frac{t}{T}, \beta_P\right) P(t) \\
            &- (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_P\right) P(t) \\

        I(t+1) &= I(t) \\
            &+ \pi (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_S\right) S(t) \\
            &+ \pi (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_P\right) P(t) \\
            &+ \pi  (1 - u(t))\lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_M\right) M(t) \\
            &- \rho I(t) \\
            &- \nu\left(\frac{t}{T}, \beta_I\right) I(t) \\

        M(t+1) &= M(t) \\
            &+ (1 - \pi) (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_S\right) S(t) \\
            &+ (1 - \pi) (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_P\right) P(t) \\
            &- \pi (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_M\right) M(t) \\
            &+ \rho I(t) \\
            &- \nu\left(\frac{t}{T}, \beta_M\right) M(t) \\
        
        \bar{F}_f(t+1) &= \bar{F}_f(t) \\
            &+ c_f(t) \\
            &- r_f\left(t, \bar{F}_f(t)\right) \\

        \bar{F}_p(t+1) &= \bar{F}_p(t) \\
            &+ c_p(t) \\
            &- r_p\left(t, \bar{F}_p(t)\right)
    \end{align*}\right.
$$

$t$: unità di tempo

$T$: tempo massimo


## Popolazioni

- $S$: sani
- $P$: atleti con infortuni pregressi
- $I$: infortunati (non si possono allenare)
- $M$: malconci (si possono allenare)
- $\bar{F}_f$: fatica fisica media del gruppo
- $\bar{F}_p$: fatica psicologica media del gruppo


## Parametri

- $\mu\left(\frac{t}{T}\right)$: funzione di crescita della popolazione alla frazione di tempo $\frac{t}{T}$
- $\nu\left(\frac{t}{T}, \beta_\cdot\right)$: funzione di decrescita della popolazione alla frazione di tempo $\frac{t}{T}$ con peso $\beta_\cdot$
- $\alpha$: percentuale di effetto della crescita sulla popolazione sana
- $\beta_\cdot$: moltiplicatore per la decrescita sulla popolazione a cui è riferita
- $\gamma_\cdot$: moltiplicatore di rischio per la funzione di infortunio sulla popolazione a cui è riferita
- $\lambda\left(\bar{F}_f(t), \bar{F}_p(t), \gamma_\cdot\right)$: funzione di probabilità dell'infortunio al tempo $t$ con peso $\gamma_\cdot$
- $\pi$: probabilità che l'infortunio sia di tipo grave ($I$) invece che malconcio ($M$)
- $u(t)$: termine di controllo, influenza dell'allenatore sulla prevenzione da infortuni
- $\rho$: tasso di transizione da $I$ a $M$
- $c_\cdot(t)$: funzione di carico della seduta di allenamento al tempo $t$ (0: riposo, 1: carico massimo, >1: overtraining)
- $r_\cdot\left(t, \bar{F}_\cdot(t)\right)$: recupero medio al tempo $t$
- $A_{\max}$: numero massimo di atleti sul tatami affinché l'allenamento sia sicuro e il rischio di collisione sia basso


## Ipotesi

- $\mu: [0, 1] \longrightarrow [0, +\infty)$
- $\nu: {[0, 1]}^2 \longrightarrow [0, 1]$
- $\alpha \in [0, 1]$
- $\beta_S, \beta_P, \beta_I, \beta_M \in [0, +\infty)$
- $\gamma_S, \gamma_P, \gamma_M \in [0, +\infty)$
- $\lambda: {[0, +\infty)}^4 \longrightarrow [0, 1]$
- $\pi \in [0, 1]$
- $u: [0, T] \longrightarrow [u_{\min}, 1]$
- $u_{\min} \in [0, 1]$
- $\rho \in [0, 1]$
- $c_f, c_p: [0, T] \longrightarrow [0, +\infty)$
- $r_f, r_p: [0, T] \longrightarrow [0, 1]$
- $A_{\max} \in [1, +\infty)$

Vincoli:

- Popolazione $S$
    $$
        \nu\left(\frac{t}{T}, \beta_S\right) + (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_S\right) \leq 1
    $$
- Popolazione $P$
    $$
        \nu\left(\frac{t}{T}, \beta_P\right) + (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_P\right) \leq 1
    $$
- Popolazione $I$
    $$
        \rho + \nu\left(\frac{t}{T}, \beta_I\right) \leq 1
    $$
- Popolazione $M$
    $$
        \nu\left(\frac{t}{T}, \beta_M\right) + \pi (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_M\right) \leq 1
    $$

Ipotesi per la funzione di accumulo della fatica:

- Mescolamento: durante l'allenamento gli accoppiamenti cambiano frequentemente e in modo casuale, quindi ogni atleta interagisce in media con partner rappresentativi della fatica media del gruppo. Questo giustifica l'uso di $\bar{F}_f(t)$ e $\bar{F}_p(t)$ al posto delle fatiche individuali.
- Simmetria: l'infortunio può capitare sia a chi è stanco sia al partner fresco, quindi la fatica rilevante è quella dell'incontro, non del singolo.
- Gruppi non piccoli: il gruppo deve essere sufficientemente numeroso e omogeneo da rendere la media stabile e rappresentativa.

Altre ipotesi:

- Monotonia di $\lambda$: la funzione di infortunio $\lambda$ è crescente rispetto a $\bar{F}_f(t)$ e $\bar{F}_p(t)$.
- La densità di atleti $\frac{S(t) + P(t) + M(t)}{A_{\max}}$ è la percentuale di saturazione del tatami, può superare 1, ma il rischio diventa molto alto.

Osservazioni:

- Conservazione: ogni transizione tra popolazioni è conservativa, non ci sono perdite o aggiunte di atleti se non per $\mu$ e $\nu$.
- Un sano che si infortuna entra in $I$ con probabilità $\pi$ e in $M$ con probabilità $1-\pi$.
- Un malconcio che si infortuna di nuovo entra in $I$ con probabilità $\pi$ e resta in $M$ con probabilità $1-\pi$.