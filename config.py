def can_build(env, platform):
    # Rapier doesn't support double precision
    if env.get("precision", "single") == "double":
        return False
    return True

def configure(env):
    pass

def get_doc_classes():
    return [
        "Fluid3D",
        "FluidEffect3D",
        "FluidEffect3DElasticity",
        "FluidEffect3DSurfaceTensionAKINCI",
        "FluidEffect3DSurfaceTensionHE",
        "FluidEffect3DSurfaceTensionWCSPH",
        "FluidEffect3DViscosityArtificial",
        "FluidEffect3DViscosityDFSPH",
        "FluidEffect3DViscosityXSPH",
        "RapierDirectBodyState3D",
        "RapierDirectSpaceState3D",
        "RapierMath3D",
        "RapierPhysics3DExtensionLibrary",
        "RapierPhysicsServer3D",
        "RapierPhysicsServerFactory3D",
    ]

def get_doc_path():
    return "doc_classes"
