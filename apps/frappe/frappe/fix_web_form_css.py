from pathlib import Path

path = Path('apps/frappe/frappe/public/scss/website/web_form.scss')
lines = path.read_text().splitlines(True)
modified = False
for i, line in enumerate(lines):
    if 'tbody tr:nth-child(odd)' in line:
        lines[i] = '\t\t\t\t\t\tbody tr:nth-child(odd) {\n'
        modified = True
    elif 'tbody tr:hover' in line:
        lines[i] = '\t\t\t\t\t\tbody tr:hover {\n'
        modified = True
    elif 'input[type="checkbox"] {' in line and 'margin-top' in lines[i+1] if i + 1 < len(lines) else False:
        lines[i] = '\t\t\t\t\t\tinput[type="checkbox"] {\n'
        modified = True
    elif 'margin-top: 2px;' in line and 'input[type="checkbox"]' not in lines[i-1]:
        lines[i] = '\t\t\t\t\t\t\tmargin-top: 2px;\n'
        modified = True

if modified:
    path.write_text(''.join(lines))
    print('patched indent fixes')
else:
    print('no changes applied')
