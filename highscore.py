from effects import print_text


class HighScore:

    def __init__(self, table):
        self.hs_table = table

    def update(self, name, scores):
        self.hs_table[name] = scores

    def print(self, x, y):
        step_x = 250
        step_y = 30

        sorted_dict = sorted(self.hs_table.items(), key=lambda val: -val[1])[:5]
        for name, scores in sorted_dict:
            print_text(name, x, y)
            x += step_x
            print_text(str(scores), x, y)
            x -= step_x
            y += step_y
