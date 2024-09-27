gas_supply= input('is there gas supply to the train(yes/no):\n').lower()
steps= ['pressurisation', 'startup']
status= ['open', 'closed']
#checking if there is feed gas supply
if gas_supply == 'no':
    print('Open feed gas supply from inlet manifold to train')
else:
    #feed gas supply is available
    while gas_supply != 'no':
        try:
            #getting process variables and handling for errors
            inlet_pressure= int(input('what is the pressure of the feed gas: '))
            inlet_temp= int(input('what is the temperature of the feed gas: '))
            #checking startup process
            startup_step= input('what startup operation is to be carried out(pressurisation/startup): ').lower()
            #validating startup process
            if startup_step not in steps:
                raise ValueError("You have entered a wrong startup step or an invalid response")
        except ValueError as e:
            print(e)
            print('please enter valid data')
            continue
        #Startup steps
        #pressurisation startup step
        if startup_step == 'pressurisation':
            #checking equipment status
            inlet_vbl= 'closed'
            inlet_uzv= input('what is the status of the inlet emergency shutdown valve(open/closed): \n')