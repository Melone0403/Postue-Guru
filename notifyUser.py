from win10toast import ToastNotifier

def show_mess():
    msg = ToastNotifier()
    msg.show_toast("alarm", "Check Your Posture")
