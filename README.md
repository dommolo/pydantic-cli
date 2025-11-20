# pydantic-config-generator

**pydantic-config-generator** è una libreria Python che fornisce prompt interattivi per la configurazione di modelli Pydantic. Permette di creare interfacce CLI interattive per raccogliere e validare dati secondo i tuoi modelli Pydantic.

## Caratteristiche

- 🎯 **Validazione automatica**: Usa la validazione di Pydantic per garantire dati corretti
- 🔄 **Supporto per modelli annidati**: Gestisce configurazioni complesse con modelli Pydantic annidati
- ⚡ **Facile da usare**: Basta passare il tuo modello Pydantic e pydantic-config-generator fa il resto
- 🛡️ **Type-safe**: Sfrutta il sistema di tipi di Pydantic
- 💾 **Salvataggio in file**: Salva le configurazioni in formato INI per un uso successivo

## Installazione

```bash
pip install pydantic-config-generator
```

## Utilizzo

### Esempio Base

```python
from pydantic import BaseModel
from pydantic_config_generator import run

class ExampleConfig(BaseModel):
    name: str = ''
    surname: str
    age: int
    is_student: bool = True

# Avvia il prompt interattivo
config = run(ExampleConfig)
```

### Esempio con Modelli Annidati

```python
from pydantic import BaseModel
from pydantic_config_generator import run

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

config = run(ExampleConfig)
```

Il sistema ti chiederà di inserire i valori per ogni campo, mostrando i valori di default tra parentesi quadre. I campi obbligatori devono essere compilati, mentre quelli opzionali possono essere saltati.

### Salvare la Configurazione in un File

Dopo aver raccolto la configurazione tramite `run()`, puoi salvarla in un file INI usando la funzione `write()`:

```python
from pydantic import BaseModel
from pydantic_config_generator import run, write

class ExampleConfig(BaseModel):
    name: str = ''
    surname: str
    age: int
    is_student: bool = True

# Raccogli la configurazione
config = run(ExampleConfig)

# Salva in un file INI
write(config, 'config.ini')
```

La funzione `write()` salva la configurazione in formato INI. Se il file esiste già, ti chiederà conferma prima di sovrascriverlo. I modelli annidati vengono salvati come sezioni separate nel file INI.

## Come Funziona

1. **Campi semplici**: Per ogni campo del modello, pydantic-config-generator chiede un valore, mostrando il default se disponibile
2. **Validazione**: Ogni input viene validato secondo le regole del modello Pydantic
3. **Modelli annidati**: Se un campo è un modello Pydantic, pydantic-config-generator chiede se includerlo (se opzionale) e poi richiede i suoi campi
4. **Gestione errori**: Se un valore non è valido, viene mostrato un errore e viene richiesto di nuovo
5. **Salvataggio in file**: La funzione `write()` salva la configurazione in formato INI, dove ogni campo del modello diventa una sezione con le sue proprietà come opzioni. I modelli annidati vengono salvati come sezioni separate

## Requisiti

- Python >= 3.7
- pydantic >= 1.0, < 2.0

## Licenza

MIT License

## Contribuire

I contributi sono benvenuti! Sentiti libero di aprire issue o pull request.

