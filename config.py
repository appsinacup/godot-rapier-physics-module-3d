def can_build(env, platform):
    return False
    # Rapier doesn't support double precision
    return env.get("precision", "single") != "double"


def configure(env):
    pass
