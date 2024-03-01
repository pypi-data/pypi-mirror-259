import random, codecs, os, sys
try:
    import disnake

    def is_online(guild: disnake.Guild, user_id) -> bool:
        """
        returns True if member is not offline (online, idle, etc.)
        else returns False

        also returns False if member was not found on guild
        """
        member = guild.get_member(user_id)

        memberOnline = False

        if member:
            memberOnline = (member.status != disnake.Status.offline)
        return memberOnline

except ModuleNotFoundError:
    pass

def smthfile(fp, readingmode):
    """
    returns file with utf-8 encoding and uses write mode you want to use
    """
    return codecs.open(fp, readingmode, encoding="utf-8")

def openfile(fp):
    """
    returns file with utf-8 encoding
    """
    return smthfile(fp, "r")

def editfile(fp):
    """
    returns file with utf-8 encoding and uses write mode
    """
    return smthfile(fp, "w")

def get_folder_path(caller, *args, create_folders=True):
    """
    returns folder that is in same folder as caller
    for example if your caller is "D:/kreisi program/main.py"
    get_folder_path(__file__, "folder 1", "folder 2") will return
    "D:/kreisi program/folder 1/folder 2"
    if any folder doesn't exist it will be created
    do get_folder_path(..., create_folders=False) if you won't
    """
    args = [str(a) for a in args]
    folder_dir = os.path.dirname(caller)

    for f in args:
        folder_dir = os.path.join(folder_dir, f)
        if create_folders and not os.path.exists(folder_dir):
            os.makedirs(folder_dir)
    return folder_dir

def get_file_path(caller, *args, create_folders=True, create_file=True):
    """
    returns "folder where caller is"/args/filename"
    for example if caller is "D:/kreisi program/main.py"
    get_file_path("folder", "opinion on mars.txt") will return
    "D:/kreisi program/folder/opinion on mars.txt"

    if file or folder doesn't exist it will be created
    do get_folder_path(folder, filename, create_file=False) (same
    with create_folders) if you won't

    if you will replace create_file with any string this value will
    be wrote to file if it doesn't exist
    """
    args = [str(a) for a in args]
    folder_dir = get_folder_path(caller, *args[:-1], create_folders=create_folders)

    filepath = os.path.join(folder_dir, args[-1])
    if create_file!=False and not os.path.exists(filepath):
        with open(filepath, "w") as f:
            if type(create_file)!=str: pass
            else: f.write(create_file)

    return filepath

def add_line(fp, line):
    """
    adds line to the of the file
    for example if file already has 2 strings
    add_line("opinion on mars.txt", "MARS IS A STUPID PLANET!!!!!!")
    will do

    already existsing string in file 1
    already existsing string in file 2
    MARS IS A STUPID PLANET!!!!!!
    """
    with smthfile(fp, "a+") as file:
        file.seek(0)
        if file.read():
            file.seek(0, 2)
            file.write("\n")
        file.write(line)

def remove_line(fp, line):
    """
    removes line to the of the file
    for example if file is from previous example
    remove_line("opinion on mars.txt", "already existsing string in file 1")
    will do

    already existsing string in file 2
    MARS IS A STUPID PLANET!!!!!!
    """
    typingemoji=""
    for every in openfile(fp).read().split("\n"):
        if every != line:
            typingemoji+=f"{every}\n"
    editfile(fp).write(typingemoji[:-1])

def listpaths(fp):
    """
    lists paths of files in folder

    >>> import temalib
    >>> temalib.listpaths("C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter")
    ['C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\achs', ..., 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\main.py', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\pi.txt', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\ropl.dat', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\SAVE SPLASHSES.py', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\save_file_trusteds.txt', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\scrl', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\shitpost', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\splashes.dat', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\splashesinfo.dat', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\splashes_channels.txt', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\src', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\temp', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\TOKEN.txt', 'C:\\Users\\User\\Documents\\folder without name\\python\\discord bots\\ammeter\\__pycache__']
    """
    return [os.path.join(fp, i) for i in os.listdir(fp)]

def generate_ip(name):
    random.seed(name)
    return ".".join([str(random.randint(0,255)) for _ in range(4)])