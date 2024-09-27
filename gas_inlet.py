# Creating a function for an emergency shutdown system at the inlet of a gas plant
def inlet_esds():
    # Collecting the variable data
    inlet_valve_status = input('Inlet valve status (open/closed): \n').lower()
    esdv_status = input('ESD valve status (open/closed): \n').lower()
    
    trials = 0

    # Check inlet valve status
    if inlet_valve_status == 'closed':
        print('No supply of feed gas\nInlet valve is closed!!')
        return
    else:
        while inlet_valve_status != 'closed':
            try:
                # Measuring process variables
                inlet_pressure = int(input("What is the pressure of the feed gas (bar): "))
                inlet_temperature = int(input("What is the temperature of the feed gas (°C): "))
            except ValueError:
                print("Please enter valid numerical values for pressure and temperature.")
                continue

            # Operations when ESD valve is open
            if esdv_status == 'open':
                if inlet_pressure < 61:
                    print(f'Feed gas is passing through to the gas metering skid at {inlet_pressure} bar.')
                    break
                else:
                    print('Emergency shutdown alert!!!\nESD valve will shut down upon the 3rd pressure measurement!')
                    trials += 1
                    # Measures process variable thrice to ensure standard operating range
                    if trials == 3:
                        print('ESD valve has shut down to prevent flow of excessive pressure into the plant.')
                        break
            # Operations when ESD valve is closed
            else:
                if inlet_pressure < 61:
                    print('Give an open command to the ESD valve to allow gas flow through to the gas metering skid.\n')
                    esdv_status = 'open'
                    print(f'ESD valve is now open!\nGas is flowing through at {inlet_pressure} bar to the gas metering skid.')
                    break
                else:
                    print('ESD valve should remain shut till pressure has been stabilized to plant operating standards!!')
                    if trials == 3:
                        print('Maximum trials reached. ESD valve remains shut.')
                        break

# Call the function
inlet_esds()