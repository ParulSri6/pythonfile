# String constants for the Terraforming Mars Program

# Program introduction
INTRO_MESSAGE = "Mars Terraforming Program"

# Input prompts
INPUT_TEMPERATURE_PROMPT = "Enter initial temperature (C): "
INPUT_PRESSURE_PROMPT = "Enter initial pressure (Pa): "
INPUT_WATER_PROMPT = "Enter initial water (liters): "

# Decision phase messages
TEMP_TOO_LOW = "Temperature too low"
TEMP_TOLERABLE = "Temperature tolerable"
PRESSURE_TOO_LOW = "Pressure too low"
PRESSURE_SUFFICIENT = "Pressure sufficient"
WATER_TOO_LOW = "Water too low"
WATER_SUFFICIENT = "Water sufficient"

# Strategy prompts
HEATING_STRATEGY_PROMPT = "Choose heating strategy (greenhouse/space mirrors/nuclear): "
PRESSURE_STRATEGY_PROMPT = "Choose pressure strategy (co2/volcanic/plants): "
WATER_STRATEGY_PROMPT = "Choose water strategy (melting/importing/extracting): "

# Heating strategy responses
USING_GREENHOUSE = "Using greenhouse gases"
USING_SPACE_MIRRORS = "Using space mirrors"
USING_NUCLEAR = "Using nuclear reactors"

# Pressure strategy responses
USING_CO2 = "Releasing CO2"
USING_VOLCANIC = "Simulating volcanoes"
USING_PLANTS = "Planting terraforming plants"

# Water strategy responses
USING_MELTING = "Melting ice caps"
USING_IMPORTING = "Importing water"
USING_EXTRACTING = "Extracting from soil"

# Default strategy responses
DEFAULT_HEATING_STRATEGY = "Defaulting to using greenhouse gases"
DEFAULT_PRESSURE_STRATEGY = "Defaulting to releasing CO2"
DEFAULT_WATER_STRATEGY = "Defaulting to melting ice caps"

# Final input prompts
FINAL_INPUT_TEMPERATURE_PROMPT = "Enter final temperature (C): "
FINAL_INPUT_PRESSURE_PROMPT = "Enter final pressure (Pa): "
FINAL_INPUT_WATER_PROMPT = "Enter final water (liters): "

# Final assessment messages
MARS_HABITABLE = "Mars habitable!"
CONTINUE_TERRAFORMING = "Continue terraforming"


def terraform_mars():
    # Initial input
    initial_temperature = int(input(INPUT_TEMPERATURE_PROMPT))
    initial_pressure = int(input(INPUT_PRESSURE_PROMPT))
    initial_water = int(input(INPUT_WATER_PROMPT))

    # Decision phase
    if initial_temperature < -50:
        print(TEMP_TOO_LOW)
        heating_strategy = input(HEATING_STRATEGY_PROMPT)
        if heating_strategy == "greenhouse":
            print(USING_GREENHOUSE)
        elif heating_strategy == "space mirrors":
            print(USING_SPACE_MIRRORS)
        elif heating_strategy == "nuclear":
            print(USING_NUCLEAR)
        else:
            print(DEFAULT_HEATING_STRATEGY)
    else:
        print(TEMP_TOLERABLE)

    if initial_pressure < 600:
        print(PRESSURE_TOO_LOW)
        pressure_strategy = input(PRESSURE_STRATEGY_PROMPT)
        if pressure_strategy == "co2":
            print(USING_CO2)
        elif pressure_strategy == "volcanic":
            print(USING_VOLCANIC)
        elif pressure_strategy == "plants":
            print(USING_PLANTS)
        else:
            print(DEFAULT_PRESSURE_STRATEGY)
    else:
        print(PRESSURE_SUFFICIENT)

    if initial_water < 1000:
        print(WATER_TOO_LOW)
        water_strategy = input(WATER_STRATEGY_PROMPT)
        if water_strategy == "melting":
            print(USING_MELTING)
        elif water_strategy == "importing":
            print(USING_IMPORTING)
        elif water_strategy == "extracting":
            print(USING_EXTRACTING)
        else:
            print(DEFAULT_WATER_STRATEGY)
    else:
        print(WATER_SUFFICIENT)

    # Final input
    final_temperature = int(input(FINAL_INPUT_TEMPERATURE_PROMPT))
    final_pressure = int(input(FINAL_INPUT_PRESSURE_PROMPT))
    final_water = int(input(FINAL_INPUT_WATER_PROMPT))

    # Final assessment
    if final_temperature >= 0 and final_pressure >= 1000 and final_water >= 5000:
        print(MARS_HABITABLE)
    else:
        print(CONTINUE_TERRAFORMING)


if __name__ == "__main__":
    terraform_mars()
