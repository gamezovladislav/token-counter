#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Token Counter - Simple utility for counting tokens in text files for AI models.
Uses tiktoken library for OpenAI models and anthropic library for Anthropic models.
Supports processing individual files or entire directories.

Usage:
    python count_tokens.py <file_or_directory_path> [--model MODEL]

Parameters:
    --model, -m    AI model for token counting (default: from .env or claude-3-7-sonnet-latest)

Configuration:
    The application can be configured using a .env file with the following variables:
    - OPENAI_MODELS: Comma-separated list of available OpenAI models
    - ANTHROPIC_MODELS: Comma-separated list of available Anthropic models
    - DEFAULT_MODEL: Default model to use when not specified
    - IGNORE_DIRS: Comma-separated list of directories to ignore
    - IGNORE_EXTENSIONS: Comma-separated list of file extensions to ignore
"""

import argparse
import os
import re
import sys
from typing import Tuple, Set

import anthropic
import tiktoken
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ANSI colors for output
COLORS = {
    'blue': '\033[94m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'bold': '\033[1m',
    'end': '\033[0m'
}

# Common text file extensions
TEXT_EXTENSIONS = {
    '.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.xml', '.yaml', '.yml'
}

# Helper function to parse comma-separated environment variables into sets
def parse_env_list(env_var: str, default_set: Set[str]) -> Set[str]:
    """Parse a comma-separated environment variable into a set of strings."""
    value = os.environ.get(env_var)
    if not value:
        return default_set
    return {item.strip() for item in value.split(',')}

# Default values
DEFAULT_IGNORE_EXTENSIONS = {
    '.jpg', '.jpeg', '.png', '.gif', '.exe', '.dll', '.pyc', '.pyo'
}

DEFAULT_IGNORE_DIRS = {
    '.git', '.idea', '.vscode', '__pycache__', 'venv', 'node_modules', '.venv'
}

DEFAULT_OPENAI_MODELS = {
    "o1",
    "o3",
    "o4-mini",
    "gpt-4.1",
    "gpt-4o",
    "gpt-4"
}

DEFAULT_ANTHROPIC_MODELS = {
    "claude-3-7-sonnet-latest",
    "claude-3-7-sonnet-20250219",
    "claude-3-5-haiku-latest",
    "claude-3-5-haiku-20241022",
    "claude-sonnet-4-20250514",
    "claude-sonnet-4-0",
    "claude-4-sonnet-20250514",
    "claude-3-5-sonnet-latest",
    "claude-3-5-sonnet-20241022",
    "claude-3-5-sonnet-20240620",
    "claude-opus-4-0",
    "claude-opus-4-20250514",
    "claude-4-opus-20250514",
    "claude-opus-4-1-20250805",
    "claude-3-opus-latest",
    "claude-3-opus-20240229",
    "claude-3-haiku-20240307"
}

# Load configuration from environment variables
IGNORE_EXTENSIONS = parse_env_list('IGNORE_EXTENSIONS', DEFAULT_IGNORE_EXTENSIONS)
IGNORE_DIRS = parse_env_list('IGNORE_DIRS', DEFAULT_IGNORE_DIRS)
OPENAI_MODELS = parse_env_list('OPENAI_MODELS', DEFAULT_OPENAI_MODELS)
ANTHROPIC_MODELS = parse_env_list('ANTHROPIC_MODELS', DEFAULT_ANTHROPIC_MODELS)

# Set default model
DEFAULT_MODEL = os.environ.get('DEFAULT_MODEL', 'claude-3-7-sonnet-latest')

# Combine all models
ALL_MODELS = OPENAI_MODELS.union(ANTHROPIC_MODELS)


def colorize(text: str, color: str) -> str:
    """Adds color formatting to text."""
    return f"{COLORS.get(color, '')}{text}{COLORS['end']}"

def is_binary_file(file_path: str) -> bool:
    """Checks if a file is binary."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.read(1024)
        return False
    except UnicodeDecodeError:
        return True


def count_tokens_in_text(text: str, model: str) -> int:
    """
    Counts the exact number of tokens in text using the appropriate tokenizer.
    
    Args:
        text: Text to count tokens in
        model: AI model for token counting
        
    Returns:
        int: Number of tokens, or 0 if an error occurs
    """
    try:
        if model in OPENAI_MODELS:
            # Use tiktoken for OpenAI models
            enc = tiktoken.encoding_for_model(model)
            tokens = enc.encode(text)
            return len(tokens)

        if model in ANTHROPIC_MODELS:
            # Use anthropic for Anthropic models
            try:
                # Create client and use messages.count_tokens method with correct format
                client = anthropic.Anthropic()
                # Use the provided model or fallback to a default Claude model
                response = client.messages.count_tokens(
                    messages=[{"role": "user", "content": text}],
                    model=model
                )
                return response.token_count
            except Exception as e:
                # If there's an error with the token counting, use fallback method
                print(colorize(f"Warning: Using fallback token counting method for Anthropic: {str(e)}", "yellow"))
                # Fallback method
                tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
                return 0

        # If model is not recognized, show error
        raise ValueError(f"Unknown model: {model}. Please use a supported model.")
    except Exception as e:
        print(colorize(f"Error counting tokens: {str(e)}", "red"))
        # Fallback method if there's an error
        tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
        return 0

def process_file(file_path: str, model: str) -> Tuple[int, int]:
    """
    Processes a single file and returns token and character counts.
    
    Args:
        file_path: Path to the file
        model: AI model for token counting
        
    Returns:
        Tuple[int, int]: (token_count, character_count)
    """
    # Check if file exists
    if not os.path.isfile(file_path):
        print(colorize(f"Error: File not found: {file_path}", "red"))
        return 0, 0
    
    # Check file extension
    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext in IGNORE_EXTENSIONS:
        return 0, 0
    
    # Check if a file is a text
    if file_ext not in TEXT_EXTENSIONS and is_binary_file(file_path):
        return 0, 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        char_count = len(content)
        token_count = count_tokens_in_text(content, model)
        
        print(f"File: {colorize(file_path, 'blue')}")
        print(f"  Characters: {colorize(str(char_count), 'green')}")
        print(f"  Tokens: {colorize(str(token_count), 'yellow')}")
        
        return token_count, char_count
    
    except Exception as e:
        print(colorize(f"Error processing file {file_path}: {str(e)}", "red"))
        return 0, 0


def process_directory(dir_path: str, model: str) -> Tuple[int, int, int]:
    """
    Recursively processes all files in a directory.
    
    Args:
        dir_path: Path to the directory
        model: AI model for token counting
        
    Returns:
        Tuple[int, int, int]: (total_token_count, total_character_count, file_count)
    """
    total_tokens = 0
    total_chars = 0
    file_count = 0
    
    # Check if a directory exists
    if not os.path.isdir(dir_path):
        print(colorize(f"Error: Directory not found: {dir_path}", "red"))
        return total_tokens, total_chars, file_count
    
    print(colorize(f"\nProcessing directory: {dir_path}", "bold"))
    print(colorize(f"Using model: {model}", "blue"))
    
    for root, dirs, files in os.walk(dir_path):
        # Exclude ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            file_path = os.path.join(root, file)
            tokens, chars = process_file(file_path, model)
            
            if tokens > 0 or chars > 0:
                total_tokens += tokens
                total_chars += chars
                file_count += 1
    
    return total_tokens, total_chars, file_count


def format_number(num: int) -> str:
    """Formats a number with a thousand separators."""
    return f"{num:,}".replace(',', ' ')


def main():
    parser = argparse.ArgumentParser(
        description='Count tokens in text files for AI models'
    )
    parser.add_argument(
        'path', 
        help='Path to file or directory to analyze'
    )
    parser.add_argument(
        '--model', '-m',
        default=DEFAULT_MODEL,
        choices=list(ALL_MODELS),
        required=False,
        help=f'AI model for token counting (default: {DEFAULT_MODEL})'
    )
    args = parser.parse_args()
    path = args.path
    model = args.model
    
    print(colorize("=" * 60, "blue"))
    print(colorize("  TOKEN COUNTER", "bold"))
    print(colorize(f"  Model: {model}", "bold"))
    print(colorize("=" * 60, "blue"))
    
    if os.path.isfile(path):
        tokens, chars = process_file(path, model)
        
        print(colorize("\nSummary:", "bold"))
        print(f"Characters: {colorize(format_number(chars), 'green')}")
        print(f"Tokens: {colorize(format_number(tokens), 'yellow')}")
        
    elif os.path.isdir(path):
        total_tokens, total_chars, file_count = process_directory(path, model)
        
        print(colorize("\nSummary:", "bold"))
        print(f"Files processed: {colorize(str(file_count), 'blue')}")
        print(f"Total characters: {colorize(format_number(total_chars), 'green')}")
        print(f"Total tokens: {colorize(format_number(total_tokens), 'yellow')}")
        
    else:
        print(colorize(f"Error: Path does not exist: {path}", "red"))
        sys.exit(1)
    
    print(colorize("=" * 60, "blue"))


if __name__ == "__main__":
    main()