# 🔢 Token Counter ✨

> *Vibe check your AI costs with this super lit token counter!* 💸

A simple yet powerful utility for counting tokens in text files for AI language models. This tool supports both OpenAI and Anthropic models, providing accurate token counts for cost estimation and context length management. No cap!

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.6+-blue.svg" alt="Python 3.6+">
  <img src="https://img.shields.io/badge/OpenAI-Compatible-green.svg" alt="OpenAI Compatible">
  <img src="https://img.shields.io/badge/Anthropic-Compatible-purple.svg" alt="Anthropic Compatible">
</div>

## ✨ Features

- 📁 Count tokens in individual files or entire directories
- 🤖 Support for multiple AI models:
  - **OpenAI models**: gpt-4, gpt-4o, gpt-4.1, o1, o3, o4-mini
  - **Anthropic models**: claude-3-7-sonnet-latest (default), claude-3-5-haiku-latest, claude-3-5-sonnet-latest, claude-3-opus-latest, claude-sonnet-4-0, claude-opus-4-0, and many more version-specific models
- 🔄 Automatic selection of the appropriate tokenizer based on the specified model
- 🌈 Colorized output for better readability
- 📊 Detailed summary statistics
- 🛟 Fallback counting method when tokenizer libraries are not available or encounter errors

## 🚀 Installation

> *Three easy steps and you're ready to flex!* 💯

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/token-counter.git
   cd token-counter
   ```

2. (Optional) Create a virtual environment:
   
   **Windows:** 🪟
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **macOS/Linux:** 🐧
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📋 Requirements

> *Minimal dependencies, maximum vibes* ✌️

- 🐍 Python 3.6 or higher
- 🟢 tiktoken (for OpenAI models)
- 🟣 anthropic (for Anthropic models)
- 🌱 python-dotenv (for .env file configuration)

## 🔥 Usage

> *Let's get this token bread!* 🍞

### 🔍 Basic Usage

Count tokens in a single file:
```bash
python count_tokens.py path/to/file.txt
```

Count tokens in a directory (recursively):
```bash
python count_tokens.py path/to/directory
```

### 🤖 Specifying a Model

Count tokens using a specific model:
```bash
python count_tokens.py path/to/file.txt --model gpt-4
```

#### Available Models:

| 🟢 **OpenAI** | 🟣 **Anthropic** |
|--------------|-----------------|
| gpt-4        | claude-3-7-sonnet-latest (default) |
| gpt-4o       | claude-3-5-haiku-latest |
| gpt-4.1      | claude-3-5-sonnet-latest |
| o1           | claude-3-opus-latest |
| o3           | claude-sonnet-4-0 |
| o4-mini      | claude-opus-4-0 |
|              | *and many more version-specific models* |

## ⌨️ Command-line Options

```bash
usage: count_tokens.py [-h] [--model MODEL] [--pretty-output [BOOL]] path

Count tokens in text files for AI models

positional arguments:
  path                  Path to file or directory to analyze

optional arguments:
  -h, --help            show this help message and exit
  --model MODEL, -m MODEL
                        AI model for token counting (default: from .env or claude-3-7-sonnet-latest)
  --pretty-output, -p [BOOL]
                        Enable/disable colorized output (default from PRETTY_OUTPUT or True). When provided
                        without a value, it enables colors. Accepted values: true/false, 1/0, yes/no, on/off.
```

### Pretty Output Toggle
- CLI (single property):
  - `count_tokens.py path` -> colors ON (default from PRETTY_OUTPUT or True)
  - `count_tokens.py --pretty-output path` -> colors ON
  - `count_tokens.py --pretty-output false path` -> colors OFF
  - Accepted values for BOOL: true/false, 1/0, yes/no, on/off (case-insensitive)
- Environment: set `PRETTY_OUTPUT=false` to change the default (accepted values: 1/0, true/false, yes/no, on/off; default: true).

## ⚙️ Configuration with .env File

> *Customize your token counting experience!* 🛠️

You can configure the token counter using a `.env` file in the project root directory. Create a copy of the `.env.example` file and rename it to `.env`:

```bash
cp .env.example .env
```

### Available Configuration Options:

| Variable | Description | Example |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Anthropic API key used for Claude models | `sk-ant-...` |
| `CLAUDE_API_KEY` | Optional alias for Anthropic API key (fallback if ANTHROPIC_API_KEY is not set) | `sk-ant-...` |
| `OPENAI_MODELS` | Comma-separated list of available OpenAI models | `o1,o3,o4-mini,gpt-4.1,gpt-4o,gpt-4` |
| `ANTHROPIC_MODELS` | Comma-separated list of available Anthropic models | `claude-3-7-sonnet-latest,claude-3-5-haiku-latest` |
| `DEFAULT_MODEL` | Default model to use when not specified | `claude-3-7-sonnet-latest` |
| `IGNORE_DIRS` | Directories to ignore during processing | `.git,.idea,.vscode,__pycache__,venv` |
| `IGNORE_EXTENSIONS` | File extensions to ignore during processing | `.jpg,.jpeg,.png,.gif,.exe` |
| `PRETTY_OUTPUT` | Toggle colorized console output (boolean) | `true` or `false` |

### Example .env File:

```
# Token Counter Configuration

# Anthropic API Key (required when using Claude models)
ANTHROPIC_API_KEY=sk-ant-your-api-key-here
# Optional alias if you prefer: CLAUDE_API_KEY=sk-ant-your-api-key-here

# OpenAI Models (comma-separated list)
OPENAI_MODELS=o1,o3,o4-mini,gpt-4.1,gpt-4o,gpt-4

# Anthropic Models (comma-separated list)
ANTHROPIC_MODELS=claude-3-7-sonnet-latest,claude-3-5-haiku-latest,claude-3-opus-latest

# Default Model (must be included in one of the model lists above)
DEFAULT_MODEL=gpt-4o

# Directories to ignore (comma-separated list)
IGNORE_DIRS=.git,.idea,.vscode,__pycache__,venv,node_modules,.venv

# File extensions to ignore (comma-separated list)
IGNORE_EXTENSIONS=.jpg,.jpeg,.png,.gif,.exe,.dll,.pyc,.pyo

# Pretty output (colors): true/false (default true)
PRETTY_OUTPUT=true
```

## 💯 Examples

> *Check out these sick examples!* 🔥

<details open>
<summary>🔍 <b>Example 1:</b> Count tokens in a single file</summary>

```bash
$ python count_tokens.py sample.txt
============================================================
  TOKEN COUNTER
  Model: claude-3-7-sonnet-latest
============================================================
File: sample.txt
  Characters: 239
  Tokens: 49

Summary:
Characters: 239
Tokens: 49
============================================================
```
</details>

<details>
<summary>🟣 <b>Example 2:</b> Count tokens with specific Claude model</summary>

```bash
$ python count_tokens.py sample_claude.txt --model claude-3-opus-latest
============================================================
  TOKEN COUNTER
  Model: claude-3-opus-latest
============================================================
File: sample_claude.txt
  Characters: 488
  Tokens: 101

Summary:
Characters: 488
Tokens: 101
============================================================
```
</details>

<details>
<summary>🟢 <b>Example 3:</b> Count tokens with OpenAI model</summary>

```bash
$ python count_tokens.py sample.txt --model gpt-4
============================================================
  TOKEN COUNTER
  Model: gpt-4
============================================================
File: sample.txt
  Characters: 239
  Tokens: 45

Summary:
Characters: 239
Tokens: 45
============================================================
```
</details>

<details>
<summary>📁 <b>Example 4:</b> Count tokens in a directory</summary>

```bash
$ python count_tokens.py ./docs
============================================================
  TOKEN COUNTER
  Model: claude-3-7-sonnet-latest
============================================================

Processing directory: ./docs
Using model: claude-3-7-sonnet-latest
File: ./docs/introduction.txt
  Characters: 1250
  Tokens: 245
File: ./docs/tutorial.txt
  Characters: 3500
  Tokens: 680

Summary:
Files processed: 2
Total characters: 4 750
Total tokens: 925
============================================================
```
</details>

## 🧠 How It Works

> *The secret sauce behind the magic!* ✨

The token counter works by:

1. 📖 Reading the content of text files
2. 🔄 Using the appropriate tokenizer library based on the selected model:
   - 🟢 **tiktoken** for OpenAI models (gpt-4, gpt-4o, etc.)
   - 🟣 **anthropic** for Anthropic models (claude-3-7-sonnet-latest, etc.)
3. 🧮 Counting the tokens using the selected tokenizer
4. 📊 Providing a summary of the results

### 🛟 Fallback Mechanism

<details>
<summary><b>What happens if something goes wrong?</b> (click to expand)</summary>

If the tokenizer libraries encounter errors (such as initialization issues or compatibility problems), the tool automatically falls back to a simple regex-based token counting method. This ensures that the tool continues to function even when:

- ❌ The required libraries are not installed
- 🔄 There are version compatibility issues
- 🌐 Environment-specific configuration problems occur

When the fallback method is used, a warning message is displayed, but the tool continues to provide approximate token counts.
</details>

## 💰 Why Token Counting Matters

> *Know your tokens, save your coins!* 💸

Accurate token counting is **super important** for:

- 💵 Estimating API costs when using AI language models
- 📏 Ensuring your prompts fit within model context limits
- 🚀 Optimizing prompt design for efficiency

## 👥 Contributing

> *Join the squad and make this tool even more fire!* 🔥

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">
  <p>Made with ❤️ for the AI community</p>
  <p>© 2025 - Stay vibin'! ✌️</p>
</div>