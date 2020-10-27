from pynput import mouse
import argparse
import signal
import sys


def invisible_move(mouse_controller):
    mouse_controller.move(1, 0)
    mouse_controller.move(-1, 0)


def process_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-t', '--timeout', default=30, type=int,
                        help='set timeout in seconds after last event')
    parser.add_argument('--silent', action='store_true',
                        help="don't printing to STDOUT")

    args = parser.parse_args()
    return args


def signal_handler(_, __):
    sys.exit(0)


def listen_and_count():
    args = process_args()
    timeout = args.timeout
    silent = args.silent
    mouse_controller = mouse.Controller()
    signal.signal(signal.SIGINT, signal_handler)
    with mouse.Events() as events:
        while True:
            event = events.get(timeout)
            if event is None:
                invisible_move(mouse_controller)
                if not silent:
                    print(f'You did not interact with the mouse within {timeout} seconds')
