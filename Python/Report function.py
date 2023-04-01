def generate_report(main_tank, external_tank, hydrogen_tank): 
        output = f"""Fuel report: \n
        Main_tank: {main_tank}\n
        External tank: {external_tank}\n
        Hydrogen tank: {hydrogen_tank}"""

        return output 

print(generate_report(90,433,111))

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report(main=50, external=100, emergency=60)