# Tutorial de Inginerie Software aplicat pe proiectul HESPERIA (v0.1)

Acest document descrie, punct cu punct, planul cerut și îl mapează pe artefactele, codul și guvernanța existente în repository-ul HESPERIA.

## 1. Software Overview

### 1.1 Definitions
- **Definiția software-ului**: ansamblu de programe, date, configurații, procese și documentație care rulează împreună pentru a oferi comportament util.
- **Inginerie software (IEEE)**: aplicarea sistematică, disciplinată și cuantificabilă a dezvoltării, operării și mentenanței software.
- **Inginerie software (Fritz Bauer)**: stabilirea și utilizarea principiilor solide de inginerie pentru a obține software economic, fiabil și eficient.
- **În HESPERIA**: software-ul nu este doar cod Python (`sphere_rag/`), ci și specificații numerotate, politici de guard, documente de proiect și fluxuri operaționale.

### 1.2 Software Evolution
- **Concept**: software-ul evoluează continuu pentru a rămâne util într-un context în schimbare.
- **Etape tipice**: inițializare concept → formalizare spec → implementare minimă → hardening/observability → guvernanță și extindere.
- **În HESPERIA**: traseul este explicit prin versiuni (`v0.1`, `v0.2`, fixed-point V1, extensii observability).

### 1.3 Software Evolution Laws
- **Legile lui Lehman** descriu cum sistemele reale cresc în complexitate și necesită adaptare permanentă.
- **Aplicat la HESPERIA**: există mecanisme de control al complexității (fixed point, guard layer ΣΓΘ, schimbări prin documente versionate) pentru a evita deriva haotică.

### 1.4 E-Type Software Evolution
- **Software E-type**: sisteme care modelează o lume reală și trebuie actualizate odată cu aceasta.
- **Caracteristici**: feedback continuu, creștere funcțională, risc de degradare fără guvernanță.
- **În HESPERIA**: componenta semantică și guvernanța îl apropie de E-type; de aceea sunt definite reguli stricte pentru evoluție și publishability (Θ guard).

### 1.5 Software Paradigms
- **Clasificare**: procedural, orientat obiect, funcțional, declarativ, data-driven.
- **Relație dezvoltare-design-programare**:
  - paradigma de dezvoltare (ex. iterativ) controlează procesul,
  - paradigma de design (ex. modular/OO) controlează arhitectura,
  - paradigma de programare controlează implementarea concretă.
- **În HESPERIA**: dezvoltare iterativă + design determinist pe specificații + implementare Python modulară.

### 1.6 Need of Software Engineering
- Necesitatea vine din: risc de complexitate, nevoia de trasabilitate, calitate, securitate, cost predictibil.
- **În HESPERIA**: nevoia este acoperită prin charter, context-packet gate-bound, schedule/risk/security baseline, politici ΣΓΘ.

### 1.7 Characteristics of Good Software
- **Operaționale**: corectitudine, fiabilitate, eficiență, securitate.
- **Tranzitorii**: portabilitate, reutilizare, interoperabilitate.
- **Mentenanță**: modificabilitate, testabilitate, lizibilitate, auditabilitate.
- **În HESPERIA**: accent pe determinism, invariants, documentație versionată, scripturi de self-test.

## 2. Software Development Life Cycle (SDLC)

### 2.1 SDLC Activities
- **Communication**: realizată prin documente governance/project.
- **Requirement Gathering**: prin master spec, blueprint și politici.
- **Feasibility Study**: evaluări de scope și limitări în context/schedule.
- **System Analysis**: analiză de stare și boundaries în documente “state-now”/arch-decision.
- **Software Design**: geometry/indexing/semantic engine în specificații dedicate.
- **Coding**: implementare în `sphere_rag/` și `scripts/`.
- **Testing**: self-tests, stress tests, validări de guard.
- **Integration**: legătură între atribuție semantică, geometrie, traversare, metrics.
- **Implementation**: scripturi CLI și flux deterministic de faze.
- **Operation & Maintenance**: fixed-point, evoluție controlată, issue-closure docs.

### 2.2 Software Development Paradigm
- **Waterfall**: util pentru secvența de formalizare a spec-urilor.
- **Iterative**: dominant în repo (v0.x → v1 fixed point → extensii).
- **Spiral**: prezent implicit prin risc + validări + iterații.
- **V-Model**: mapare între specificații și teste/self-tests.
- **Big Bang**: nerecomandat; evitat prin baseline-uri și guard discipline.

## 3. Software Project Management

### 3.1 Software Project
- Proiectul HESPERIA este un produs semantic-substrate cu ownership explicit, scope și artefacte de guvernanță.

### 3.2 Need of Software Project Management
- Fără management, un sistem complex semantic devine dificil de sincronizat, estimat și operat.
- În repo există procese clare pentru gates, scope, ownership și change control.

### 3.3 Software Project Manager
- **Managing People**: roluri clar definite (Grace, Ethan, Daniel, Sophia etc.).
- **Managing Project**: charter, context packet, WBS approval, handoff checklist.

### 3.4 Software Management Activities
- **Project Planning**: charter + context packet.
- **Scope Management**: `SCOPE-AND-SYNC.md`.
- **Project Estimation**: schedule baseline (durate/dev/infra).
- **Estimation Techniques**: placeholders pentru completare per task.
- **Project Scheduling**: baseline + ferestre de deploy/rollback când e cazul.
- **Resource Management**: assignment pe roluri.
- **Risk Management**: risk register.
- **Execution & Monitoring**: gates + rapoarte + release fixed point.
- **Communication Management**: artefact index + documente de stare.
- **Configuration Management**: baseline/fixed-point și reguli de schimbare.
- **Baseline**: release V1 fixed point.
- **Change Control**: CCB menționat în charter.
- **Project Management Tools**:
  - **Gantt Chart**: concept aplicabil (nu este încă completat în repo).
  - **PERT Chart**: concept aplicabil pentru dependențe.
  - **Resource Histogram**: derivabil din roluri și workload.
  - **Critical Path Analysis**: util când apar work packages concrete.

## 4. Software Requirements

### 4.1 Requirement Engineering
- Capturare, formalizare, validare și management al cerințelor.
- În HESPERIA, cerințele sunt exprimate în spec-urile numerotate și politici.

### 4.2 Requirement Engineering Process
- **Feasibility Study**: definită prin scope curent și constrângeri.
- **Requirement Gathering**: master spec + blueprint + specs tematice.
- **SRS**: familia de documente numerotate funcționează ca SRS distribuit.
- **Requirement Validation**: self-tests, guard checks, review de governance.

### 4.3 Requirement Elicitation Process
- În practică: owner/architecture/governance formulează cerințe, apoi sunt convertite în artefacte versionate.

### 4.4 Requirement Elicitation Techniques
- **Interviews / Surveys / Questionnaires**: reflectate indirect prin task-uri și rapoarte interne.
- **Task Analysis / Domain Analysis**: foarte puternice în specs geometrice/semantice.
- **Brainstorming**: vizibil în documentele de direcție și propuneri.
- **Prototyping**: `sphere_rag/` este prototip de referință determinist.
- **Observation**: rapoarte de stare și stress-test.

### 4.5 Software Requirements Characteristics
- Cerințele bune trebuie să fie clare, testabile, consistente, trasabile și prioritizate.
- HESPERIA folosește numerotare și versiuni pentru trasabilitate.

### 4.6 Functional Requirements
- Mapare text → arie/familie,
- Construire regiune semantică,
- Traversare de faze,
- Calcul metrici,
- Aplicare guard/gating.

### 4.7 Non-Functional Requirements
- Determinism, auditabilitate, consistență structurală, securitate și guvernanță a publicării.

### 4.8 User Interface Requirements
- UI principală actuală este orientată pe CLI/scripturi și output JSON.

### 4.9 Software System Analyst
- Rolul analistului este distribuit între architecture/governance și autorii de spec.

### 4.10 Software Metrics and Measures
- Metrici interne: entropy, coherence, tension, fragmentation, coverage, obstacle, decision integrity.

## 5. Software Design Basics

### 5.1 Software Design Levels
- **High-level**: model semantic geometric + servicii logice.
- **Low-level**: module Python, funcții și structuri de date deterministe.

### 5.2 Modularization
- Repo-ul e modular: specs, governance, project, scripts, `sphere_rag`.

### 5.3 Concurrency
- Nu este focus major în implementarea minimală curentă; designul favorizează determinismul secvențial.

### 5.4 Coupling and Cohesion
- Coeziune bună pe module tematice; coupling redus prin separarea clară pe responsabilități.

### 5.5 Design Verification
- Verificare prin aliniere cu specs, self-tests, guard checks și release baselines.

## 6. Software Analysis and Design Tools

- **DFD**: poate modela fluxul input → attribution → region → traversal → output.
- **Structure Charts**: aplicabile pe modulele `sphere_rag` + scripturi.
- **HIPO Diagram**: util pentru vizualizarea ierarhiei proceselor.
- **Structured English / Pseudo-code**: deja folosit frecvent în documentele spec.
- **Decision Tables**: potrivite pentru reguli guard (Σ/Γ/Θ).
- **ER Model / Data Dictionary**: aplicabile pentru schema de date statements/families/areas.

## 7. Software Design Strategies

- **Structured Design**: puternic prezent prin separarea pe fluxuri și specificații.
- **Function Oriented Design**: dominant în scripturi și pipeline procedural.
- **Object Oriented Design**: prezent moderat (tipuri/structuri), fără heavy OOP.

## 8. Software Design Approaches

- **Top-Down**: de la master spec la implementare.
- **Bottom-Up**: de la scripturi/prototip către consolidare în blueprint și politici.
- HESPERIA folosește un hibrid controlat între cele două.

## 9. Software User Interface Design

- **CLI**: interfața principală curentă (`scripts/*.py`).
- **GUI**: nu este focus în faza actuală.
- **UI Design Activities**: acum orientate pe operator interface textual și outputs structurate.
- **GUI Implementation Tools**: neaplicabil momentan.
- **UI Golden Rules**: consistență, feedback clar, control al erorilor, minimizarea ambiguității.

## 10. Software Design Complexity

- **Halstead**: aplicabil pentru evaluarea complexității implementării Python.
- **Cyclomatic Complexity**: relevant pentru traversal/guards/scripts.
- **Function Point**: util pentru estimarea livrabilelor funcționale viitoare.
- În prezent, repo-ul prioritizează complexitatea semantică + guvernanță, nu doar complexitatea de cod.

## 11. Software Implementation

- **Structured Programming**: implementare clar secvențială pe pași deterministici.
- **Functional Programming**: folosit parțial prin funcții pure/transformări.
- **Programming Style**: orientat pe claritate și mapare directă la specificații.
- **Coding Guidelines**: dictate de specs + AGENTS + politici.
- **Software Documentation**: foarte extinsă și versionată.
- **Implementation Challenges**: sincronizarea între spec, cod, guard discipline și scope curent.

## 12. Software Testing Overview

- **Validation vs Verification**:
  - Verification: „am construit corect conform spec?”
  - Validation: „construim ce este util și publicabil?”
- **Manual vs Automated**: ambele sunt necesare; repo-ul include scripturi de auto-validare.
- **Black-box / White-box**:
  - Black-box pe CLI/output,
  - White-box pe metrici și invariants.
- **Testing Levels**:
  - Unit: module individuale,
  - Integration: flux semantic + traversal,
  - System: rulare end-to-end,
  - Acceptance: gates de governance,
  - Regression: comparare față de fixed point.
- **Testing Documentation**: rapoarte, issue-closure, release docs.
- **Testing vs QC & QA**:
  - Testing = execuție verificări,
  - QC = controlul artefactelor,
  - QA = sistemul de procese și standarde.

## 13. Software Maintenance Overview

- **Tipuri de mentenanță**: corectivă, adaptivă, perfectivă, preventivă.
- **Costul mentenanței**: crește fără discipline de baseline/versioning.
- **Maintenance Activities**: update spec, sincronizare cod, retestare, documentare.
- **Software Re-Engineering**: posibil în jurul nucleului traversal/guard.
- **Reverse Engineering**: repo-ul permite reconstrucția logicii din docs + cod.
- **Forward Engineering**: din spec-uri numerotate către implementări noi.
- **Component Reusability**: modulele geometry/metrics/semantic_engine pot fi reutilizate.

## 14. Software CASE Tools Overview

- **CASE Tools**: ansamblu de unelte pentru analiză, design, cod, testare, management.
- **Components / Scope**: în HESPERIA includ documentație, scripturi, validări, guvernanță.
- **Diagram Tools / Modeling Tools**: recomandate pentru formalizarea fluxurilor.
- **Project Management Tools**: charter/context/schedule/risk ca bază.
- **Documentation Tools**: markdown/txt versionate și indexate.
- **Analysis / Design Tools**: specs numerotate + politici guard.
- **Configuration Management Tools**: git + baseline/fixed-point discipline.
- **Programming Tools**: Python scripts + module.
- **Prototyping Tools**: implementarea de referință din `sphere_rag`.
- **Web Development Tools**: neaplicabil în faza curentă.
- **Quality Assurance Tools**: checks, reviews, security baseline.
- **Maintenance Tools**: issue closure, release docs, evoluție versionată.

---

## Concluzie

Planul de „Software Engineering Tutorial” se poate aplica complet pe HESPERIA deoarece proiectul are deja toate elementele-cheie: specificații formale, implementare minimă, guvernanță, baseline-uri de proiect, politici de risc/securitate și disciplină de evoluție controlată.
