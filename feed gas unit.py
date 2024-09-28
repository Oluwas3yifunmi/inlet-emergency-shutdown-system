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
        #pressurisation startup stepqsdv
        while startup_step == 'pressurisation':
            #checking startup critical equipment status
            #emergency and inlet ball valve status
            inlet_vbl= 'closed'
            inlet_uzv= 'closed'
            #pressure variables
            pic_cv= 0
            inlet_pcv_a= int(input('what percent is PCV-A open to: '))
            inlet_pcv_b= int(input('what percent is PCV-B open to: '))
            #pressurisation process
            while inlet_vbl != 'open':
                #giving open command to uzv
                print('give open command to inlet uzv to begin pressurisation\n')
                inlet_uzv = 'open'
                print('open command given to inlet uzv\nopen command received\ninlet uzv is now open.\n')
                print('set pic controller to pressurisation range')
                break