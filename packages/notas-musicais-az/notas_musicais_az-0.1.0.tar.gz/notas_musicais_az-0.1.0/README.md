<p align="left">
  <img src="https://notas-musicais-azevedo.readthedocs.io/pt/latest/assets/logo.png" alt="Logo notas musicais" width="20%">
</p>

# Notas musicais

[![Documentation Status](https://readthedocs.org/projects/notas-musicais-azevedo/badge/?version=latest)](https://notas-musicais-azevedo.readthedocs.io/pt/latest/?badge=latest)
[![codecov](https://codecov.io/gh/azmovi/notas-musicais/graph/badge.svg?token=2S97895YU9)](https://codecov.io/gh/azmovi/notas-musicais)
![CI](https://github.com/azmovi/notas-musicais/actions/workflows/pipeline.yaml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos harmônicos

Temos dois comandos diponíveis: `escala`, `acorde` e `campo-harmonico`

## Como instalar o projeto

para instalação do cli do projeto recomendamos que use o `pipx` para fazer essa
instalação:

```bash
pipx install notas-musicais-az
```

Embora isso seja somente uma recomendação! Você também pode instalar pode instalar
o projeto com o gerenciador da sua preferência. Como o pip:

```bash
pip install notas-musicais-az
```

## Como usar?

### Escalas

Você pode chamar as escalas via linha de comando. Por exemplo:


```bash
notas-musicais escala
```
Retornando os graus e as notas correspondentes a essa escala:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘

```
#### Alteração da tônica da escala

O primeiro parâmentro do CLI é a tônica da escala que deseja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala 'F#':

```bash
notas-musicais escala F#
```
Resultado em: 
```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘

```
#### Alteração na tonalidade da escala
Você pode alterar a tonalidade da escala também! Esse é o segundo parâmentro da linha de comando. Por exemplo, a escala 'D#' maior:
```bash
notas-musicais escala D# maior 
```
Resultado em:
```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘

```
## Acordes 

Uso básico

```bash
notas-musicais acorde
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

### Variações na cifra

```bash
notas-musicais acorde C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```
Até o momento você pode usar acordes maiores, menores, diminutos, aumentads.

## Campo Harmônico
Você pode chamar os campos harmônicos via o subcomando `campo-harmonico`. Por exemplo:

```bash
notas-musicais campo-harmonico
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

Por padrão os parâmentros utilizados são a tônica `C` e a tonalidade `maior`

### Alterações nos campos harmônicos

Você pode alterar os parâmentros da tônica e da tonalidade.

```bash
notas-musicais campo-harmonio [OPTIONS] [TONICA] [TONALIDADE]
```
#### Alteração na tônica do campo harmônico

Um exemplo com o campo hamônico de `E`

```bash
notas-musicais campo-harmonio E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Alteração da tonalidade do campo

Um exemplo com o campo hamônico de `E` na tonalidade `menor`

```bash
notas-musicais campo-harmonio E menor

┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## Mais infromações sobre o CLI

Para descobrir outras opções, você pode usar a flag '--help'

```bash
notas-musicais --help

```

Resultado em:
```bash
Usage: notas-musicais [OPTIONS] COMMAND [ARGS]...                                                     
                                                                                                       
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified   │
│                                                              shell.                                 │
│                                                              [default: None]                        │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified      │
│                                                              shell, to copy it or customize the     │
│                                                              installation.                          │
│                                                              [default: None]                        │
│ --help                                                       Show this message and exit.            │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────╮
│ acorde 
│ campo-harmonico
│ escala                                                                                              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
