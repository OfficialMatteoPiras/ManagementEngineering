# Management Engineering
Management Engineering @ Unipd — Bachelor's (L-9) and Master's (LM-31) in Vicenza: combining engineering, economics and management to design and run complex production, logistics and service systems. 

---

# 📚 Appunti — Management Engineering (Ingegneria Gestionale) · Università di Padova

> Appunti, dispense ed esercizi di **Ingegneria Gestionale** dell'Università degli Studi di Padova.
> Le note sono in formato Markdown e pensate per essere lette con [Obsidian](https://obsidian.md).
> **Non serve sapere programmare**: questa guida ti spiega tutto, passaggio per passaggio.

---

## 🎓 Il corso in breve

**Ingegneria Gestionale** (in inglese *Management Engineering*) è il corso di studio che unisce l'ingegneria all'economia e all'organizzazione aziendale: chi si laurea sa "parlare" sia con i tecnici sia con i manager, e sa analizzare, progettare e gestire sistemi produttivi, logistici e di servizi complessi.

All'Università di Padova il percorso esiste in due livelli, entrambi con sede a **Vicenza**:

| | Laurea Triennale | Laurea Magistrale |
|---|---|---|
| **Codice / Classe** | L-9 — Ingegneria Industriale | LM-31 — Ingegneria Gestionale |
| **Durata** | 3 anni | 2 anni |
| **Lingua** | Italiano | Italiano **o** Inglese |
| **Accesso** | Libero, con prova d'ingresso | Libero, con requisiti curriculari |

- **Triennale (L-9)**: fornisce le basi di matematica, fisica, informatica e statistica, unite all'ingegneria industriale e alle discipline economico-aziendali. Prepara a ruoli operativi e manageriali in produzione e logistica, processi operativi e amministrativi, acquisti, marketing e valutazione economica dei progetti.
- **Magistrale (LM-31)**: aggiunge un approccio multidisciplinare su tre pilastri — tecnico-ingegneristico, economico-gestionale e metodologico-quantitativo — e offre **due curricula**: uno in italiano (focalizzato sui processi di business, anche in ottica sostenibile) e uno in inglese chiamato proprio **Management Engineering** (focalizzato sulla trasformazione digitale). Il percorso si conclude con un tirocinio e una tesi.
- **Sbocchi**: produzione, logistica, acquisti e approvvigionamenti, commerciale e marketing, R&S, controllo di gestione, consulenza, banche e assicurazioni — secondo i dati Almalaurea il tasso di occupazione dei laureati LM-31 a Padova è tra i più alti (~98,6%).

Fonti: [Scheda triennale Unipd](https://www.ingegneria.unipd.it/offerta-didattica/corsi-di-laurea?tipo=L&ordinamento=2025&key=IN2919) · [Scheda magistrale Unipd](https://www.ingegneria.unipd.it/offerta-didattica/corsi-di-laurea-magistrale?tipo=LM&ordinamento=2025&key=IN3084)

---

## 📁 Cosa contiene questa repository

```
📁 appunti-management-engineering-unipd/
├── 00 - Indice.md          ← partite sempre da qui: è la "mappa" di tutti gli appunti
├── 01 - ....md             ← una nota per capitolo/argomento
├── 02 - ....md
├── ...
├── allegati/               ← immagini e figure citate nelle note
└── README.md               ← questo file
```

- I file con estensione **`.md`** sono semplici documenti di testo (Markdown): si leggono benissimo anche qui su GitHub, ma con Obsidian diventano interattivi — formule matematiche, evidenziazioni e collegamenti cliccabili tra gli argomenti (`[[così]]`).
- La nota **`00 - Indice`** contiene i link a tutti i capitoli: è il punto di partenza consigliato.

## 🔍 Due modi per leggere gli appunti

| Metodo | Per chi | Serve internet? | Si aggiorna facilmente? |
|---|---|---|---|
| **A — Download ZIP** (consigliato) | Chiunque, zero installazioni "strane" | Solo per scaricare | Riscaricando lo ZIP |
| **B — Clonare con Git** | Chi ha (o vuole imparare) Git | Solo per scaricare | Sì, con un comando |

In entrambi i casi vi servirà **Obsidian** per leggere gli appunti con formula, immagini e link. Ecco come installarlo.

---

## 🛠️ Installare Obsidian (una volta sola)

Obsidian è **gratuito** (per uso personale e anche commerciale) e non richiede la creazione di un account: basta installarlo e aprirlo.

### Su Windows

1. Aprite il browser e andate su **[obsidian.md/download](https://obsidian.md/download)**.
2. Nella sezione **Windows** cliccate il pulsante di download: partirà il download di un file `.exe` (di solito finisce nella cartella *Download*).
3. Fate **doppio clic** sul file scaricato (`Obsidian-x.x.x.exe`).
4. Cliccate **Install** e aspettate qualche secondo: Obsidian si aprirà da solo al termine.
5. La prima volta scegliete la lingua (c'è anche **italiano**) e chiudete pure la finestra di benvenuto: al prossimo passaggio apriremo gli appunti.

> Non comparirà nessuna richiesta di account o password: se vedete un pulsante "Sign in" potete ignorarlo tranquillamente.

### Su macOS

1. Andate su **[obsidian.md/download](https://obsidian.md/download)**.
2. Nella sezione **macOS** cliccate il pulsante **Universal** per scaricare il file `.dmg`.
3. Fate **doppio clic** sul file `.dmg` scaricato: si aprirà una finestrella con l'icona di Obsidian e la cartella `Applications`.
4. **Trascinate** l'icona di Obsidian dentro `Applications`.
5. Chiudete la finestrella e aprite Obsidian dal **Launchpad** (o dalla cartella Applicazioni). Se macOS chiede "vuoi aprire un'app scaricata da internet?", cliccate **Apri**.

### Su Linux (facoltativo)

- **Facile**: da terminale, `flatpak install flathub md.obsidian.Obsidian` e poi avviatelo dal menu applicazioni.
- In alternativa scaricate l'**AppImage** dalla stessa pagina, poi: `chmod u+x Obsidian-*.AppImage` e `./Obsidian-*.AppImage`.

---

## 🅰️ Metodo A — Aprire gli appunti senza Git (consigliato ai principianti)

Con questo metodo "copiate" gli appunti sul vostro computer semplicemente scaricandoli come archivio ZIP. Non serve alcun programma aggiuntivo.

1. Nella pagina GitHub di questa repo, cliccate il pulsante verde **`<> Code`** (in alto a destra, sopra l'elenco dei file).
2. Nel menu che si apre, cliccate **Download ZIP**.
3. Il browser scaricherà un file tipo `appunti-management-engineering-unipd-main.zip` (di solito nella cartella *Download*).
4. **Estraete l'archivio**:
   - **Windows**: clic destro sul file ZIP → **Estrai tutto…** → cliccate **Estrai** (lasciate pure la destinazione proposta). Otterrete una cartella con lo stesso nome dello ZIP.
   - **macOS**: fate semplicemente doppio clic sul file ZIP: si estrae da solo in una cartella omonima.
5. Aprite **Obsidian** e cliccate su **Open folder as vault** (in italiano: *Apri cartella come vault*).
   - Se non vedete la finestra iniziale: menu `File` → `Open vault…` → scheda **Open folder as vault**.
6. Selezionate la cartella **appena estratta** (quella che contiene `00 - Indice.md`, non lo ZIP!) e confermate.
7. Se Obsidian chiede *"Do you trust the author of this vault?"* cliccate **Trust author and enable plugins** (in italiano: *Fidati dell'autore*): è una richiesta standard, serve solo ad attivare le impostazioni incluse nella cartella.
8. Aprite la nota **`00 - Indice`** e buona lettura ✨

> 💡 **Da ricordare**: gli appunti scaricati così sono una *fotografia*: non si aggiorneranno da soli. Quando escono note nuove, ripetete i passaggi 1–4 e sostituite la cartella (oppure passate al Metodo B).

## 🅱️ Metodo B — Clonare la repository con Git

"Clonare" significa scaricare una copia "intelligente" degli appunti, che potrete aggiornare con un solo comando ogni volta che escono note nuove.

### B.1 — Installare Git (una volta sola)

- **Windows**: scaricate il programma da **[git-scm.com/download/win](https://git-scm.com/download/win)**, aprite il file `.exe` scaricato e cliccate sempre **Avanti/Next** senza cambiare nulla: le opzioni predefinite vanno benissimo. Alla fine potete deselezionare "Launch Git Bash" se volete.
- **macOS**: Git è già incluso. Se il terminale vi chiede di installare "Command Line Developer Tools", confermate e aspettate.

### B.2 — Clonare la repo

1. In questa pagina GitHub cliccate il pulsante verde **`<> Code`** e copiate l'indirizzo HTTPS (somiglia a `https://github.com/TUO-USERNAME/appunti-management-engineering-unipd.git`).
2. Aprite un terminale:
   - **Windows**: premete il tasto ⊞ Start, scrivete **Git Bash** e aprite quell'app (si apre una finestra nera dove si scrive).
   - **macOS**: premete `Cmd + Spazio`, scrivete **Terminale** e premete Invio.
3. Scrivete (o incollate con `Ctrl+V` / `Cmd+V`) il comando seguente, sostituendo l'indirizzo con quello copiato al punto 1:

   ```bash
   git clone <https://github.com/TUO-USERNAME/appunti-management-engineering-unipd.git>
   ```

4. Premete **Invio**: verrà creata una cartella `appunti-management-engineering-unipd` nella posizione dove avete aperto il terminale.
   - Su Windows Git Bash si apre nella vostra cartella utente (`C:\Users\VostroNome`); se preferite un'altra posizione, prima scrivete ad esempio `cd Documents` e poi ripetete il clone.

### B.3 — Aprirla in Obsidian

1. Aprite **Obsidian** → **Open folder as vault** (*Apri cartella come vault*).
2. Selezionate la cartella `appunti-management-engineering-unipd` creata dal clone.
3. Se richiesto, cliccate **Trust author and enable plugins**.
4. Aprite **`00 - Indice`** e studiate! 📖

### B.4 — Aggiornare gli appunti

Quando escono note nuove, aprite Git Bash (o il Terminale) **dentro** la cartella della repo e scrivete:

```bash
git pull
```

Se siete dentro la cartella: `cd appunti-management-engineering-unipd` prima di `git pull`. Obsidian aggiornerà le note automaticamente.

---

## ❓ Problemi comuni

| Problema | Soluzione |
|---|---|
| "I file `.md` si aprono con Blocco note e non li capisco" | Non aprite i file singolarmente: installate Obsidian e aprite **l'intera cartella** come vault (punti 5–7 del Metodo A). |
| "Non vedo le immagini / le formule" | Avete estratto lo ZIP **completo**, inclusa la cartella `allegati/`? Se avete copiato solo alcuni file, le immagini restano orfane: ri-estraete tutta la cartella. |
| "Obsidian chiede di fidarsi dell'autore" | È normale: cliccate *Trust author and enable plugins*. |
| "Dove trovo un argomento?" | Premete `Ctrl+O` (o `Cmd+O` su Mac) per cercare una nota per nome, oppure `Ctrl+Shift+F` per cercare una parola dentro tutte le note. |
| "Come aggiorno gli appunti?" | Metodo A: riscaricate lo ZIP. Metodo B: `git pull`. |
| "Posso usarle sul telefono?" | Sì: Obsidian esiste gratis anche per iOS/Android (App Store / Play Store), ma per avere gli stessi file sul telefono serve un sistema di sincronizzazione (es. cartella su iCloud/Drive) — argomento non trattato qui. |
| "Ho modificato le note, posso condividerle?" | Certo: aprite una *Issue* su GitHub o contattate l'autore. Le modifiche fatte in locale restano però sul vostro computer finché non le caricate voi. |

---

## 📜 Licenza

<!-- Scegliete una licenza e sostituite questa riga, es. CC BY-NC-SA 4.0 -->
Questi appunti sono forniti "as is" per uso di studio personale. Prima di redistribuirli, chiedete all'autore o aggiungete una licenza esplicita (per appunti universititi è comune [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.it)).

*Appunti realizzati da uno studente del corso: possono contenere errori — segnalali pure, si accetta ogni contributo!*
