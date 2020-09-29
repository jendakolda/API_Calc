import fluids.safety_valve as f


def steam_area(iv):
    area = f.API520_A_steam(m=iv[0] / 3600, T=iv[1] + 273.15, P1=iv[2] * 100000, Kd=iv[3], Kb=iv[4], Kc=iv[5])
    area_rounded = f.API520_round_size(area)
    letter = f.API526_letters[f.API526_A.index(area_rounded)]
    return area, area_rounded, letter


class SteamBackend:
    pass
