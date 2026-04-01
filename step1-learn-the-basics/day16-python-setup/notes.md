### 1st april 2026: setting up vscode for python dsa and cp

switching from c++ to python, so had to set up the same input/output workflow i had before.

first i checked if python was installed on my system (windows) using:

```
python --version
```

and got:

```
Python 3.10.7
```

so yeah it was already installed. no extension needed since python runs directly without compiling.

then i set up `.vscode/tasks.json` to pipe `input.txt` into the python file, same idea as the c++ setup but simpler since there's no compile step:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Python with input.txt",
      "type": "shell",
      "command": "python \"${file}\" < \"${workspaceFolder}/input.txt\" > \"${workspaceFolder}/output.txt\"",
      "options": {
        "shell": {
          "executable": "cmd.exe",
          "args": ["/d", "/c"]
        }
      },
      "presentation": {
        "reveal": "always",
        "focus": true,
        "panel": "shared",
        "clear": true
      },
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

the `input.txt` sits at the workspace root, same as before. i just put my test cases there and hit `ctrl + shift + b` to run. output goes into `output.txt` at the workspace root — same layout as the c++ setup.

for the python code itself, i use `sys.stdin.readline` instead of the default `input()` because it's faster for large inputs:

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    print(n)

t = int(input())
for _ in range(t):
    solve()
```

the first line of `input.txt` is always `t` (number of test cases), then each test case follows — same pattern as competitive programming problems.
