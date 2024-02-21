#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import sys
import os
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    try:
        with open(markdown_file, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()

        html_content = markdown.markdown(md_content)

        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        return 0

    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    exit_code = convert_markdown_to_html(markdown_file, output_file)
    sys.exit(exit_code)
