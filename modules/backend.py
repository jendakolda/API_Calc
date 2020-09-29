import fluids


def steam_area(iv):
    return fluids.safety_valve.API520_A_steam(m=iv[0], T=iv[1], P1=iv[2], Kd=iv[3], Kb=iv[4], Kc=iv[5])


class SteamBackend:
    pass
