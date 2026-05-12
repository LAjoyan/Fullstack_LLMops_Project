# Way of Working

## Mål
- Målsättning: Prova uppgifterna på VG-nivå.
- Fokus på samarbetet och lärande.

---

# Arbetstider

## Kärntider
Alla förväntas vara tillgängliga vardagar mellan:

**Kl. 10:00–15:00**

Utanför kärntider arbetar man flexibelt efter behov.

---

# Arbetssätt

## Dagliga avstämningar

### Standup – kl. 10:00
Digital standup varje morgon.

Syfte:
- Vad arbetar jag med idag?
- Har jag fastnat?
- Behöver jag hjälp?

Tidsgräns:
- Max 15 minuter.

### Löpande kommunikation
- Korta frågor och avstämningar sker via Discord under dagen.
- Vid större frågor bokas ett snabbt möte.

### Dagens avslut – kl. 14:45
Kort gemensam avstämning:
- Vad blev klart idag?
- Finns blockers inför morgondagen?

---

# Kod- och samarbetsprinciper

## Arbetsfördelning
- Vi arbetar parallellt med olika delar av projektet.
- Kod ska vara möjlig för andra att ta över vid behov.
- Fokus på kunskapsdelning mellan gruppmedlemmar.

## Pull Requests
- Håll PR:s små och fokuserade.
- Alla PR:s ska granskas av alla innan merge till `main`.
- Kommentarer och code reviews sker i GitHub.
- Vid större frågor kring implementation tas ett kort möte.

## Branch-strategi
- Feature branches används för ny funktionalitet.
- Fix branches används för fixar. 

Exempel:
```bash
feature/rag-pipeline
feature/frontend-chat
fix/mlflow-logging