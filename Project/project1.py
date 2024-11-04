class Driver:
    def __init__(self, id, name, start_city):
        self.id = id
        self.name = name
        self.start_city = start_city

    def __str__(self):
        return f"{self.id}, {self.name}, {self.start_city}"


class City:
    def __init__(self, name):
        self.name = name
        self.neighboring_cities = []

    def add_neighbor(self, city):
        if city not in self.neighboring_cities:
            self.neighboring_cities.append(city)

    def __str__(self):
        return self.name


class DeliverySystem:
    def __init__(self):
        self.drivers = []
        self.cities = {}
        self.driver_id_counter = 1

    def add_driver(self, name, start_city):
        if start_city not in self.cities:
            add_city = input(f"{start_city} is not available. Would you like to add it? (yes/no): ")
            if add_city.lower() == 'yes':
                self.add_city(start_city)
            else:
                print("Driver not added.")
                return
        
        driver_id = f"ID{self.driver_id_counter:03}"
        self.drivers.append(Driver(driver_id, name, start_city))
        self.driver_id_counter += 1
        print(f"Driver {name} added with ID {driver_id}.")

    def add_city(self, name):
        if name not in self.cities:
            self.cities[name] = City(name)
            print(f"City {name} added.")
        else:
            print(f"City {name} already exists.")

    def show_drivers(self):
        if not self.drivers:
            print("No drivers available.")
        else:
            for driver in self.drivers:
                print(driver)

    def show_cities(self):
        sorted_cities = sorted(self.cities.keys(), reverse=True)
        print(", ".join(sorted_cities))

    def find_similar_drivers(self):
        city_drivers = {}
        for driver in self.drivers:
            if driver.start_city not in city_drivers:
                city_drivers[driver.start_city] = []
            city_drivers[driver.start_city].append(driver.name)

        for city, drivers in city_drivers.items():
            print(f"{city}: {', '.join(drivers)}")

    def search_city(self, key):
        matching_cities = [city for city in self.cities.keys() if key in city]
        if matching_cities:
            print(", ".join(matching_cities))
        else:
            print("No matching cities found.")

    def print_neighbors(self, city_name):
        if city_name in self.cities:
            neighbors = self.cities[city_name].neighboring_cities
            if neighbors:
                print(f"Neighboring cities to {city_name}: {', '.join(neighbors)}")
            else:
                print(f"No neighboring cities for {city_name}.")
        else:
            print(f"{city_name} not found.")

    def add_neighboring_city(self, city_name, neighbor_name):
        if city_name in self.cities and neighbor_name in self.cities:
            self.cities[city_name].add_neighbor(neighbor_name)
            print(f"Added {neighbor_name} as a neighboring city to {city_name}.")
        else:
            print("One or both cities not found.")


def main():
    system = DeliverySystem()
    
    while True:
        print("\nHello! Please enter:")
        print("1. To go to the drivers’ menu")
        print("2. To go to the cities’ menu")
        print("3. To exit the system")
        choice = input("Your choice: ")

        if choice == '1':
            while True:
                print("\nDRIVERS’ MENU")
                print("1. To view all the drivers")
                print("2. To add a driver")
                print("3. Check similar drivers")
                print("4. To go back to the main menu")
                driver_choice = input("Your choice: ")

                if driver_choice == '1':
                    system.show_drivers()
                elif driver_choice == '2':
                    name = input("Enter the driver's name: ")
                    start_city = input("Enter the driver's start city: ")
                    system.add_driver(name, start_city)
                elif driver_choice == '3':
                    system.find_similar_drivers()
                elif driver_choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == '2':
            while True:
                print("\nCITIES’ MENU")
                print("1. Show cities")
                print("2. Search city")
                print("3. Print neighboring cities")
                print("4. Print Drivers delivering to city")
                print("5. To go back to the main menu")
                city_choice = input("Your choice: ")

                if city_choice == '1':
                    system.show_cities()
                elif city_choice == '2':
                    key = input("Enter a key to search for cities: ")
                    system.search_city(key)
                elif city_choice == '3':
                    city_name = input("Enter a city name: ")
                    system.print_neighbors(city_name)
                elif city_choice == '4':
                    city_name = input("Enter a city name: ")
                   
                   
                elif city_choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
