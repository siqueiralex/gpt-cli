import os
import sys
import fpdf
import time
import typer
import pyperclip
from openai import OpenAI
from datetime import datetime

gpt_model = {
    '3.5-turbo' : 'gpt-3.5-turbo',
    '4' : 'gpt-4',
    '4-turbo' : 'gpt-4-turbo-preview'
}


def simulate_typing(text, delay=0.01):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)




main = typer.Typer(name="GPT Snippets CLI", add_completion=False, no_args_is_help=True,)
        

@main.command()
def en(prompt: str = typer.Argument(""), gpt: str = '3.5-turbo', max_tokens:int = 2048, temperature:float = .8):
    typer.echo(gpt_model[gpt])
    typer.echo(f'{temperature=}')
    typer.echo(f'{max_tokens=}')
    prompt = typer.prompt("Prompt") if not prompt else prompt
    if prompt.lower().strip() == 'exit': return
    
    openai_client = OpenAI()
    
    messages = [
        { 'role' : 'system', 'content' : """
        You are an english expert. The only thing you do is enhance the phrasing of the prompt.
        You are never too formal, you speak normal as an ESL speaker would, with no uncommon words but making no mistakes.
        Make sure you only respond with the corrected phrase, no comments
        """ 
        },
        {'role' : 'user', 'content' : prompt}
    ]
    
    response = openai_client.chat.completions.create(
        model = gpt_model[gpt],
        temperature = temperature,
        messages = messages,
        max_tokens= max_tokens
    )
    
    pyperclip.copy(response.choices[0].message.content)
    typer.echo(response.choices[0].message.content)

@main.command()
def pt(prompt: str = typer.Argument(""), gpt: str = '3.5-turbo', max_tokens:int = 2048, temperature:float = .8):
    typer.echo(gpt_model[gpt])
    typer.echo(f'{temperature=}')
    typer.echo(f'{max_tokens=}')
    prompt = typer.prompt("Prompt") if not prompt else prompt
    if prompt.lower().strip() == 'exit': return
    
    openai_client = OpenAI()
    
    messages = [
        { 'role' : 'system', 'content' : """
        Você é um expert em português do Brasil. A única coisa que você faz é responder com a frase do usuário melhorada.
        Não precisa ser muito formal, mas você escreve muito corretamente e claramente.
        Não esqueça: você deve apenas responder com a mensagem do usuário melhorando a escrita, sem comentários adicionais.
        """ 
        },
        {'role' : 'user', 'content' : prompt}
    ]
    
    response = openai_client.chat.completions.create(
        model = gpt_model[gpt],
        temperature = temperature,
        messages = messages,
        max_tokens= max_tokens
    )
    
    pyperclip.copy(response.choices[0].message.content)
    typer.echo(response.choices[0].message.content)

@main.command()
def cli(prompt: str = typer.Argument(""), gpt: str = '3.5-turbo', max_tokens:int = 2048, temperature:float = .8):
    typer.echo(gpt_model[gpt])
    typer.echo(f'{temperature=}')
    typer.echo(f'{max_tokens=}')
    prompt = typer.prompt("Prompt") if not prompt else prompt
    if prompt.lower().strip() == 'exit': return
    
    openai_client = OpenAI()
    
    messages = [
        { 'role' : 'system', 'content' : """
        You are a CLI and Assistant. Specilized in Macos compatible commands. 
        You only respond with the command the person asked, with nothing around it, 
        just ready-to-use command without any quotes around it.
        You never use Markdown code snippet annotation, you just respond with the code.
        """ 
        },
        {'role' : 'user', 'content' : prompt}
    ]
    
    response = openai_client.chat.completions.create(
        model = gpt_model[gpt],
        temperature = temperature,
        messages = messages,
        max_tokens= max_tokens
    )
    
    pyperclip.copy(response.choices[0].message.content)
    typer.echo(response.choices[0].message.content)


@main.command()
def python(prompt: str = typer.Argument(""), gpt: str = '3.5-turbo', max_tokens:int = 2048, temperature:float = .8):
    typer.echo(gpt_model[gpt])
    typer.echo(f'{temperature=}')
    typer.echo(f'{max_tokens=}')
    prompt = typer.prompt("Prompt") if not prompt else prompt
    if prompt.lower().strip() == 'exit': return
    
    openai_client = OpenAI()
    
    messages = [
        { 'role' : 'system', 'content' : """
        You are a Python Assistant. Specilized in Python3 efficient code. 
        You only respond with the code the person asked, with nothing around it, 
        just ready-to-use code without any quotes around it.
        You never use Markdown code snippet annotation, you just respond with the code.
        """ 
        },
        {'role' : 'user', 'content' : prompt}
    ]
    
    response = openai_client.chat.completions.create(
        model = gpt_model[gpt],
        temperature = temperature,
        messages = messages,
        max_tokens=max_tokens
    )
    
    pyperclip.copy(response.choices[0].message.content)
    typer.echo(response.choices[0].message.content)

    
    
    
    
@main.command()
def chat(gpt: str = '3.5-turbo', max_tokens:int = 2048, temperature:float = .8):
    typer.echo(gpt_model[gpt])
    typer.echo(f'{temperature=}')
    typer.echo(f'{max_tokens=}')
    hist = []
    while True:
        prompt = typer.prompt("Prompt")
        if prompt.lower().strip() == 'exit': return
        if prompt.lower().strip() == 'save last':
            content = complete_response
            filename = typer.prompt("Filename")
            if filename.lower().strip() == 'clipboard': return pyperclip.copy(content)

            current_directory = os.getcwd()
            filepath = os.path.join(current_directory, filename)
            if filepath.endswith('.pdf'):
                pdf = fpdf.FPDF()
                pdf.add_page()
                pdf.set_font("Helvetica", size = 12)
                pdf.multi_cell(0, 10, content)
                pdf.output(filepath)
                
            else:
                with open(filepath, 'w') as file:
                    file.write(content)
                                
            typer.echo('Saved to: ' +   filepath)
            
            continue

        if prompt.lower().strip() == 'save':
            
            content = f"Conversation in {datetime.now().strftime("%d/%m/%Y %H:%M")}\n\n"
            for i in range(0, len(hist), 2):
                item1 = hist[i]
                item2 = hist[i + 1]
                content += f"{item1['content']}\n{item2['content']}\n"+'*'*80+"\n"
                
            filename = typer.prompt("Filename")
            if filename.lower().strip() == 'clipboard': return pyperclip.copy(content)
            
            current_directory = os.getcwd()
            filepath = os.path.join(current_directory, filename)
            if filepath.endswith('.pdf'):
                pdf = fpdf.FPDF()
                pdf.add_page()
                pdf.set_font("Helvetica", size = 12)
                pdf.multi_cell(0, 10, content)
                pdf.output(filepath)
                
            else:
                with open(filepath, 'w') as file:
                    file.write(content)
                                
            typer.echo('Saved to: ' +   filepath)
            return
        
        openai_client = OpenAI()

        messages = [ *hist,
            {'role' : 'user', 'content' : prompt}
        ]
        
        response = openai_client.chat.completions.create(
            model = gpt_model[gpt],
            temperature = temperature,
            max_tokens = max_tokens,
            messages = messages,
            stream = True
        )
        
        complete_response = ''
        for chunk in response:
            chunk_message = chunk.choices[0].delta.content
            if chunk_message:
                complete_response += chunk_message
                simulate_typing(f"{chunk_message}")
        print()
        
        hist.append({'role' : 'user', 'content' : prompt})
        hist.append({'role' : 'assistant', 'content' : complete_response})
        

