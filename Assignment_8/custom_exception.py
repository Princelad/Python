class InvalidTemperatureError(Exception):
    """Custom exception for invalid temperature values."""
    def __init__(self, temperature, message="Temperature is out of valid range"):
        self.temperature = temperature
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}: {self.temperature} is not a valid temperature"

def check_temperature(temperature):
    """
    Check if the temperature is within a valid range.
    Valid range: -50°C to 60°C
    """
    if temperature < -50 or temperature > 60:
        raise InvalidTemperatureError(temperature)
    return f"Temperature {temperature}°C is within valid range"

def main():
    print("Temperature Validation Program")
    print("Valid temperature range: -50°C to 60°C\n")
    
    while True:
        try:
            user_input = input("Enter a temperature (or 'q' to quit): ")
            
            if user_input.lower() == 'q':
                print("Exiting program...")
                break
                
            temperature = float(user_input)
            result = check_temperature(temperature)
            print(result)
            
        except InvalidTemperatureError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: Please enter a valid number for temperature")
        
        print()  # Add a blank line for readability

if __name__ == "__main__":
    main()
