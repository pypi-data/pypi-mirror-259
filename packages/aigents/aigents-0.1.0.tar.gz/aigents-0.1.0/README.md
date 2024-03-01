# aigents

Adapters for Large Language Models and Generative Pre-trained Transformers APIs

## Installation

```bash
$ poetry install
```

## Usage

This section provides a brief overview of the classes in `core.py` and their usage.

### OpenAIChatter

The `OpenAIChatter` class is a synchronous chatbot that uses OpenAI's GPT-3 model to generate responses to prompts by default.

```python
# Initialize the chatbot
chatbot = OpenAIChatter(
    setup="You are a very skilled writer.",
    api_key="your_openai_api_key",
    temperature=0.8,
    model="gpt-3"
)

# Generate a response to a prompt
response = chatbot.answer("Hello, how are you?")
print(response)
```

Optionally you can switch the model:
```python
chatbot.change_model('gtp4-turbo-preview')
```


## AsyncOpenAIChatter

The `AsyncOpenAIChatter` class is an asynchronous version of `OpenAIChatter`. It works similarly to `OpenAIChatter`, but its `answer` method is a coroutine that must be awaited.

### Usage

```python
# Initialize the chatbot
chatbot = AsyncOpenAIChatter(
    setup="You are a very skilled writer.",
    api_key="your_openai_api_key",
    temperature=0.8,
    model="gpt-3"
)

# Generate a response to a prompt
response = await chatbot.answer("Hello, how are you?")
print(response)
```

## GoogleChatter

The `GoogleChatter` class is a synchronous chatbot that uses Google's Generative AI model to generate responses to prompts.

### Usage

```python
# Initialize the chatbot
chatbot = GoogleChatter(
    setup="You are a very skilled writer.",
    api_key="your_google_ai_api_key",
    temperature=0.8
)

# Generate a response to a prompt
response = chatbot.answer("Hello, how are you?")
print(response)
```

## AsyncGoogleChatter

The `AsyncGoogleChatter` class is an asynchronous version of `GoogleChatter`. It works similarly to `GoogleChatter`, but its `answer` method is a coroutine that must be awaited.

### Usage

```python
# Initialize the chatbot
chatbot = AsyncGoogleChatter(
    setup="You are a very skilled writer.",
    api_key="your_google_ai_api_key",
    temperature=0.8
)

# Generate a response to a prompt
response = await chatbot.answer("Hello, how are you?")
print(response)
```

## BingChatter

The `BingChatter` class is a synchronous chatbot that uses Bing's chat completions provider to generate responses to prompts. This class uses [g4f](https://github.com/xtekky/gpt4free/tree/main) adpter.

### Usage

```python
# Initialize the chatbot
chatbot = BingChatter(
    setup="You are a very skilled writer.",
    api_key="your_bing_api_key"
)

# Generate a response to a prompt
response = chatbot.answer("Hello, how are you?")
print(response)
```

## AsyncBingChatter

The `AsyncBingChatter` class is an asynchronous version of `BingChatter`. It works similarly to `BingChatter`, but its `answer` method is a coroutine that must be awaited.

### Usage

```python
# Initialize the chatbot
chatbot = AsyncBingChatter(
    setup="You are a very skilled writer.",
    api_key="your_bing_api_key"
)

# Generate a response to a prompt
response = await chatbot.answer("Hello, how are you?")
print(response)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`aigents` was created by Vagner Bessa. Vagner Bessa retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.

## Credits

`aigents` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
