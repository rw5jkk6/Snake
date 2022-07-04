- ショートキー(task.json)の実行に使う
```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "game run",
            "type": "shell",
            "command": "python3",
            "args": [
                "main.py"
            ],
        }
    ]
}
```
- ユーザースニペット(python.json)に使う
```json
{
	// Place your snippets for python here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"Print to console": {
		"prefix": "pygmain",
		"body": [
			"import pygame",
			"from pygame.locals import QUIT",
			"import sys",
			"",
			"pygame.init()",
			"SURFACE = pygame.display.set_mode((600, 600))",
			"FPSCLOCK = pygame.time.Clock()",
			"",
			"",
			"def paint():",
			"    SURFACE.fill((0,0,0))",
			"    pygame.display.update()",
			"",
			"def main():",
            "    while True:",
            "        for event in pygame.event.get():",
            "            if event.type == QUIT:",
			"                pygame.quit()",
            "                sys.exit()",
            "        paint()",
            "        FPSCLOCK.tick(5)",

            "if __name__ == '__main__':",
    		"    main()"
		]
	}
}
```
