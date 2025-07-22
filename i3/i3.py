import i3ipc

def on_window_event(self, event):
    print(f"Event: {event}")

i3 = i3ipc.Connection()
i3.on('window::focus', on_window_event)
i3.on('window::new', on_window_event)
i3.on('window::close', on_window_event)
i3.main()
