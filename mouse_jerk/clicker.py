from pynput import mouse
import argparse


def invisible_move(mouse_controller):
    mouse_controller.move(1, 0)
    mouse_controller.move(-1, 0)


def process_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t', '--timeout', default=30, type=int,
                        help='set timeout in seconds after last event')

    args = parser.parse_args()
    return args.timeout


def listen_and_count():
    timeout = process_args()
    mouse_controller = mouse.Controller()
    with mouse.Events() as events:
        while True:
            event = events.get(timeout)
            if event is None:
                invisible_move(mouse_controller)
                print(f'You did not interact with the mouse within {timeout} seconds')
