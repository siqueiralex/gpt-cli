# gpt-cli
Use GPT in your Terminal

## Overview
Welcome to gpt-cli, a simple command line interface (CLI) for interacting with Chat GPT. This tool is designed to help you communicate with Chat GPT and keep a history of your conversations. GPT-CLI also features a helper function for CLI commands, as well as for various languages including English, Portuguese, and Python. The text you want is conveniently returned to your clipboard for easy access and use.

## Usage
The basic command structure for gpt-cli is as follows:

```bash
gpt-cli [OPTIONS] COMMAND [ARGS]...
```

## Commands
The `gpt-cli` utility provides several commands:


### gpt-cli chat
To start a conversation with Chat GPT and maintain a history of your conversations:

```bash
gpt-cli chat
```

### gpt-cli cli
To get assistance with Command Line commands:

```bash
gpt-cli cli 'list all files in folder with .txt extension'
$ "ls *.txt" # <- will be already on your clipboard
```

### gpt-cli en

To get assistance with English language queries and receive enhanced responses:

```bash
gpt-cli en "Hello, how is you?"
$ "Hello, how are you?" # <- will be already on your clipboard
```

### gpt-cli pt
To receive an enhanced response in Portuguese for a given phrase:

```bash
gpt-cli pt "Olá, como tá?"
$ "Olá, como está você?" # <- will be already on your clipboard
```

### gpt-cli python
To get a Python-related inquiry, such as requesting a specific function:

```bash
gpt-cli python --prompt "python function to generate a random number"
$ random.randint(1, 100) # <- will be already on your clipboard
```