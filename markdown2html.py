#!/usr/bin/python3
"""
markdown2html - Convert Markdown to HTML

Usage:
  ./markdown2html.py <input_file> <output_file>
"""

import sys
import os
import markdown2

def convert_markdown_to_html(input_file, output_file):
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Check if the Markdown file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown content from the file
    with open(input_file, 'r') as md_file:
        markdown_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown2.markdown(markdown_content)

    # Write the HTML content to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    # Extract input and output file names from command line arguments
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
