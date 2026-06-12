from dataclasses import dataclass 

@dataclass 
class Planet:
    star_type: str              # O, B, A, F, G, K, M
    planet_temperature: int     # Kelvins
    planet_radius: int          # compared to Earth
    distance_from_star: int     # AU (Astronomical Units)
    oxygen: str                 # concentration in atmosphere: low, medium, high
    methane: str
    water_vapor: str
    carbon_dioxide: str

planet = Planet("M", 1000, 1, 1, "high", "high", "medium", "low")

@dataclass
class Interpretation:
    evidence_for_life: str
    false_positive_risks: str
    uncertainties: str
    summary: str
    
def analyze_planet(planet: Planet) -> Interpretation:
    evidence_for_life = []
    false_positive_risks = []
    uncertainties = []
    summary = []
    
    if planet.oxygen == "high" and planet.methane in ["medium", "high"]:
        evidence_for_life.append("Oxygen and methane together may suggest atmospheric disequilibrium and are likely replenished by life.")
        
    return Interpretation(
        evidence_for_life=evidence_for_life,
        false_positive_risks=false_positive_risks,
        uncertainties=uncertainties,
        summary=summary
    )