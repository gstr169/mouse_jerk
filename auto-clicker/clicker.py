from pynput import mouse


def invisible_move(mouse_controller):
    mouse_controller.move(1, 0)
    mouse_controller.move(-1, 0)


def listen_and_count():
    mouse_controller = mouse.Controller()
    with mouse.Events() as events:
        while True:
            event = events.get(30)
            if event is None:
                invisible_move(mouse_controller)
                print('You did not interact with the mouse within one second')
