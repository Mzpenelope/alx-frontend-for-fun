#!/usr/bin/python3

"""
Markdown script using python.
"""
import sys
import os.path
import re
import hashlib

def convert_markdown_to_html(markdown_file, html_file):
    with open(markdown_file) as read:
        with open(html_file, 'w') as html:
            unordered_start, ordered_start, paragraph = False, False, False
            # special syntax patterns
            for line in read:
                line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
                line = re.sub(r'__(.+?)__', r'<em>\1</em>', line)

                # md5
                md5 = re.findall(r'\[\[(.+?)\]\]', line)
                if md5:
                    line = re.sub(r'\[\[(.+?)\]\]', lambda match: hashlib.md5(match.group(1).encode()).hexdigest(), line)

                # remove the letter C
                remove_c = re.findall(r'\(\((.+?)\)\)', line)
                if remove_c:
                    line = re.sub(r'\(\((.+?)\)\)', lambda match: match.group(1).replace('C', '').replace('c', ''), line)

                length = len(line)
                headings = line.lstrip('#')
                heading_num = length - len(headings)
                unordered = line.lstrip('-')
                unordered_num = length - len(unordered)
                ordered = line.lstrip('*')
                ordered_num = length - len(ordered)

                # headings, lists
                if 1 <= heading_num <= 6:
                    line = '<h{}>{}</h{}>\n'.format(
                        heading_num, headings.strip(), heading_num)
                elif line.startswith('#'):
                    # Handle the case where there's no space after the '#' symbol
                    line = '<h1>{}</h1>\n'.format(line.lstrip('#').strip())

                # unordered listing
                if unordered_num:
                    if not unordered_start:
                        html.write('<ul>\n')
                        unordered_start = True
                    line = '<li>' + unordered.strip() + '</li>\n'
                else:
                    if unordered_start:
                        html.write('</ul>\n')
                        unordered_start = False

                if ordered_num:
                    if not ordered_start:
                        html.write('<ol>\n')
                        ordered_start = True
                    line = '<li>' + ordered.strip() + '</li>\n'
                if ordered_start and not ordered_num:
                    html.write('</ol>\n')
                    ordered_start = False

                # paragraphs
                if length > 1:
                    if not (heading_num or unordered_start or ordered_start):
                        if not paragraph:
                            html.write('<p>\n')
                            paragraph = True
                        html.write(line)
                elif paragraph:
                    html.write('</p>\n')
                    paragraph = False

            if unordered_start:
                html.write('</ul>\n')
            if ordered_start:
                html.write('</ol>\n')
            if paragraph:
                html.write('</p>\n')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    convert_markdown_to_html(sys.argv[1], sys.argv[2])
    exit(0)
