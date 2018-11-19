def Zerg():
    return ["Baneling",
            "BanelingBurrowed",
            "BanelingCocoon",
            "BanelingNest",
            "BroodLord",
            "BroodLordCocoon",
            "Broodling",
            "BroodlingEscort",
            "Changeling",
            "ChangelingMarine",
            "ChangelingMarineShield",
            "ChangelingZealot",
            "ChangelingZergling",
            "ChangelingZerglingWings",
            "Corruptor",
            "CreepTumor",
            "CreepTumorBurrowed",
            "CreepTumorQueen",
            "Drone",
            "DroneBurrowed",
            "Cocoon",
            "EvolutionChamber",
            "Extractor",
            "GreaterSpire",
            "Hatchery",
            "Hive",
            "Hydralisk",
            "HydraliskBurrowed",
            "HydraliskDen",
            "InfestationPit",
            "InfestedTerran",
            "InfestedTerranBurrowed",
            "InfestedTerranCocoon",
            "Infestor",
            "InfestorBurrowed",
            "Lair",
            "Larva",
            "Locust",
            "LocustFlying",
            "Lurker",
            "LurkerBurrowed",
            "LurkerDen",
            "LurkerCocoon",
            "Mutalisk",
            "NydusCanal",
            "NydusNetwork",
            "Overlord",
            "OverlordTransport",
            "OverlordTransportCocoon",
            "Overseer",
            "OverseerCocoon",
            "OverseerOversightMode",
            "ParasiticBombDummy",
            "Queen",
            "QueenBurrowed",
            "Ravager",
            "RavagerBurrowed",
            "RavagerCocoon",
            "Roach",
            "RoachBurrowed",
            "RoachWarren",
            "SpawningPool",
            "SpineCrawler",
            "SpineCrawlerUprooted",
            "Spire",
            "SporeCrawler",
            "SporeCrawlerUprooted",
            "SwarmHost",
            "SwarmHostBurrowed",
            "Ultralisk",
            "UltraliskBurrowed",
            "UltraliskCavern",
            "Viper",
            "Zergling",
            "ZerglingBurrowed"]


def Protoss():
    return ["Adept", "AdeptPhaseShift", "Archon",
            "Assimilator",
            "Carrier",
            "Colossus",
            "CyberneticsCore",
            "DarkShrine",
            "DarkTemplar",
            "Disruptor",
            "DisruptorPhased",
            "FleetBeacon",
            "ForceField",
            "Forge",
            "Gateway",
            "HighTemplar",
            "Immortal",
            "Interceptor",
            "Mothership",
            "MothershipCore",
            "Nexus",
            "Observer",
            "ObserverSurveillanceMode",
            "Oracle",
            "Phoenix",
            "PhotonCannon",
            "Probe",
            "Pylon",
            "PylonOvercharged",
            "RoboticsBay",
            "RoboticsFacility",
            "Sentry",
            "ShieldBattery",
            "Stalker",
            "Stargate",
            "StasisTrap",
            "Tempest",
            "TemplarArchive",
            "TwilightCouncil",
            "VoidRay",
            "WarpGate",
            "WarpPrism",
            "WarpPrismPhasing",
            "Zealot"]


def Terran():
    return ["Armory",
            "AutoTurret",
            "Banshee",
            "Barracks",
            "BarracksFlying",
            "BarracksReactor",
            "BarracksTechLab",
            "Battlecruiser",
            "Bunker",
            "CommandCenter",
            "CommandCenterFlying",
            "Cyclone",
            "EngineeringBay",
            "Factory",
            "FactoryFlying",
            "FactoryReactor",
            "FactoryTechLab",
            "FusionCore",
            "Ghost",
            "GhostAcademy",
            "GhostAlternate",
            "GhostNova",
            "HellionTank",
            "Hellion",
            "Hellbat",
            "KD8Charge",
            "Liberator",
            "LiberatorAG",
            "MULE",
            "Marauder",
            "Marine",
            "Medivac",
            "MissileTurret",
            "Nuke",
            "OrbitalCommand",
            "OrbitalCommandFlying",
            "PlanetaryFortress",
            "PointDefenseDrone",
            "Raven",
            "Reactor",
            "Reaper",
            "Refinery",
            "RepairDrone",
            "SCV",
            "SensorTower",
            "SiegeTank",
            "SiegeTankSieged",
            "Starport",
            "StarportFlying",
            "StarportReactor",
            "StarportTechLab",
            "SupplyDepot",
            "SupplyDepotLowered",
            "TechLab",
            "Thor",
            "ThorHighImpactMode",
            "VikingAssault",
            "VikingFighter",
            "WidowMine",
            "WidowMineBurrowed"]


class UnitsList:
    def allunits():
        unitsList = list()
        unitsList.extend(Protoss())
        unitsList.extend(Terran())
        unitsList.extend(Zerg())
        return unitsList