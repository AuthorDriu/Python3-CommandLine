class Command:
    def __init__(self, function, help=""):
        self.__func = function
        self.__help = help
    
    def __call__(self):
        self.__func()
    
    def __repr__(self):
        return self.__help

class CommandLine:
    def __init__(self, prefix=">>> "):
        self.prefix = prefix
        self.__command_dict = {"помощь!": Command(self.print_help, "Показать это сообщение"),
                               "выход!": Command(self.exit, "Выйти из терминала")}

    def add(self, command, function, help=""):
        self.__command_dict[command.lower()] = Command(function, help)
    
    def print_help(self):
        print("==============")
        print("Помощь:\n")
        for command_name in self.__command_dict.keys():
            print(f"[{command_name}]\n{self.__command_dict[command_name]}")
            print("\n")
        print("==============")
    
    def exit(self):
        print("Выход из терминала...")
        self.is_running = False

    def run(self):
        self.is_running = True
        try:
            while self.is_running:
                command = input(self.prefix)
                command_to_exec = self.__command_dict.get(command, None)
                if command_to_exec is None:
                    print(f"Команды {command} не существует!")
                    continue
                command_to_exec()
        except KeyboardInterrupt:
            print("Выход из терминала...")