import re
import os

authors = {}

pattern = re.compile('Created by (\w*) on')
max_lines = 10

def read_files(path):
    for f in os.listdir(path):
        if f.startswith('.'):
            continue
        if os.path.isdir(os.path.join(path, f)):
            read_files(os.path.join(path, f))
        else:
            basename = os.path.basename(f)
            components = basename.split('.')
            if len(components) > 1 and \
            (components[-1] == 'm' or
             components[-1] == 'h' or
             components[-1] == 'mm' or
             components[-1] == 'swift'):
                count_authors(os.path.join(path, f))

def count_authors(source_file):
    with open(source_file) as f:
        for i, line in enumerate(f):
            match = pattern.search(line)
            if match:
                name = match.group(1)
                if authors.get(name):
                    authors[name] += 1
                else:
                    authors[name] = 1
                break
            if i == 10:
                break

if __name__ == '__main__':
    read_files('.')
    file_count = []
    for item in authors:
        file_count.append((item, authors[item]))
        sorted_count = sorted(file_count, key=lambda x: x[1], reverse=True)
    total = 0
    for item in sorted_count:
        total += item[1]
        print('{0:4}  {1:15}'.format(item[1], item[0]))
    print('{0:4}: TOTAL'.format(total))


