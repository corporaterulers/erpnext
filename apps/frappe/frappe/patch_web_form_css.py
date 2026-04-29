from pathlib import Path
import re
path = Path('apps/frappe/frappe/public/scss/website/web_form.scss')
text = path.read_text()
pattern = re.compile(r'(\s*border-bottom: 1px solid var\(--border-color\);\n)(\s*border-top: 1px solid var\(--border-color\);)')
new_text, count = pattern.subn(r'\1\t\t\t\t\tbackground-color: var(--bg-color);\n\2', text, count=1)
if count != 1:
    raise SystemExit(f'PATCH FAILED: found {count} occurrences')
path.write_text(new_text)
print('patched', count)
