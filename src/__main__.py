from multiprocessing import Event
import sys
from main.client import run_client


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--settings":
        from gui.settings import root
        root.mainloop()
    else:
        run_client()


if __name__ == "__main__":
    main()
