import sys
from rich.console import Console

SUBCOMMAND_NAMES = ["analyse"]


def should_callback_execute():
    return "--help" not in sys.argv and sys.argv[-1] not in SUBCOMMAND_NAMES


class UnbufferedStream():
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


sys.stdout = UnbufferedStream(sys.stdout)
sys.stderr = UnbufferedStream(sys.stderr)


def flush_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sys.stdout.flush()
        sys.stderr.flush()
        return result

    return wrapper


console = Console()
# console.print = flush_output(console.print)

error_console = Console(stderr=True, style="bold red")
# error_console.print = flush_output(error_console.print)
