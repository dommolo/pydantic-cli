# pydantic-cli

**pydantic-cli** è una libreria Python che fornisce prompt interattivi per la configurazione di modelli Pydantic. Permette di creare interfacce CLI interattive per raccogliere e validare dati secondo i tuoi modelli Pydantic.

## Caratteristiche

- 🎯 **Validazione automatica**: Usa la validazione di Pydantic per garantire dati corretti
- 🔄 **Supporto per modelli annidati**: Gestisce configurazioni complesse con modelli Pydantic annidati
- ⚡ **Facile da usare**: Basta passare il tuo modello Pydantic e pydantic-cli fa il resto
- 🛡️ **Type-safe**: Sfrutta il sistema di tipi di Pydantic

## Installazione

```bash
pip install pydantic-cli
```

## Utilizzo

### Esempio Base

```python
from pydantic import BaseModel
from pydantic_cli import run

class ExampleConfig(BaseModel):
    name: str = ''
    surname: str
    age: int
    is_student: bool = True

# Avvia il prompt interattivo
run(ExampleConfig)
```

### Esempio con Modelli Annidati

```python
from pydantic import BaseModel
from pydantic_cli import run

class ExampleSubConfig(BaseModel):
    name: str
    surname: str
    age: int

class ExampleConfig(BaseModel):
    name: str = ''
    surname: str
    age: int
    is_student: bool = True
    teacher: ExampleSubConfig = None

run(ExampleConfig)
```

Il sistema ti chiederà di inserire i valori per ogni campo, mostrando i valori di default tra parentesi quadre. I campi obbligatori devono essere compilati, mentre quelli opzionali possono essere saltati.

## Come Funziona

1. **Campi semplici**: Per ogni campo del modello, pydantic-cli chiede un valore, mostrando il default se disponibile
2. **Validazione**: Ogni input viene validato secondo le regole del modello Pydantic
3. **Modelli annidati**: Se un campo è un modello Pydantic, pydantic-cli chiede se includerlo (se opzionale) e poi richiede i suoi campi
4. **Gestione errori**: Se un valore non è valido, viene mostrato un errore e viene richiesto di nuovo

## Requisiti

- Python >= 3.7
- pydantic >= 1.0, < 2.0

## Licenza

MIT License

## Contribuire

I contributi sono benvenuti! Sentiti libero di aprire issue o pull request.

