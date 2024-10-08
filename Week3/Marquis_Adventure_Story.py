"""
Author: Shaun Marquis

Purpose: Create an adventure game that allows multiple options and each option
gives you a different path.

**** For extra credit i added while loops for error checking.  The program will repeat the question until the correct option is selected instead of just exiting.
"""


#Import so i can use the exit function
import sys

#Mid-week turn in. Only the first is currently working as requested.  Almost finished with the second. I also want to try and use loops for the choice check.

#Opening story line
print('\nYou wake up disoriented in a metalic chamber with lights and future looking electronics. A display flickers to life, offering you two choices:')

#Options user can choose from
print('\n1. INVESTIGATE the control panel.')
print('2. EXIT through the doorway.\n')

#Get first option from user
while True:
    option_1 = input('Choose INVESTIGATE or EXIT: ')

    #First option path if statement
    if option_1.upper() == 'INVESTIGATE':
        print('\nYou approach the panel, symbols start to appear, and screens display equations.  You realize it''s a navigation system. Two destinations blink.')

        print('\n1. Planet KOLOB, a lush green world.')
        print('2. Interdimensional NEXUS, a gateway to unknown space.\n')

        while True:
            #Get second option from first story line
            option_2 = input('Choose KOLOB or NEXUS: ')

            #Second option in first story line
            if option_2.upper() == 'KOLOB':
                print('\nIn the depths of space on your way to Kolob, you encounter a distress signal. Will you investigate or continue your journey?\n')

                while True:
                    #Grab option 3 from the first story line from the user
                    option_3 = input('Choose INVESTIGATE or CONTINUE: ')

                    #1st Third option in first story line
                    if option_3.upper() == 'INVESTIGATE':
                        print('\nA mysterious figure offers you a chance to rule the universe at their side giving you unlimited power!!!\n')
                        sys.exit(0)
            
                    #2nd Third option in first story line
                    elif option_3.upper() == 'CONTINUE':
                        print('\nYou become lost on your journey never to find Planet Kolob spending your days going from planet')
                        print('to planet in search of a way back home!!\n')
                        sys.exit(0)
        
                    #check if the correct option was entered
                    else:
                        print('\nInvalid option. You must choose INVESTIGATE or CONTINUE.\n')

            elif option_2.upper() == 'NEXUS':
                print('\nA rift in space-time opens before you offering you a doorway into alternate realities. Do you choose to')
                print('walk through the PORTAL or play it safe and CLOSE the portal?\n')

                while True:
                    option_3 = input('Choose PORTAL or CLOSE: ')

                    if option_3.upper() == 'PORTAL':
                        print('\nYou walk through the portal finding yourself on a planet much like the one you left with only slight differences.')
                        print('You are given a device that allows you to travel to any reality you wish.\n')
                        sys.exit(0)

                    elif option_3.upper() == 'CLOSE':
                        print('\nYou close the portal never knowing what mysteries you could have unfolded but are given the')
                        print('ability teleport anywhere on the planet!!\n')
                        sys.exit(0)
                    
                    else:
                        print('\nInvalid Choice. You must choose PORTAL or CLOSE.\n')

            else:
                print('\nInvalid option. You must choose KOLOB or NEXUS.\n')
        

    elif option_1.upper() == 'EXIT':
        print('\nThe doorway leads to a vast chamber filled with swirling energies. Two passages stretch out before you:')

        print('\n1. The Quantum FOREST, a landscape of shifting realities.')
        print('2. Space station TRINITY, a portal to a hub of technology.\n')

        while True:
            option_2 = input('Which passage do you take? FOREST or TRINITY: ')

            if option_2.upper() == 'FOREST':
                print('\nYou are instantly transported to a reality in which you are on the beach one moment and in a metropolis the next.')
                print('You notice that you now have a quantum device on your arm.  You can REMOVE it immediately or start PRESSING buttons.')

                while True:
                    option_3 = input('\nChoose REMOVE or PRESSING: ')

                    if option_3.upper() == 'REMOVE':
                        print('\nAs you rip the device off your arm you notice that you are no longer moving between different landscapes.')
                        print('You seem to be stuck in the last reality you visited.  A reality where everyone has twinkies for fingers.\n')
                        sys.exit(0)

                    elif option_3.upper() == 'PRESSING':
                        print('\nYou are now the master of reality. You can come and go from any reality you wish.  Enjoy the leap!!!\n')
                        sys.exit(0)

                    else:
                        print('\nInvalid Choice. You must choose REMOVE or PRESSING.\n')

            #This option will have 3 choices as required by the instuctions
            elif option_2.upper() == 'TRINITY':
                print('\nWhen you arrive at Trinity space station you are brought to a console stored with knowledge. Three files catch your eye.\n')

                print('1. Chronicles of TIME: Unravel the mysteries of time manipulation.')
                print('2. Records of the ANCIENTS: Discover the secrets of ancient civilizations.')
                print('3. Quantum EQUATION: Unlock the fabric of reality.\n')

                while True:
                    #Getting input from the user
                    option_3 = input('Choose TIME, ANCIENTS, or EQUATION: ')

                    #Several if statements that allow the user to choose which ending they would like.
                    if option_3.upper() == 'TIME':
                        print('\nAs you are in the process of selecting the option to unravel the mysteries of time, an older version of yourself tackles you and')
                        print('breaks the machine before you have a chance to view it. Your older self fades away into nothingness.\n')
                        sys.exit(0)

                    elif option_3.upper() == 'ANCIENTS':
                        print('\nYou finally find out that aliens created the pyramids thousands of years ago and are responsible for Kentucky Fried Chicken.\n')
                        sys.exit(0)

                    elif option_3.upper() == 'EQUATION':
                        print('\nYou have unlocked the mysteries of reality. You now realize that your whole life has happened in a split second and you')
                        print('have your whole life laid out before you like a scroll. You now know that time was created to allow you to observe those moments.\n')
                        sys.exit(0)

                    else:
                        print('\nInvalid option. You must choose TIME, ANCIENTS, or EQUATION.\n')

            else:
                print('\nInvalid option. You must choose FOREST or TRINITY.\n')

    #Check for correct options
    else:
        print('\nInvalid option. You must choose INVESTIGATE or EXIT.\n')