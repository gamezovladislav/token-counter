# Token Counter

A simple utility for counting tokens in text files for AI language models. This tool supports both OpenAI and Anthropic models, providing accurate token counts for cost estimation and context length management.

## Features

- Count tokens in individual files or entire directories
- Support for multiple AI models:
  - OpenAI models: gpt-3.5-turbo, gpt-4, gpt-4-turbo
  - Anthropic models: claude-3-opus, claude-3-sonnet, claude-3-haiku
- Simple flag (--anthropic) to use Anthropic tokenizer without specifying a model
- Automatic selection of the appropriate tokenizer based on the specified model
- Colorized output for better readability
- Detailed summary statistics
- Fallback counting method when tokenizer libraries are not available or encounter errors

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/token-counter.git
   cd token-counter
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Requirements

- Python 3.6 or higher
- tiktoken (for OpenAI models)
- anthropic (for Anthropic models)

## Usage

### Basic Usage

Count tokens in a single file:
```
python count_tokens.py path/to/file.txt
```

Count tokens in a directory (recursively):
```
python count_tokens.py path/to/directory
```

### Specifying a Model

Count tokens using a specific model:
```
python count_tokens.py path/to/file.txt --model gpt-4
```

Available models:
- OpenAI: gpt-3.5-turbo (default), gpt-4, gpt-4-turbo
- Anthropic: claude-3-opus, claude-3-sonnet, claude-3-haiku

### Using Anthropic Tokenizer

Count tokens using the Anthropic tokenizer:
```
python count_tokens.py path/to/file.txt --anthropic
```

This flag simplifies token counting for Anthropic models without needing to specify a particular model.


## Command-line Options

```
usage: count_tokens.py [-h] [--model {gpt-3.5-turbo,gpt-4,gpt-4-turbo,claude-3-opus,claude-3-sonnet,claude-3-haiku}] [--anthropic] path

Count tokens in text files for AI models

positional arguments:
  path                  Path to file or directory to analyze

optional arguments:
  -h, --help            show this help message and exit
  --model {gpt-3.5-turbo,gpt-4,gpt-4-turbo,claude-3-opus,claude-3-sonnet,claude-3-haiku}, -m {gpt-3.5-turbo,gpt-4,gpt-4-turbo,claude-3-opus,claude-3-sonnet,claude-3-haiku}
                        AI model for token counting (default: gpt-3.5-turbo)
  --anthropic, -a       Use Anthropic tokenizer instead of OpenAI
```

## Examples

### Example 1: Count tokens in a single file

```
$ python count_tokens.py sample.txt
============================================================
  TOKEN COUNTER
  Model: gpt-3.5-turbo
============================================================
File: sample.txt
  Characters: 239
  Tokens: 49

Summary:
Characters: 239
Tokens: 49
============================================================
```

### Example 2: Count tokens with Anthropic tokenizer

```
$ python count_tokens.py sample_claude.txt --anthropic
============================================================
  TOKEN COUNTER
  Tokenizer: Anthropic
============================================================
File: sample_claude.txt
  Characters: 488
  Tokens: 101

Summary:
Characters: 488
Tokens: 101
============================================================
```

### Example 3: Count tokens with specific Claude model

```
$ python count_tokens.py sample_claude.txt --model claude-3-opus
============================================================
  TOKEN COUNTER
  Model: claude-3-opus
============================================================
File: sample_claude.txt
  Characters: 488
  Tokens: 101

Summary:
Characters: 488
Tokens: 101
============================================================
```

### Example 4: Count tokens in a directory

```
$ python count_tokens.py ./docs
============================================================
  TOKEN COUNTER
  Model: gpt-3.5-turbo
============================================================

Processing directory: ./docs
Using model: gpt-3.5-turbo
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

### Example 5: Count tokens in a directory with Anthropic tokenizer

```
$ python count_tokens.py ./docs --anthropic
============================================================
  TOKEN COUNTER
  Tokenizer: Anthropic
============================================================

Processing directory: ./docs
Using Anthropic tokenizer
File: ./docs/introduction.txt
  Characters: 1250
  Tokens: 240
File: ./docs/tutorial.txt
  Characters: 3500
  Tokens: 670

Summary:
Files processed: 2
Total characters: 4 750
Total tokens: 910
============================================================
```

## How It Works

The token counter works by:

1. Reading the content of text files
2. Using the appropriate tokenizer library based on the selected options:
   - tiktoken for OpenAI models (gpt-3.5-turbo, gpt-4, gpt-4-turbo)
   - anthropic for Anthropic models or when the --anthropic flag is used
3. Counting the tokens using the selected tokenizer
4. Providing a summary of the results

When using the --anthropic flag, the tool uses the Anthropic tokenizer directly without needing to specify a particular Claude model, since the tokenization is the same across all Claude models.

### Fallback Mechanism

If the tokenizer libraries encounter errors (such as initialization issues or compatibility problems), the tool automatically falls back to a simple regex-based token counting method. This ensures that the tool continues to function even when:

- The required libraries are not installed
- There are version compatibility issues
- Environment-specific configuration problems occur

When the fallback method is used, a warning message is displayed, but the tool continues to provide approximate token counts.

## Why Token Counting Matters

Accurate token counting is important for:

- Estimating API costs when using AI language models
- Ensuring your prompts fit within model context limits
- Optimizing prompt design for efficiency

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.