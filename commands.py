from glad_vars import *
import random
import requests

def execute_api_lights(state, target, domain):
    if state == keyword_on:
        if domain == "lights":
            executing_url = light_on
        elif domain == "script":
            executing_url = script_on
        elif domain == "shopping_list":
            executing_url = shopping_list
        elif domain == "task_list":
            executing_url = task_list
    elif state == keyword_off:
        if domain == "lights":
            executing_url = light_off
        if domain == "script":
            executing_url = script_on

    for item in target:
        payload_data = {"entity_id": item}
        if domain == 'lights' and state == keyword_on:
            payload_data = {"entity_id": item, "brightness": 254, "color_temp": 300}
        elif domain == "shopping_list":
            payload_data = {"name": item}
        elif domain == "task_list":
            payload_data = {"entity_id": "todo.patryk", "item": item}
        response = requests.post(executing_url, headers=headers, json=payload_data)
    return response


def process_output(voice_input):

    temp_input = voice_input.split()
    input = []
    for item in temp_input:
        input.append(item.lower())

    print(input)

    if any(i in keywords_joke for i in input):
        return random.choice(glados_jokes)
    
    elif any(i in keywords_whoami for i in input) and any(i in keywords_whoami2 for i in input):
        return random.choice(glados_whoami)
    
    elif any(i in keywords_howareyou for i in input) and any(i in keywords_howareyou2 for i in input):
        return random.choice(glados_howareyou)
    
    elif any(i in keywords_magicball for i in input):
        return random.choice(glados_magicball)
    
    elif any(i in keywords_lights for i in input) and any(i in keywords_lights2 for i in input):
        #On-off check
        if keyword_on in input:
            keyword = keyword_on
        elif keyword_off in input:
            keyword = keyword_off

        #Check if command want to turn lights in any room
        if any(i in keywords_kitchen for i in input):
            command_response = execute_api_lights(keyword, lights_kitchen, "lights")
        elif any(i in keywords_livingroom for i in input):
            command_response = execute_api_lights(keyword, lights_livingroom, "lights")
        elif any(i in keywords_office for i in input):
            command_response = execute_api_lights(keyword, lights_office, "lights")
        elif any(i in keywords_toilet for i in input):
            command_response = execute_api_lights(keyword, lights_toilet, "lights")
        elif any(i in keywords_bedroom for i in input):
            command_response = execute_api_lights(keyword, lights_bedroom, "lights")
        elif any(i in keywords_hallway for i in input):
            command_response = execute_api_lights(keyword, lights_hallway, "lights")

        #Return responses
        if command_response.status_code == 200:
            return random.choice(glados_command_succesfull)   
        else:
            return random.choice(glados_command_failed)
        
    #Check if command want to turn script
    #VACUUM
    elif any(i in keywords_script_vacuum for i in input):
        command_response = execute_api_lights(keyword_on, script_vacuum, "script")
        print(command_response.status_code)
        if command_response.status_code == 200:
            print("RETURNED 200")
            return random.choice(glados_vacuum)
        else:
            print("RETURNED OTHER")
            return random.choice(glados_command_failed)
    #POWER ON OFF COMPUTER
    elif any(i in keywords_script_powercomputer for i in input):
        if keyword_on in input:
            command_response = execute_api_lights(keyword_on, script_powercomputer, "script")
            if command_response.status_code == 200:
                return random.choice(glados_powercomputer)
            else:
                return random.choice(glados_command_failed)
        elif keyword_off in input:
            command_response = execute_api_lights(keyword_on, script_turnoffcomputer, "script")
            if command_response.status_code == 200:
                return random.choice(glados_command_succesfull)   
            else:
                return random.choice(glados_command_failed)
        else:
            return "I understand what you are saying, but I have no interest in helping you"
    #ENTER HOME
    elif any(i in keywords_script_enter for i in input):
        command_response = execute_api_lights(keyword_on, script_enter, "script")
        if command_response.status_code == 200:
            return random.choice(glados_enter)
        else:
            return random.choice(glados_command_failed)
    #EXIT HOME
    elif any(i in keywords_script_exit for i in input):
        command_response = execute_api_lights(keyword_on, script_exit, "script")
        if command_response.status_code == 200:
            return random.choice(glados_exit)
        else:
            return random.choice(glados_command_failed)
    #RADIO
    elif any(i in keywords_script_antyradio for i in input):
        if keyword_off in input:
            command_response = execute_api_lights(keyword_on, script_turnoffmusic, "script")
        else:
            command_response = execute_api_lights(keyword_on, script_antyradio, "script")
        if command_response.status_code == 200:
            return random.choice(glados_command_succesfull)
        else:
            return random.choice(glados_command_failed)
    #SPOTIFY
    elif any(i in keywords_script_music for i in input):
        if keyword_off in input:
            command_response = execute_api_lights(keyword_on, script_turnoffmusic, "script")
        else:
            command_response = execute_api_lights(keyword_on, script_music, "script")
        if command_response.status_code == 200:
            return random.choice(glados_command_succesfull)
        else:
            return random.choice(glados_command_failed)
    #LISTA ZAKUPÓW
    elif any(i in keywords_shopping_list for i in input):
        print("SHOPPING LIST GO")
        target_list = []
        for item in input:
            if item != 'dodaj' and item !='listy' and item != 'zakupów' and item != 'do' and item != "i":
                target_list.append(item)
        command_response = execute_api_lights(keyword_on, target_list, "shopping_list")
        if command_response.status_code == 200:
            return random.choice(glados_command_succesfull)
        else:
            return random.choice(glados_command_failed)
    #LISTA ZADAN
    elif any(i in keywords_task_list for i in input):
        print("TASK LIST GO")
        target_list = []
        target_string = ""
        for item in input:
            if item != 'dodaj' and item !='listy' and item != 'zadań' and item != 'do':
                target_string = target_string + item + " "
        print(target_string)
        target_list.append(target_string)
        print(target_list)
        command_response = execute_api_lights(keyword_on, target_list, "task_list")
        if command_response.status_code == 200:
            return random.choice(glados_command_succesfull)
        else:
            return random.choice(glados_command_failed)

    else:
        return "I understand what you are saying, but I have no interest in helping you"