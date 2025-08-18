#!/usr/bin/env python3
"""
🦄 Unicorn - A magical utility that brings sparkle to your day!
"""

import random
import sys

# ANSI color codes for colorful output
COLORS = {
    'pink': '\033[95m',
    'blue': '\033[94m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'purple': '\033[35m',
    'white': '\033[97m',
    'reset': '\033[0m',
    'bold': '\033[1m'
}

def colorize(text, color):
    """Add color to text output."""
    return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"

def print_unicorn_art():
    """Print beautiful ASCII unicorn art."""
    unicorn = [
        "                 /|   /|  ",
        "               _/_|__/ | ",
        "              /       |  ",
        "             /         | ",
        "            | \\     /  |",
        "            |  \\_.-;   |",
        "           /   _.-|    |",
        "          ;   /   |    |",
        "          |  |    \\    |",
        "          |  |     |   |",
        "          |  |     |   |",
        "           \\ |     |  /",
        "            \\|     | /",
        "             \\     |/",
        "              |_____|",
        "              |     |",
        "              |     |",
        "             /|     |\\",
        "            / |     | \\",
        "           |  |     |  |",
        "          |___|_____|___|"
    ]
    
    # Print unicorn with random colors
    colors = ['pink', 'cyan', 'purple', 'white']
    for line in unicorn:
        color = random.choice(colors)
        print(colorize(line, color))

def get_magical_message():
    """Return a random inspirational unicorn message."""
    messages = [
        "✨ Believe in magic, and magic will believe in you! ✨",
        "🌟 You are as unique and magical as a unicorn! 🌟",
        "💫 Sprinkle kindness wherever you go! 💫",
        "🦄 Today is a perfect day to be awesome! 🦄",
        "⭐ Your dreams are valid and magical! ⭐",
        "🌈 Be a rainbow in someone's cloud! 🌈",
        "✨ Magic happens when you believe in yourself! ✨",
        "🦄 You have the power to make today amazing! 🦄",
        "💖 Sparkle with positivity and light! 💖",
        "🌟 Be the unicorn you want to see in the world! 🌟"
    ]
    return random.choice(messages)

def main():
    """Main function to run the unicorn program."""
    print(colorize("\n🦄 Welcome to the Magical Unicorn Experience! 🦄\n", 'bold'))
    
    # Print unicorn art
    print_unicorn_art()
    
    # Print magical message
    print(f"\n{colorize(get_magical_message(), 'pink')}\n")
    
    # Add some sparkles
    sparkles = "✨ " * 20
    print(colorize(sparkles, 'yellow'))
    
    print(colorize("\nMay your day be filled with magic and wonder! 🌈✨", 'cyan'))

if __name__ == "__main__":
    main()