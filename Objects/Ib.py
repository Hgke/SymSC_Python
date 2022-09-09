import numpy as np
from Objects.ElementBase import ElementBase


class Ib(ElementBase):
    def __init__(self, loc, val):
        super().__init__()

        if len(loc) == 1:
            loc = [loc[0], 0]
        self.loc = loc
        self.val = val

        self.name = 'Ib'
        self.complex = False

        self.contains_current = False
        self.contains_variable = False

    def get_matrix_stamp(self, h):
        return np.zeros((2, 2)) if 0 in self.loc else np.zeros((1, 1))

    def get_right_side(self, sol, i, h):
        if self.loc[0] == 0:  # no V+
            return np.array([-self.val])
        elif self.loc[1] == 0:  # no V-
            return np.array([self.val])
        else:
            return np.array([-self.val, self.val])

    def get_data(self, kind, t, sol):
        if kind == 'I':
            return np.zeros_like(t) + self.val
        else:
            raise ValueError('Only I(t) data are avaliable for current sources')
