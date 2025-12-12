### 11th december 2025: setting up vscode for dsa and cp

i simply checked if c++ was installed on my system (macos) using the command:

```
clang --version
```

and got this as output:

```
apple clang version 13.1.6 (clang-1316.0.21.2.5)
target: arm64-apple-darwin25.0.0
thread model: posix
installeddir: /applications/xcode.app/contents/developer/toolchains/xcodedefault.xctoolchain/usr/bin
```

so yeah it was installed already, so i headed towards vscode and installed the c++ extension pack.

then i wanted to setup my vscode like he showed in the video of setting vscode for dsa and cp, like code editor on left, and top right: input, and on bottom right: output. so i did that setup by following his instructions in the video and here's how my screen looks like:

![vscode setup](images/vscode-setup.png)

here's the `.vscode/tasks.json` code if you need:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "compile",
            "type": "shell",
            "command": "g++",
            "args": [
                "-std=c++17",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}",
                "${file}"
            ],
            "presentation": {
                "echo": false,
                "reveal": "never",
                "focus": false,
                "panel": "dedicated"
            },
            "group": {
                "kind": "build",
                "isDefault": false
            }
        },
        {
            "label": "compile and run",
            "type": "shell",
            "command": "g++ -std=c++17 -o ${fileDirname}/${fileBasenameNoExtension} ${file} && ${fileDirname}/${fileBasenameNoExtension} < ${workspaceFolder}/input.txt > ${workspaceFolder}/output.txt",
            "presentation": {
                "echo": false,
                "reveal": "never",
                "focus": false,
                "panel": "dedicated"
            },
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```

i modified it a bit according to my folder structure.

so yeah then i wrote the code as he showed, and ran using `cmd + shift + b` (macos) and it worked.

see you tomorrow!
