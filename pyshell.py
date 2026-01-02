#version: 0.1.0
#functions
def print_custom(args):
    print(" ".join(args))
#parse
def parse_custom(value):
    value_str = value.strip("'").strip('"')
    value_low = value_str.lower()
    #bool
    if value == "true":
        return True
    if value == "false":
        return False
    #math
    try:
        return eval(value_str, {"__builtins__": None}, variables)
    except:
        pass
    return value
#other funcs. ignore my bad parse^
def exit(args):
    global running
    print("closing program...")
    running = False
def set(args):
    varname = args[0]
    value = parse_custom(" ".join(args[1:]))
    variables[varname] = value
    print("set ", varname, "as", variables[args[0]])
    print("current list: ", variables)
def printvar(args):
    #yes, print and printvar are different commands
    try:
        print(variables[args[0]])
    except:
        print("something went wrong")
def math(args):
    global mathmode
    if args[0].lower() == "on":
        mathmode = True
        print("set mathmode on")
    elif args[0].lower() == "off":
        mathmode = False
        print("set mathmode off")
    else:
        pass
def comment(args):
    #does nothing. basically useless
    pass

#new / file manager / because they deserve a space just for them
#"new" format: new <type> <name> <value> ?<extra3> ?<extra4>
def new(args):
    #small "lexer"
    TYPE = args[0]
    NAME = args[1]
    VALUE = args[2]
    try:
        EXTRA3 = args[3]
        EXTRA4 = args[4]
    except:
        pass
#if/elif/else because this was made in py 3.0, so i dont have match/case
    if TYPE.lower() == "var":
        nvar(NAME, VALUE)
    elif TYPE.lower() == "dict":
        ndict(NAME, VALUE, EXTRA3)
    elif TYPE.lower() == "array":
        narray(NAME, VALUE)
def nvar(NAME, VALUE):
    #ignore that ts is just set but slightly different
    variables[NAME] = VALUE
def ndict(NAME, VALUE, EXTRA3):
    #name: name of the dict
    #value: key
    #extra3: value
    enviroment[NAME] = {}
    enviroment[NAME][VALUE] = [EXTRA3]
    #WIP - working a bit
def narray(NAME, VALUE):
    #WIP - not working
    enviroment[NAME] = []
    enviroment[NAME].append(VALUE)
def cd():
    #WIP - not working
    pass
def look(args):
    #WIP - barely working
    try:
        print(eval(args[0], {"__builtins__": None}, **variables, **enviroment)) #idk if this eval is disarmed
    except:
        print("name error")
def delete():
    pass
    #WIP - not working

#data storage
keywords = {
"print": print_custom,
"exit": exit,
"set": set,
"printvar": printvar,
"math": math,
"new": new,
"look": look,
"//": comment
} #self explanatory
variables = {} #variable storage for teminal set
enviroment = {} #stores lists / possibly classes and objs in the future
running = True #triggers input loop
mathmode = False #math: on/off
#input loop
while running == True:
    command = input(">>> ")
    if not command.strip():
        #checks if the command is blank
        continue 
    if mathmode == False:
        #normal terminal pass
        commands = command.lower().split()
        if commands[0] in keywords:
            args = commands[1:]
            keywords[commands[0]](args)
        else:
            print("invalid command")
    else:
        #mathmode pass
        if not command == "math off":     
           print(eval(command, {"__builtins__": None}, variables))
           #BUGGED. fix soon. i dont even know what i did wrong
        else:
            mathmode = False
            print("set mathmode off")