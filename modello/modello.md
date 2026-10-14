
# Modello

Modellizzazione, a tempo discreto, di un periodo di allenamento di un gruppo di atleti di judo.

## Ipotesi iniziali

- Il tempo e $t \in \{0, 1, \dots, T\}$, dove $T$ è il tempo massimo (orizzonte del modello). Si suppone che le sedute di allenamento siano distribuite circa omogeneamente nel tempo, così che un passo $t \to t+1$ corrisponda a una seduta e il recupero tra due passi consecutivi sia confrontabile.
- La popolazione di atleti è omogenea: a parte la suddivisione descritta sotto, gli atleti hanno lo stesso livello e la stessa esposizione al carico.
- Si parla prevalentemente di atleti non alle prime armi, quindi con possibili infortuni pregressi ($P$).
- Il carico di allenamento non è costante: può essere nullo (es. sessione di recupero), inferiore al massimo (es. lavoro tecnico) oppure superiore al massimo (overtraining).
- L'orizzonte $T$ è breve: non c'è abbastanza tempo affinché un atleta malconcio ($M$) torni in $S$ o in $P$. L'unico percorso di recupero previsto è $I \to M$.
- Gli stati sono numeri reali non negativi, non conteggi interi. Il modello è quindi significativo per gruppi sufficientemente numerosi.


## Popolazioni e variabili di stato

- $S$: sani
- $P$: atleti con infortuni pregressi (si allenano)
- $I$: infortunati (non si possono allenare)
- $M$: malconci (si possono allenare, ma sono più a rischio)
- $\bar{F}_f$: fatica fisica media del gruppo che si allena ($S$, $P$, $M$)
- $\bar{F}_p$: fatica psicologica media del gruppo che si allena ($S$, $P$, $M$)

Condizioni iniziali: $S(0), P(0) \geq 0$ e $I(0), M(0), \bar{F}_f(0), \bar{F}_p(0) = 0$.

## Modello

Modello esteso
$$
    \left\lbrace\begin{aligned}
        S(t+1) &= S(t) \\
            &+ \alpha \mu\left(\frac{t}{T}\right) \\
            &- \nu\left(\frac{t}{T}, \beta_S\right) S(t) \\
            &- (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_S\right) S(t) \\[5pt]

        P(t+1) &= P(t) \\
            &+ (1 - \alpha) \mu\left(\frac{t}{T}\right) \\
            &- \nu\left(\frac{t}{T}, \beta_P\right) P(t) \\
            &- (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_P\right) P(t) \\[5pt]

        I(t+1) &= I(t) \\
            &+ \pi (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_S\right) S(t) \\
            &+ \pi (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_P\right) P(t) \\
            &+ \pi (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_M\right) M(t) \\
            &- \rho I(t) \\
            &- \nu\left(\frac{t}{T}, \beta_I\right) I(t) \\[5pt]

        M(t+1) &= M(t) \\
            &+ (1 - \pi) (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_S\right) S(t) \\
            &+ (1 - \pi) (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_P\right) P(t) \\
            &- \pi (1 - u(t)) \lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_M\right) M(t) \\
            &+ \rho I(t) \\
            &- \nu\left(\frac{t}{T}, \beta_M\right) M(t) \\[5pt]

        \bar{F}_f(t+1) &= \bar{F}_f(t) \\
            &+ c_f(t) \\
            &- r(t) \bar{F}_f(t) \\[5pt]

        \bar{F}_p(t+1) &= \bar{F}_p(t) \\
            &+ c_p(t) \\
            &- r(t) \bar{F}_p(t)
    \end{aligned}\right.
$$

$t$: unità di tempo

$T$: tempo massimo

Significato dei termini:

- $\mu$, $\alpha$: ogni seduta entrano in media $\mu(t/T)$ nuovi atleti; una frazione $\alpha$ è sana ($S$), la restante $1-\alpha$ ha infortuni pregressi ($P$). Nessuno entra direttamente in $I$ o $M$.
- $\nu$: uscite dal gruppo (abbandoni, trasferimenti) dalla popolazione a cui si riferisce $\beta_\cdot$.
- $(1-u)\lambda$: probabilità effettiva di infortunio di un singolo atleta, ridotta dalla prevenzione dell'allenatore. Il terzo argomento di $\lambda$, $\frac{S+P+M}{A_{\max}}$, è la densità sul tatami: gli infortunati $I$ non si allenano e quindi non contano.
- $\pi$: un nuovo infortunio è grave (porta in $I$) con probabilità $\pi$, lieve (porta in $M$) con probabilità $1-\pi$.
- $\rho I$: gli infortunati guariscono parzialmente e passano in $M$.
- $\bar{F}_\cdot$: ogni seduta aggiunge il carico $c_\cdot(t)$ e il gruppo ne recupera una parte $r$.

## Parametri e funzioni

- $\mu\left(\frac{t}{T}\right)$: numero di nuovi atleti che entrano nel gruppo alla frazione di tempo $\frac{t}{T}$ (funzione di crescita)
- $\nu\left(\frac{t}{T}, \beta_\cdot\right)$: frazione di atleti che esce dal gruppo alla frazione di tempo $\frac{t}{T}$, pesata da $\beta_\cdot$ (funzione di decrescita)
- $\alpha$: frazione dei nuovi ingressi che è sana (i restanti hanno infortuni pregressi)
- $\beta_\cdot$: moltiplicatore della decrescita sulla popolazione a cui è riferito
- $\gamma_\cdot$: moltiplicatore di rischio nella funzione di infortunio sulla popolazione a cui è riferito
- $\lambda\left(\bar{F}_f(t), \bar{F}_p(t), \frac{S(t) + P(t) + M(t)}{A_{\max}}, \gamma_\cdot\right)$: probabilità che un atleta si infortuni nella seduta $t$, in funzione delle fatiche medie, della densità sul tatami e del moltiplicatore di rischio $\gamma_\cdot$
- $\pi$: probabilità che un infortunio sia grave ($I$) invece che lieve ($M$)
- $u(t)$: termine di controllo, efficacia della prevenzione degli infortuni da parte dell'allenatore ($u=0$: nessuna prevenzione, $u=1$: prevenzione perfetta)
- $\rho$: tasso di transizione da $I$ a $M$
- $c_\cdot(t)$: carico della seduta al tempo $t$ (0: riposo, 1: carico massimo, $>1$: overtraining)
- $r(t)$: recupero medio al tempo $t$
- $A_{\max}$: numero massimo di atleti sul tatami affinché l'allenamento sia sicuro e il rischio di collisione sia basso

## Ipotesi sui domini

- $\mu: [0, 1] \longrightarrow [0, +\infty)$
- $\nu: {[0, 1]}^2 \longrightarrow [0, 1]$
- $\alpha \in [0, 1]$
- $\beta_S, \beta_P, \beta_I, \beta_M \in [0, 1]$
- $\gamma_S, \gamma_P, \gamma_M \in [0, 1]$
- $\lambda: [0, +\infty)^3 \times [0, 1] \longrightarrow [0, 1]$
- $\pi \in [0, 1]$
- $u: \{0, \dots, T\} \longrightarrow [u_{\min}, 1]$ con $0 \leq u_{\min} < 1$
- $\rho \in [0, 1]$
- $c_f, c_p: \{0, \dots, T\} \longrightarrow [0, +\infty)$
- $r: \{0, \dots, T\} \longrightarrow [0, 1]$
- $A_{\max} \in [1, +\infty)$


## Vincoli

Per ogni $t$, le uscite da ciascuna popolazione non possono superare il contenuto del compartimento:

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

Poiché $\lambda$ dipende dallo stato, questi vincoli sono condizioni sulla traiettoria. Una condizione sufficiente che non dipende dallo stato è, ad esempio per $S$,
$$
    \sup \nu(\cdot, \beta_S) + (1 - u_{\min}) \sup \lambda(\cdot, \gamma_S) \leq 1,
$$
e analogamente per $P$ e $M$.


## Ipotesi per la funzione di accumulo della fatica

- Mescolamento: durante l'allenamento gli accoppiamenti cambiano frequentemente e in modo casuale, quindi ogni atleta interagisce in media con partner rappresentativi della fatica media del gruppo. Questo giustifica l'uso di $\bar{F}_f(t)$ e $\bar{F}_p(t)$ al posto delle fatiche individuali.
- Simmetria: l'infortunio può capitare sia a chi è stanco sia al partner fresco, quindi la fatica rilevante è quella dell'incontro, non del singolo.
- Gruppi non piccoli: il gruppo deve essere sufficientemente numeroso e omogeneo da rendere la media stabile e rappresentativa.
- La fatica media è calcolata sul gruppo che si allena ($S$, $P$, $M$) e si assume che la sua evoluzione non dipenda dalle variazioni di composizione del gruppo.


## Altre ipotesi

- Monotonia di $\lambda$: la funzione di infortunio $\lambda$ è crescente rispetto a $\bar{F}_f(t)$, $\bar{F}_p(t)$, alla densità $\frac{S(t) + P(t) + M(t)}{A_{\max}}$ e a $\gamma_\cdot$.
- La densità di atleti $\frac{S(t) + P(t) + M(t)}{A_{\max}}$ è la percentuale di saturazione del tatami: può superare 1, ma il rischio diventa molto alto.
- Ipotesi di lavoro (da confermare): chi ha un infortunio pregresso o in corso è più a rischio, cioè $\gamma_S \leq \gamma_P \leq \gamma_M$.


## Osservazioni

- Conservazione: ogni transizione tra popolazioni è conservativa. Detta $N(t) = S(t) + P(t) + I(t) + M(t)$ la popolazione totale,
    $$
        \begin{aligned}
            N(t+1) &= N(t) \\
                &+ \mu\left(\frac{t}{T}\right) \\
                &- \nu\left(\frac{t}{T}, \beta_S\right) S(t) \\
                &- \nu\left(\frac{t}{T}, \beta_P\right) P(t) \\
                &- \nu\left(\frac{t}{T}, \beta_I\right) I(t) \\
                &- \nu\left(\frac{t}{T}, \beta_M\right) M(t)
        \end{aligned}
    $$
    cioè non ci sono perdite o aggiunte di atleti se non per $\mu$ e $\nu$.
- Un sano (o un atleta in $P$) che si infortuna entra in $I$ con probabilità $\pi$ e in $M$ con probabilità $1-\pi$.
- Un malconcio che si infortuna di nuovo entra in $I$ con probabilità $\pi$ e resta in $M$ con probabilità $1-\pi$.


# Funzioni

## Crescita

$$
    \mu(x) = \omega_\mu \exp\left(-\frac{1}{2}\left(\frac{x}{\sigma_\mu}\right)^{2}\right)
$$

Dove:

- $\omega_\mu \in [0, +\infty)$
- $\sigma_\mu \in (0, +\infty)$

## Decrescita

$$
    \nu(x, \beta) = \beta \exp\left(-\frac{1}{2}\left(\frac{x - 1}{\sigma_\nu}\right)^{2}\right)
$$

Dove:

- $\beta \in [0, 1]$
- $\sigma_\nu \in (0, +\infty)$

## Infortunio

$$
    \lambda\left(f_f, f_p, d, \gamma\right) = \gamma \frac{1}{1 + \exp\left(-\omega_f f_f - \omega_p f_p - \omega_d d + b\right)}
$$

Dove:

- $\gamma \in [0,1]$
- $b \in [0, +\infty)$ fattore di soglia, senza di esso anche un atleta fresco con densità del tatami tendente a zero ha un tasso di infortunio alto.
- $\omega_f, \omega_p, \omega_d \in [0, +\infty)$

Proprietà:

- $\lambda \in [0, \gamma]$
- Crescente rispetto a $f_f$, $f_p$ e $d$
- Lineare rispetto a $\gamma$
- Appartenente a $\mathcal{C}^{\infty}$

## Recupero

$$
    r\left(t\right) = \omega_r \frac{1}{1 + \exp\left(\sigma_r t\right)}
$$

Dove:

- $\omega_r \in [0, 2]$
- $\sigma_r \in [0, +\infty)$

# Problema di controllo

L'obiettivo è minimizzare gli atleti infortunati o malconci (in particolare gli infortunati) mantenendo il carico di allenamento più alto possibile. Poiché sono due obiettivi in conflitto, conviene combinarli in un'unica funzione. I controlli sono $u$, $c_f$ e $c_p$:

$$
    \min_{u,\, c_f,\, c_p} \; J = \sum_{t=0}^{T} \big[ w_I\, I(t) + w_M\, M(t) \big] - w_c \sum_{t=0}^{T-1} \big( c_f(t) + c_p(t) \big) + w_u \sum_{t=0}^{T-1} u(t)
$$

Con pesi:
- $w_I \geq w_M \geq 0$ (un infortunio grave pesa di più)
- $w_c, w_u \geq 0$

E vincoli:
- $u \in [u_{\min}, 1]$
- $c_f, c_p \leq c_{\max} \in [0, +\infty)$