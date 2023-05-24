class RelativePoint:
    @staticmethod
    def point(p_rel, x, y):
        return (p_rel[0] // 2) + x, (p_rel[1] // 2) - y
