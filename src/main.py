from os import listdir, mkdir, rmdir
from os.path import isfile, join, isdir

path = "/"

while True:
    args = input().split(" ")
    cmd = args[0]

    if cmd == "pwd":
        print(path)

    elif cmd == "ls":
        file_names = [f for f in listdir(path)]
        print(*file_names, sep="\n")

    # mkdir file.txt zaza. args[1] = file.txt#

    elif cmd == "mkdir":
        file_names = [f for f in listdir(path)]
        if args[1] in file_names:
            print("file already exists")
        else:
            mkdir(path + "/" + args[1])

    elif cmd == "rmdir":
        # Here we need to get ONLY directories and not every possible file:
        dir_names = [f for f in listdir(path) if filter(isdir, f)]
        if args[1] in dir_names:
            if len(listdir(path + "/" + args[1])) == 0:
                rmdir(path + "/" + args[1])

        else:
            print("no such directory")

    elif cmd == "cd":
        # here we get the parts of path to which we want to cd.
        path_parts = args[1].split('/')

        # /cores -> ["", "cores"]

        if path_parts[-1] == '':
            path_parts.pop()

        # Here the user asked for the absolute path:
        if path_parts[0] == '':
            path = "/"
            path_parts.pop(0)

        for path_part in path_parts:
            # Here we need to get ONLY directories and not every possible file:
            dir_names = [f for f in listdir(path) if filter(isdir, f)]

            if path_part == '.':
                continue

            elif path_part == '..':
                current_path_parts = path.split('/')
                current_path_parts.pop()
                path = '/'.join(current_path_parts)

                if path == '':
                    path = '/'

            elif path_part in dir_names:
                if path != '/':
                    path += '/'
                path += path_part

            else:
                print("No such directory")
