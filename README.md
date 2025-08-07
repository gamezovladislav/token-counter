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
usage: count_tokens.py [-h] [--model MODEL] path

Count tokens in text files for AI models

positional arguments:
  path                  Path to file or directory to analyze

optional arguments:
  -h, --help            show this help message and exit
  --model MODEL, -m MODEL
                        AI model for token counting (default: claude-3-7-sonnet-latest)
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