class COLORS:
    ''' class which uses the colors: black,red,green,yellow,blue,magenta,cyan,white
    and bold versions of them
    and bold background versions of them
    and functions with all those combinations
    and print functions with all those combinations
    for better code completion than if it were defined dynamically using __getitem__ overloading
    '''
    BOLD_BLACK="\u001b[30;1m"
    BOLD_RED="\u001b[31;1m"
    BOLD_GREEN="\u001b[32;1m"
    BOLD_YELLOW="\u001b[33;1m"
    BOLD_BLUE="\u001b[34;1m"
    BOLD_MAGENTA="\u001b[35;1m"
    BOLD_CYAN="\u001b[36;1m"
    BOLD_WHITE="\u001b[37;1m"
    RESET="\u001b[0m"
    BACK_BLACK="\u001b[40m"
    BACK_RED="\u001b[41m"
    BACK_GREEN="\u001b[42m"
    BACK_YELLOW="\u001b[43m"
    BACK_BLUE="\u001b[44m"
    BACK_MAGENTA="\u001b[45m"
    BACK_CYAN="\u001b[46m"
    BACK_WHITE="\u001b[47m"
    BACK_BOLD_BLACK="\u001b[40;1m"
    BACK_BOLD_RED="\u001b[41;1m"
    BACK_BOLD_GREEN="\u001b[42;1m"
    BACK_BOLD_YELLOW="\u001b[43;1m"
    BACK_BOLD_BLUE="\u001b[44;1m"
    BACK_BOLD_MAGENTA="\u001b[45;1m"
    BACK_BOLD_CYAN="\u001b[46;1m"
    BACK_BOLD_WHITE="\u001b[47;1m"
    BOLD="\u001b[1m"
    UNDERLINE="\u001b[4m"
    REVERSED="\u001b[7m"

    # functions
    @classmethod
    def bold_black(cls,str_):
        return cls.BOLD_BLACK + str(str_) + cls.RESET
    @classmethod
    def bold_red(cls,str_):
        return cls.BOLD_RED + str(str_) + cls.RESET
    @classmethod
    def bold_green(cls,str_):
        return cls.BOLD_GREEN + str(str_) + cls.RESET
    @classmethod
    def bold_yellow(cls,str_):
        return cls.BOLD_YELLOW + str(str_) + cls.RESET
    @classmethod
    def bold_blue(cls,str_):
        return cls.BOLD_BLUE + str(str_) + cls.RESET
    @classmethod
    def bold_magenta(cls,str_):
        return cls.BOLD_MAGENTA + str(str_) + cls.RESET
    @classmethod
    def bold_cyan(cls,str_):
        return cls.BOLD_CYAN + str(str_) + cls.RESET
    @classmethod
    def bold_white(cls,str_):
        return cls.BOLD_WHITE + str(str_) + cls.RESET
    @classmethod
    def reset(cls,str_):
        return cls.RESET + str(str_) + cls.RESET
    @classmethod
    def back_black(cls,str_):
        return cls.BACK_BLACK + str(str_) + cls.RESET
    @classmethod
    def back_red(cls,str_):
        return cls.BACK_RED + str(str_) + cls.RESET
    @classmethod
    def back_green(cls,str_):
        return cls.BACK_GREEN + str(str_) + cls.RESET
    @classmethod
    def back_yellow(cls,str_):
        return cls.BACK_YELLOW + str(str_) + cls.RESET
    @classmethod
    def back_blue(cls,str_):
        return cls.BACK_BLUE + str(str_) + cls.RESET
    @classmethod
    def back_magenta(cls,str_):
        return cls.BACK_MAGENTA + str(str_) + cls.RESET
    @classmethod
    def back_cyan(cls,str_):
        return cls.BACK_CYAN + str(str_) + cls.RESET
    @classmethod
    def back_white(cls,str_):
        return cls.BACK_WHITE + str(str_) + cls.RESET
    @classmethod
    def back_bold_black(cls,str_):
        return cls.BACK_BOLD_BLACK + str(str_) + cls.RESET
    @classmethod
    def back_bold_red(cls,str_):
        return cls.BACK_BOLD_RED + str(str_) + cls.RESET
    @classmethod
    def back_bold_green(cls,str_):
        return cls.BACK_BOLD_GREEN + str(str_) + cls.RESET
    @classmethod
    def back_bold_yellow(cls,str_):
        return cls.BACK_BOLD_YELLOW + str(str_) + cls.RESET
    @classmethod
    def back_bold_blue(cls,str_):
        return cls.BACK_BOLD_BLUE + str(str_) + cls.RESET
    @classmethod
    def back_bold_magenta(cls,str_):
        return cls.BACK_BOLD_MAGENTA + str(str_) + cls.RESET
    @classmethod
    def back_bold_cyan(cls,str_):
        return cls.BACK_BOLD_CYAN + str(str_) + cls.RESET
    @classmethod
    def back_bold_white(cls,str_):
        return cls.BACK_BOLD_WHITE + str(str_) + cls.RESET
    @classmethod
    def bold(cls,str_):
        return cls.BOLD + str(str_) + cls.RESET
    @classmethod
    def underline(cls,str_):
        return cls.UNDERLINE + str(str_) + cls.RESET
    @classmethod
    def reversed(cls,str_):
        return cls.REVERSED + str(str_) + cls.RESET

    #print functions
    @classmethod
    def print_bold_black(cls,str_):
        print(cls.BOLD_BLACK + str(str_) + cls.RESET)
    @classmethod
    def print_bold_red(cls,str_):
        print(cls.BOLD_RED + str(str_) + cls.RESET)
    @classmethod
    def print_bold_green(cls,str_):
        print(cls.BOLD_GREEN + str(str_) + cls.RESET)
    @classmethod
    def print_bold_yellow(cls,str_):
        print(cls.BOLD_YELLOW + str(str_) + cls.RESET)
    @classmethod
    def print_bold_blue(cls,str_):
        print(cls.BOLD_BLUE + str(str_) + cls.RESET)
    @classmethod
    def print_bold_magenta(cls,str_):
        print(cls.BOLD_MAGENTA + str(str_) + cls.RESET)
    @classmethod
    def print_bold_cyan(cls,str_):
        print(cls.BOLD_CYAN + str(str_) + cls.RESET)
    @classmethod
    def print_bold_white(cls,str_):
        print(cls.BOLD_WHITE + str(str_) + cls.RESET)
    @classmethod
    def print_reset(cls,str_):
        print(cls.RESET + str(str_) + cls.RESET)
    @classmethod
    def print_back_black(cls,str_):
        print(cls.BACK_BLACK + str(str_) + cls.RESET)
    @classmethod
    def print_back_red(cls,str_):
        print(cls.BACK_RED + str(str_) + cls.RESET)
    @classmethod
    def print_back_green(cls,str_):
        print(cls.BACK_GREEN + str(str_) + cls.RESET)
    @classmethod
    def print_back_yellow(cls,str_):
        print(cls.BACK_YELLOW + str(str_) + cls.RESET)
    @classmethod
    def print_back_blue(cls,str_):
        print(cls.BACK_BLUE + str(str_) + cls.RESET)
    @classmethod
    def print_back_magenta(cls,str_):
        print(cls.BACK_MAGENTA + str(str_) + cls.RESET)
    @classmethod
    def print_back_cyan(cls,str_):
        print(cls.BACK_CYAN + str(str_) + cls.RESET)
    @classmethod
    def print_back_white(cls,str_):
        print(cls.BACK_WHITE + str(str_) + cls.RESET)
    @classmethod
    def print_back_bold_black(cls,str_):
        print(cls.BACK_BOLD_BLACK + str(str_) + cls.RESET)
    @classmethod
    def print_back_bold_red(cls,str_):
        print(cls.BACK_BOLD_RED + str(str_) + cls.RESET)
    @classmethod
    def print_back_bold_green(cls,str_):
        print(cls.BACK_BOLD_GREEN + str(str_) + cls.RESET)
    @classmethod
    def print_back_bold_yellow(cls,str_):
        print(cls.BACK_BOLD_YELLOW + str(str_) + cls.RESET)
    @classmethod
    def print_back_bold_blue(cls,str_):
        print(cls.BACK_BOLD_BLUE + str(str_) + cls.RESET)
    @classmethod
    def print_back_bold_magenta(cls,str_):
        print(cls.BACK_BOLD_MAGENTA + str(str_) + cls.RESET)
    @classmethod
    def print_back_bold_cyan(cls,str_):
        print(cls.BACK_BOLD_CYAN + str(str_) + cls.RESET)
    @classmethod
    def print_back_bold_white(cls,str_):
        print(cls.BACK_BOLD_WHITE + str(str_) + cls.RESET)
    @classmethod
    def print_bold(cls,str_):
        print(cls.BOLD + str(str_) + cls.RESET)
    @classmethod
    def print_underline(cls,str_):
        print(cls.UNDERLINE + str(str_) + cls.RESET)
    @classmethod
    def print_reversed(cls,str_):
        print(cls.REVERSED + str(str_) + cls.RESET)

