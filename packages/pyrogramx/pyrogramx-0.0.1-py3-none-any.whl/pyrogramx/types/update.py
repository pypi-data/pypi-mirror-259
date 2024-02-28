import pyrogramx


class Update:
    def stop_propagation(self):
        raise pyrogramx.StopPropagation

    def continue_propagation(self):
        raise pyrogramx.ContinuePropagation
