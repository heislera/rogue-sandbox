class Action:
    pass

#user hits ESC key
class EscapeAction(Action):
    pass

#user moves around (w/arrow keys)
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy