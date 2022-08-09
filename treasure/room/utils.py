def direction(point_a, point_b):
    """
    Returns the direction from point_a to point_b, or None if they
    are not neighhbouring grid points.
    """
    if point_b == point_a:
        return "nowhere"
    if point_b[1] == point_a[1]:
        if point_b[0] == point_a[0] - 1:
            return "left"
        if point_b[0] == point_a[0] + 1:
            return "right"
    if point_b[0] == point_a[0]:
        if point_b[1] == point_a[1] - 1:
            return "up"
        if point_b[1] == point_a[1] + 1:
            return "down"

    return None
