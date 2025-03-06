def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    # using the method update() to add new keys and values to the dictionary
    spacecraft.update({"distance": "0.01", "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    # using get() to find the values of the keys and establishing a default return in case values are not found
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ==========================
    """


main()