from CommandLine import CommandLine

def Command1():
    print("Команда 1 выполнена")

def Command2():
    print("Команда 2 выполнена")

command_line = CommandLine()
command_line.add("Command1", Command1, "Выполнить команду 1")
command_line.add("Command2", Command2, "Выполнить команду 2")
command_line.run()
