def verification(param):
    if param not in (5, 2, 3):
        raise ValueError("'Param' ne peut etre que 5,2,3")

verification(10)