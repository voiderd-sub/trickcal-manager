from dps.artifact import Artifact
from dps.enums import DamageType

class ToyTelescope(Artifact):
    # This dictionary will hold the character-specific distance factor 'a'.
    # It should be populated manually with {character_name: factor}
    # Characters not in this map will have a factor of 0.
    DISTANCE_FACTOR_MAP = {
        "시온 더 다크불릿": 1.0,
        "실라": 1.0,
        "죠안": 0.470,
        "림(혼돈)": 0.415,
        "아멜리아": 0.261,
    }

    def __init__(self, level: int = 1):
        super().__init__(name="장난감 망원경", level=level)
        self.init_effect_fn = self.apply_init_effect

    def apply_init_effect(self, hero):
        """
        Applies damage amplification for basic and enhanced attacks based on
        the hero's distance factor 'a' and whether they are an Eldain.
        """
        if not self.effects:
            return

        effect_value = self.effects[0]
        distance_factor_a = self.DISTANCE_FACTOR_MAP.get(hero.name_kr, 0)
        print(f"Distance factor a for {hero.name_kr}: {distance_factor_a}")
        
        if distance_factor_a == 0:
            return

        # Calculate base amplification values
        basic_attack_amp = 40 * distance_factor_a * effect_value
        enhanced_attack_amp = 10 * distance_factor_a * effect_value

        print(f"Basic attack amp: {basic_attack_amp}")
        print(f"Enhanced attack amp: {enhanced_attack_amp}")

        # Apply Eldain bonus: double the basic attack amplification
        if hero.is_eldain:
            basic_attack_amp *= 2

        # Apply the amplification to the hero
        if basic_attack_amp > 0:
            hero.add_amplify(DamageType.AutoAttackBasic, basic_attack_amp)
            print(f"Added basic attack amp: {basic_attack_amp}")
            print(f"Hero amplify: {hero.get_amplify(DamageType.AutoAttackBasic)}")
        
        if enhanced_attack_amp > 0:
            hero.add_amplify(DamageType.AutoAttackEnhanced, enhanced_attack_amp) 
            print(f"Added enhanced attack amp: {enhanced_attack_amp}")
            print(f"Hero amplify: {hero.get_amplify(DamageType.AutoAttackEnhanced)}")