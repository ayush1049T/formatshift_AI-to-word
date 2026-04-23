import os

for filename in os.listdir('.'):
    if 'todo' in filename.lower():
        print(f"Found {filename}")

try:
    with open('formatshift/lint_errors.txt', 'r', encoding='utf-16le') as f:
        content = f.read()
    with open('todo_list.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully converted formatshift/lint_errors.txt to todo_list.txt (UTF-8)")
except Exception as e:
    print("Error:", e)
