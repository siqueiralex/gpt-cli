# GPT-CLI
Welcome to GPT-CLI, a simple for interacting with ChatGPT in your Terminal. 

GPT-CLI also includes a variety of helper functions designed to enhance productivity.

## OpenAI API Key

Before running the code in this repository, please make sure to export your OpenAI API key to the environment.

To export your API key, you can set it as an environment variable in your terminal by running the following command:

```bash
export OPENAI_API_KEY=<your_api_key_here>
```

Replace `<your_api_key_here>` with your actual OpenAI API key.

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

### gpt-cli term
To get assistance with Terminal Commands:

```bash
gpt-cli term 'list all files in folder with .txt extension'
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
gpt-cli python "python function to generate a random number"
$ random.randint(1, 100) # <- will be already on your clipboard
```


### Further Options

Users are able to change the model, the max number of tokens and the temperature

```bash
gpt-cli python 'check if a number is prime' --gpt 4 --temperature .5 --max-tokens 100
```

Users can skip the prompt, so gpt-cli will shortly ask you to provide it.

```bash
gpt-cli en
Prompt:
```