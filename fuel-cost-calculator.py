# Day 26 - Fuel Cost Calculator (2026-11-01)
#
# What it does:
#   Calculates how much fuel you need and what a trip will cost, so you can
#   budget before you travel. Works with km or miles, litres or gallons.
#
# Who it is useful for:
#   Anyone who drives a car, rides a motorbike, or shares a trip with friends -
#   great for planning road trips, daily office commutes, or splitting fuel
#   costs fairly with passengers.
#
# Plain Python, no external libraries needed.


def litres_needed(distance, mileage_per_litre):
    """Fuel needed for a trip: distance (km) / mileage (km per litre)."""
    if mileage_per_litre <= 0:
        raise ValueError("Mileage must be greater than 0")
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    return distance / mileage_per_litre


def trip_fuel_cost(distance, mileage_per_litre, fuel_price_per_litre):
    """Total fuel cost of a trip (same currency as the fuel price)."""
    if fuel_price_per_litre < 0:
        raise ValueError("Fuel price cannot be negative")
    return litres_needed(distance, mileage_per_litre) * fuel_price_per_litre


def cost_per_person(distance, mileage_per_litre, fuel_price_per_litre, people):
    """Fuel cost split fairly among the people sharing the ride."""
    if people <= 0:
        raise ValueError("Number of people must be greater than 0")
    total = trip_fuel_cost(distance, mileage_per_litre, fuel_price_per_litre)
    return total / people


def monthly_commute_cost(daily_distance_km, mileage_per_litre,
                         fuel_price_per_litre, working_days=22):
    """Estimated fuel cost for a whole month of office commuting."""
    return trip_fuel_cost(daily_distance_km, mileage_per_litre,
                          fuel_price_per_litre) * working_days


if __name__ == "__main__":
    # Example 1: Dhaka to Cox's Bazar road trip (~390 km) by car.
    # Car gives 12 km/litre, octane costs 125 taka/litre.
    trip_cost = trip_fuel_cost(distance=390, mileage_per_litre=12,
                               fuel_price_per_litre=125)
    fuel = litres_needed(390, 12)
    print("Dhaka -> Cox's Bazar: %.1f litres needed, trip fuel cost %.0f taka"
          % (fuel, trip_cost))

    # Example 2: Split that trip cost among 4 friends sharing the car.
    share = cost_per_person(distance=390, mileage_per_litre=12,
                            fuel_price_per_litre=125, people=4)
    print("Each person's share: %.0f taka" % share)

    # Example 3: Monthly office commute - 20 km each way (40 km/day) by
    # motorbike giving 45 km/litre, petrol at 122 taka/litre.
    monthly = monthly_commute_cost(daily_distance_km=40, mileage_per_litre=45,
                                   fuel_price_per_litre=122)
    print("Monthly commute fuel cost: %.0f taka" % monthly)
