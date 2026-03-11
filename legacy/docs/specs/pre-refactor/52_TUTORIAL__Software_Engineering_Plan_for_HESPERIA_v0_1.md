# Historical reference (pre-refactor)

# 52_TUTORIAL__Software_Engineering_Plan_for_HESPERIA_v0_1

## Scopul documentului
Acest document livrează un **plan complet de Software Engineering** aplicat pe proiectul existent **HESPERIA**, în format academic, fără programare, folosind artefactele deja prezente în repository.

Planul urmează structura clasică din tutorialele universitare de inginerie software (overview → SDLC → management → requirements → design → implementation → testing → maintenance → CASE), dar este **instanțiat concret** pe HESPERIA.

---

## 0) Fundamentul proiectului HESPERIA

### 0.1 Ce stă la bază
HESPERIA este construit pe un nucleu triplu:
1. **Formalism semantic-geometric** (arie/familie/hex/side + coordonate și indici canonici).
2. **Engine semantic determinist** (atribuire lexicală/sentențială și agregări controlabile).
3. **Guvernanță operațională** (policy, guard layers ΣΓΘ, gates de publicare).

Acest fundament este specificat în lanțul de documente numerotate (master spec, blueprint, semantic engine, indexing), completat de politici operaționale și artefacte de proiect.

### 0.2 Necesitatea
Necesitatea proiectului apare în contexte cu volum mare de afirmații/text, unde este nevoie de:
- clasificare semantică stabilă,
- trasabilitate a deciziilor,
- controlul conflictelor și al derivației semantice,
- guvernanță explicită pentru publishability.

### 0.3 Valorile proiectului
Valorile centrale pe care le operationalizează repository-ul:
- **determinism** (același input are traseu explicabil),
- **auditabilitate** (artefacte versionate, baseline-uri),
- **siguranță logică** (invariante ΣΓΘ),
- **evoluție controlată** (fixed-point + change control),
- **interoperabilitate academică** (specificații explicite + glosar de termeni).

### 0.4 Aplicații posibile
- **Scară îngustă (narrow scope):**
  - asistent intern de analiză pentru seturi mici/medii de afirmații,
  - suport pentru echipe de policy/compliance,
  - instrument de verificare semantică în proiecte de cercetare.
- **Scară largă (large scope):**
  - strat semantic pentru platforme multi-agent,
  - guvernanță de conținut în ecosisteme enterprise,
  - infrastructură de reasoning asistat pentru fluxuri cu risc reputațional/etic.

---

## 1) Software Overview (teorie + instanțiere HESPERIA)

### 1.1 Definiții de bază
- **Software**: programe + date + configurații + documentație + procese operaționale.
- **Inginerie software**: aplicare disciplinată, măsurabilă și repetabilă pentru dezvoltare, operare și mentenanță.
- **În HESPERIA**: software-ul include atât codul (`sphere_rag/`, `scripts/`), cât și corpusul formal de specificații/politici/proiect.

### 1.2 Evoluția software
Teoretic, orice produs software util evoluează în timp (cerințe, context, risc).
Practic, HESPERIA arată această evoluție prin secvența: concept → v0.x prototipuri → formalizare v1/fixed-point → extensii operaționale.

### 1.3 Legile evoluției (Lehman, interpretare aplicată)
- Complexitatea tinde să crească fără control explicit.
- Calitatea scade fără mentenanță sistematică.
- Evoluția trebuie guvernată, nu doar codată.

În HESPERIA, răspunsul este: baseline-uri, politici de guard, issue closure, release discipline.

### 1.4 E-type software
HESPERIA are caracteristici E-type: modelarea unei realități semantice în schimbare, cu feedback continuu și necesar de recalibrare.

### 1.5 Paradigme software
- proces: iterativ-incremental;
- design: modular, spec-driven;
- implementare: predominant procedural/funcțional în Python.

### 1.6 De ce este necesară ingineria software aici
Fără disciplină de inginerie, un sistem semantic complex devine opac și instabil. HESPERIA folosește această disciplină pentru a păstra coerența între specificații, cod și guvernanță.

### 1.7 Caracteristici de software bun (mapare)
- corectitudine, fiabilitate, securitate,
- modificabilitate și testabilitate,
- trasabilitate și auditabilitate,
- consistență semantică inter-versiuni.

---

## 2) SDLC aplicat

### 2.1 Activități SDLC
1. **Communication**: documente governance/project.
2. **Requirements**: master spec + blueprint + spec-uri specializate.
3. **Feasibility**: evaluări de context, risc, securitate, schedule.
4. **Analysis**: state assessments, scope sync.
5. **Design**: semantic engine + indexing + traversal + guard model.
6. **Implementation**: module Python și scripturi operaționale.
7. **Testing**: self-tests, stress-tests, checks de gardă.
8. **Deployment/Operations**: release fixed-point + handoff.
9. **Maintenance**: issue closure + iterații controlate.

### 2.2 Modelul de dezvoltare predominant
Modelul real este **hibrid**:
- waterfall pentru formalizarea de spec;
- iterativ pentru evoluția repository-ului;
- elemente V-model prin maparea spec ↔ verificare.

---

## 3) Software Project Management

### 3.1 Proiectul
HESPERIA este tratat explicit ca proiect software, nu doar colecție de scripturi.

### 3.2 De ce management de proiect
Coordonarea între semnificație, logică, risc, securitate și release necesită management formal.

### 3.3 Roluri și responsabilități
Rolurile sunt explicitate în charter, task-uri de guvernanță și documente de handoff.

### 3.4 Activități de management observabile în repo
- project charter,
- scope and sync,
- schedule baseline,
- risk register,
- security baseline,
- artifact index,
- release fixed-point,
- handoff checklist,
- issue closure.

### 3.5 Baseline și change control
Practica de baseline + fixed-point stabilizează evoluția și reduce regresiile conceptuale.

---

## 4) Software Requirements Engineering

### 4.1 Ce sunt cerințele
Cerințele descriu ce trebuie să facă sistemul și în ce limite de calitate/riscuri.

### 4.2 Clasificare
- **Funcționale**: atribuire semantică, construcție de regiune, traversare, metrici, decizie.
- **Non-funcționale**: determinism, explainability, auditability, siguranță operațională.

### 4.3 Elicitation (aplicat)
În HESPERIA, elicitation este realizat prin:
- specificații numerotate,
- documente de task/direcție,
- rapoarte de stare,
- convergență în blueprint și politici.

### 4.4 Calitatea cerințelor
Cerințele trebuie să fie clare, coerente, verificabile, versionabile și trasabile.

### 4.5 SRS practic HESPERIA
SRS-ul nu este un singur fișier, ci un **set orchestrat** de documente canonice + extensii operaționale.

---

## 5) Software Design Basics

### 5.1 Niveluri
- **High-level**: model semantic-geometric + guvernanță.
- **Low-level**: module Python + structuri + pipeline.

### 5.2 Modularizare
Separare pe domenii: specs / governance / project / scripts / engine.

### 5.3 Coupling & cohesion
- coeziune bună pe module tematice,
- cuplare redusă prin specificații canonice și interfețe logice clare.

### 5.4 Concurență
Concurența nu este încă focală; prioritatea actuală este determinismul secvențial.

### 5.5 Verificarea designului
Se face prin aliniere la spec, checks de guard și artefacte de release.

---

## 6) Instrumente de analiză și design

Aplicabile în contextul curent:
- DFD pentru pipeline semantic,
- decision tables pentru ΣΓΘ,
- structured pseudo-code pentru formule și reguli,
- data dictionary pentru entități (areas/families/sides/statements),
- structuri de trasabilitate între requirement și artefact.

---

## 7) Strategii și abordări de design

- **Structured design**: dominant în descompunerea pipeline-ului.
- **Function-oriented**: dominant în scripts și calcule.
- **Top-down**: de la master spec la implementare.
- **Bottom-up**: validări din prototip spre consolidare de policy.

HESPERIA folosește un **hibrid controlat** între aceste abordări.

---

## 8) User Interface (stadiul actual)

- Interfața principală este CLI + document-driven operation.
- UI rules relevante: consistență output, feedback explicit, minimizarea ambiguității.
- GUI poate fi etapă ulterioară, după stabilizarea semantic-governance core.

---

## 9) Software Complexity

### 9.1 Teorie minimă
- complexitate structurală (cod),
- complexitate semantică (model),
- complexitate organizațională (guvernanță).

### 9.2 În HESPERIA
Complexitatea critică este semantică + guvernanță, nu doar algoritmică.

Metrici clasice (cyclomatic/Halstead/FP) pot completa evaluarea când nucleul devine produs extins.

---

## 10) Implementare (fără cod nou)

Implementarea existentă respectă principiul:
**specificație formală → mapare modulară → rulare controlată → output auditabil**.

Provocarea principală nu este „cum scriem cod”, ci „cum menținem sincronizarea între semantică, indexare, traversal și policy”.

---

## 11) Testing & Quality

### 11.1 Cadru teoretic
- Verification: „built right?”.
- Validation: „right thing?”.
- QA: sistemul de procese;
- QC: controlul livrabilelor;
- Testing: execuția verificărilor.

### 11.2 În HESPERIA
- self-test/stress-test pentru robustețe,
- verificări pe integrarea semantică,
- gates de guvernanță pentru decizie finală.

Niveluri acoperite: unit/integration/system + acceptance prin governance.

---

## 12) Maintenance & Evolution

### 12.1 Tipuri
- corectivă,
- adaptivă,
- perfectivă,
- preventivă.

### 12.2 Practică recomandată pentru HESPERIA
- schimbările mari să apară în fișiere versionate noi,
- menținerea disciplinei fixed-point,
- actualizare simultană spec + project docs + governance impact.

---

## 13) CASE Tools și ecosistemul de lucru

În formă actuală, ecosistemul CASE este compus din:
- git + discipline de release/baseline,
- corpus documentar versionat,
- scripturi de verificare,
- artefacte de management proiect,
- rapoarte de guvernanță.

---

## 14) Mapare directă la artefacte existente (exemple concrete)

### 14.1 Nucleu semantic și geometric
- `10_MASTER_SPEC__HESPERIA_v1_0.txt`
- `11_BLUEPRINT__HESPERIA_v4_5_full.txt`
- `12_SPEC__Semantic_Engine_v0_4.txt`
- `13_SPEC__Indexing_and_Coordinates_v1_0.txt`
- `20_GEOMETRY__formalized_structure_java.txt`
- `21_MATH__HESPERIA_formalization_v1_java.txt`
- `30_FAMILIES__HESPERIA_hex_canonical_v1_0.txt`
- `31_FAMILIES__area_family_table_full.txt`

### 14.2 Guard și policy
- `40_POLICY__Loopability_and_traversal.txt`
- `41_POLICY__Operational_additions_v0_1.txt`
- `42_POLICY__Guard_Layer_Sigma_Gamma_Theta_v1_0.txt`

### 14.3 Implementare existentă
- `sphere_rag/geometry.py`
- `sphere_rag/semantic_engine.py`
- `sphere_rag/phase_engine.py`
- `sphere_rag/metrics.py`
- `sphere_rag/guards.py`
- `scripts/phase_traversal_selftest.py`
- `scripts/hesperia_safeguard_stress_test.py`

### 14.4 Management proiect și operaționalizare
- `project/PROJECT-CHARTER.md`
- `project/SCOPE-AND-SYNC.md`
- `project/SCHEDULE-BASELINE.md`
- `project/RISK-REGISTER.md`
- `project/SECURITY-BASELINE.md`
- `project/ARTIFACT-INDEX.md`
- `project/RELEASE-V1-FIXED-POINT-2026-02-18.md`
- `project/HANDOFF-CHECKLIST.md`

### 14.5 Cadru academic și glosar de concepte
- `ACADEMIC.md`

---

## 15) Concluzie

HESPERIA are deja baza necesară pentru un parcurs complet de software engineering: specificații canonice, implementare minimă funcțională, guvernanță structurată și management de proiect formalizat.

Acest plan transformă repository-ul într-un **studiu de caz aplicat** pentru disciplina de inginerie software, cu utilitate atât academică, cât și practică, la scară îngustă și largă.
