---
cssclasses: [home]
---
# 🎓 Management Engineering — Home

> [!quote] LM-31 · Università di Padova · Vicenza · a.a. 2026/27
> Punto di partenza del vault: corsi, progetti, materiale d'esame. Info sul repo → [[README]]

---

## 📍 Oggi
```dataviewjs
// Orario settimanale (1 = lunedì … 5 = venerdì)
const C = {
  SOSCM: {e:"🟧", n:"Smart Operations & SCM", note:"00 - SOSCM index-claude", prof:"Macchion, Vinelli"},
  DWT:   {e:"🟦", n:"Digital Warehousing & Transportation", note:"Lessons - DWT", prof:"Persona"},
  MFSLN: {e:"🟢", n:"Material Flow Systems & Logistic Networks", note:"Lessons - MFSSCM", prof:"Battini, Katiraee"},
  DMIM:  {e:"🟩", n:"Digital Marketing & International Mgmt", note:"Lessons - International Management", prof:"—"},
};
const W = {
  1: [["08:30","10:30","DMIM","VM6"],["10:30","12:30","SOSCM","Sala 8"],["12:30","14:30","DWT","Sala 8"]],
  2: [["10:30","12:30","DWT","Sala 8"],["12:30","14:30","SOSCM","Sala 8"]],
  3: [["10:30","12:30","MFSLN","VM8"],["14:30","16:30","SOSCM","Sala 8"]],
  4: [["10:30","12:30","MFSLN","VM8"],["14:30","16:30","MFSLN","VM8"],["16:30","18:30","DMIM","VM8"]],
  5: [],
};
const giorni = ["domenica","lunedì","martedì","mercoledì","giovedì","venerdì","sabato"];
const now = moment();
const d = now.day();
const t = now.format("HH:mm");
const today = W[d] ?? [];

dv.paragraph(`**${giorni[d].charAt(0).toUpperCase()+giorni[d].slice(1)} ${now.format("D MMMM YYYY")}** · ore ${t}`);

if (today.length) {
  dv.table(["", "Orario", "Corso", "Aula", "Stato"],
    today.map(([a,b,k,aula]) => {
      const st = t >= b ? "✔️ finita" : (t >= a ? "🔴 **in corso**" : "⏳ da fare");
      return [C[k].e, `${a}–${b}`, dv.fileLink(C[k].note, false, `${k} — ${C[k].n}`), aula, st];
    }));
  const next = today.find(([a]) => t < a);
  if (next) dv.paragraph(`➡️ Prossima: **${next[2]}** alle ${next[0]} in ${next[3]}`);
  else if (today.every(([,b]) => t >= b)) dv.paragraph("🏁 Lezioni finite per oggi.");
} else {
  // Trova il prossimo giorno con lezioni
  let k = 1;
  while (!(W[(d + k) % 7] ?? []).length) k++;
  const nd = (d + k) % 7, first = W[nd][0];
  dv.paragraph(`🎉 Nessuna lezione oggi. Prossima: **${giorni[nd]}** alle ${first[0]} — ${C[first[2]].e} **${first[2]}** (${first[3]})`);
}
```

## 🗓️ Settimana tipo

| Ora | Lunedì | Martedì | Mercoledì | Giovedì | Venerdì |
|---|---|---|---|---|---|
| **08:30–10:30** | 🟩 [[Lessons - International Management\|DMIM]]<br><small>VM6</small> | | | | |
| **10:30–12:30** | 🟧 [[00 - SOSCM index-claude\|SOSCM]]<br><small>Sala 8</small> | 🟦 [[Lessons - DWT\|DWT]]<br><small>Sala 8</small> | 🟢 [[Lessons - MFSSCM\|MFSLN]]<br><small>VM8</small> | 🟢 [[Lessons - MFSSCM\|MFSLN]]<br><small>VM8</small> | |
| **12:30–14:30** | 🟦 [[Lessons - DWT\|DWT]]<br><small>Sala 8</small> | 🟧 [[00 - SOSCM index-claude\|SOSCM]]<br><small>Sala 8</small> | | | |
| **14:30–16:30** | | | 🟧 [[00 - SOSCM index-claude\|SOSCM]]<br><small>Sala 8</small> | 🟢 [[Lessons - MFSSCM\|MFSLN]]<br><small>VM8</small> | |
| **16:30–18:30** | | | | 🟩 [[Lessons - International Management\|DMIM]]<br><small>VM8</small> | |

> [!info]- Docenti e sedi
> Tutte le aule sono in **Nuovo Viale Margherita, Vicenza**.
> - 🟧 **SOSCM** — Smart Operations & Supply Chain Mgmt · Macchion L., Vinelli A. · Sala 8 · 6 h/sett.
> - 🟦 **DWT** — Digital Warehousing & Transportation · Persona A. · Sala 8 · 4 h/sett.
> - 🟢 **MFSLN** — Material Flow Systems & Logistic Networks · Battini D., Katiraee N. · VM8 · 6 h/sett.
> - 🟩 **DMIM** — Digital Marketing & International Mgmt · VM6 (lun) / VM8 (gio) · 4 h/sett.
> - Venerdì libero 🎉

---

## 📚 Corsi in corso

| Corso | Lezioni | Riassunti | Moodle |
|---|---|---|---|
| **Smart Operations & Supply Chain Mgmt** (SOSCM) | — | [[00 - SOSCM index-claude\|Indice capitoli]] · [[Summary SOSCM - Vinelli\|Vinelli]] · [[Summary SOSCM - Macchion\|Macchion]] · [[Book Summary]] | — |
| **Digital Warehousing & Transportation** (DWT) | [[Lessons - DWT]] | — | [link](https://stem.elearning.unipd.it/course/view.php?id=16780) |
| **Material Flow Systems & SCM** (MFSSCM) | [[Lessons - MFSSCM]] | [[DEFINING REQUIREMENTS]] | [link](https://stem.elearning.unipd.it/course/view.php?id=17225) |
| **Digital Marketing & International Mgmt** (IM) | [[Lessons - International Management]] | [[Summary IM]] · [[Summary IM - Complete-claude\|Summary completo]] | [link](https://stem.elearning.unipd.it/course/view.php?id=16800) |

---

## 🛠️ Progetti

- **APW 2026 — Magazzino six-way shuttle** (DWT)
  - [[Project overview]]
  - [[APW 2026 – Assignment Guide and Sizing of the Six-Way Shuttle Warehouse|Assignment guide & sizing]]
  - [[modeling_analysis_and_design_of_shuttle_based_storage_systems|Paper: SBS systems]]
- **Assembly Line Balancing — CPLEX** (MFSSCM) → [[MaterialFlowSystemsAndSupplyChainManagement/cplex/Assembly Line Balancing Optimal Solution - TEAM 21.pdf|Soluzione Team 21]]

---

## 📝 Appunti d'esame del gruppo

> [!example]- Apri l'elenco
> - [[NotesFromGroup/SOSCM exam notes.pdf|SOSCM]] · [[NotesFromGroup/DWT exam notes.pdf|DWT]] · [[NotesFromGroup/IM exam notes.pdf|IM]] · [[NotesFromGroup/MFSLN exam notes.pdf|MFSLN]]
> - [[NotesFromGroup/BADM exam notes.pdf|BADM]] · [[NotesFromGroup/DC exam notes.pdf|DC]] · [[NotesFromGroup/DM exam notes.pdf|DM]] · [[NotesFromGroup/DO exam notes.pdf|DO]]
> - [[NotesFromGroup/MLCDM exam note.pdf|MLCDM]] · [[NotesFromGroup/NPPM exam notes.pdf|NPPM]] · [[NotesFromGroup/SDT exam notes.pdf|SDT]] · [[NotesFromGroup/SOM exam notes.pdf|SOM]]

## 📖 Libri di testo

- SOSCM → [[Smart operation and supply chain management.pdf]]
- IM → [[International Business Competing in the Global Marketplace, 14e ISE (Charles W. L. Hill) (z-library.sk, 1lib.sk, z-lib.sk).pdf|Hill — International Business 14e]]
- MFSSCM → [[Facilities Planning John A. White Yavuz A. Bozer J. M. A. Tanchoco (James A. Tompkins) (z-library.sk, 1lib.sk, z-lib.sk).pdf|Tompkins — Facilities Planning]] · [[Material flow system and logistic networks.pdf]]

## 🧱 Prerequisiti (triennale)

- **Impianti meccanici** → [[Formulario impianti meccanici.pdf|Formulario]] · [[Impianti Calzavara.pdf|Dispensa]] · [[Eserciziario Impianti.pdf|Eserciziario]]
- **OPSL** → [[Quaderno OPSL.pdf|Quaderno]] · [[Eserciziario OPSL.pdf|Eserciziario]] · [[Quiz_OPSL.pdf|Quiz]]

---

## ✅ Da fare
```tasks
not done
sort by due
limit 15
```

## 🕒 Modificate di recente
```dataview
TABLE WITHOUT ID file.link AS "Nota", file.folder AS "Cartella", file.mtime AS "Modifica"
FROM ""
WHERE file.name != this.file.name AND !contains(file.path, "Excalidraw") AND !contains(file.path, ".pdf-annotator")
SORT file.mtime DESC
LIMIT 10
```

## ✏️ Disegni recenti
```dataview
LIST FROM "Excalidraw" SORT file.ctime DESC LIMIT 5
```
