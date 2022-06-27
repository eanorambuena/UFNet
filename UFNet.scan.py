import os
from colorama import Fore, Style, init

def track(PATH):
    PATH_INTERN = PATH + "/UFNet"
    templates_number = 5

    tmp = [""]

    for i in range(1, templates_number + 1):
        with open(f'{PATH_INTERN}/templates/{i}.html', 'r') as f:
            tmp.append(f.read())

    def scan(path, depth=0):
        """
        Scan a folder and update the files folder.
        """
        arrow = '    ' * depth + ('├─ ') * (depth > 0)
        init()
        obj = os.scandir(path)

        if depth == 0:
            print(Style.BRIGHT + Fore.YELLOW + "Files and Directories in '% s':" % path)

        list = []

        for entry in obj :
            if entry.is_dir() and entry.name not in ['__pycache__', 'UFNet']:
                print(Style.BRIGHT + arrow + Fore.GREEN + entry.name)
                with open(entry.path.replace('\\','/') + ".folder.hyperlink", "w") as f:
                    pass
                scan(entry.path, depth + 1)
            elif entry.is_file() and entry.name not in ['UFNet.scan.py', 'UFNet.index.html']:
                print(Style.BRIGHT + Fore.WHITE + arrow + entry.name)
                list.append(f"                    addFile('{entry.name}');")
                
        content = tmp[1] + PATH_INTERN + tmp[2] + PATH_INTERN + tmp[3] + path.replace('\\','/') + tmp[4] + "\n".join(list) + tmp[5]

        with open(f'{path}/UFNet.index.html', 'w', encoding="utf-8") as f:
            f.write(content)
        
        # https://www.flaticon.com/packs/file-types-10?word=file%20extension&style_id=171&family_id=60&group_id=247

    scan(PATH)

track("C:/Users/yasna/OneDrive/Escritorio/¡Aportes!")
