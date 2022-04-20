from pyglet.app import run
from code.screen import GameScreen
from sys import argv

def usage() -> None:
    print("Usage: python3 py_of_life.py [OPTIONS]")
    print("Options:")
    print("    -h, --help:                 Prints this help message")
    print("    -s, --size <width, height>: Sets the size of the field (default: 800, 600)")
    print("    -c, --cell-size <size>:     Sets the size of the cells default: 10")
    print("    -r, --rules <rules>:        Sets the rules of the game (default: 3/23)")
    
def main() -> None:
    width = 800
    height = 600
    cell_size = 10
    rules = "3/23"
    
    if len(argv) > 1:
        i = 1
        while i < len(argv):
            if argv[i] == "-h" or argv[i] == "--help":
                usage()
                return
            elif argv[i] == "-s" or argv[i] == "--size":
                if len(argv) > i + 1:
                    width, height = argv[i + 1], argv[i + 2]
                    width = int(width)
                    height = int(height)
                    i += 3
            elif argv[i] == "-c" or argv[i] == "--cell-size":
                if len(argv) > i + 1:
                    cell_size = int(argv[i + 1])
                    i += 2
            elif argv[i] == "-r" or argv[i] == "--rules":
                if len(argv) > i + 1:
                    rules = argv[i + 1]
                    i += 2
            else:
                print("Unknown option: " + argv[i])
                usage()
                return
    
    GameScreen(width, height, cell_size, rules)
    run()


if __name__ == "__main__":
    main()
