import threading


class EmailThread(threading.Thread):
    """Overriding constructor"""

    def __init__(self, email_obj):
        """Calling parent class constructor"""
        threading.Thread.__init__(self)
        self.email_obj = email_obj

    def run(self):
        self.email_obj.send()
