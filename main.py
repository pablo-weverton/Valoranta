# -*- coding: utf-8 -*-
import requests
import pygame

ENDPOINT = 'https://valorant-api.com/v1/agents/'

params = {
    'isPlayableCharacter': True,
}

response = requests.get(f'{ENDPOINT}22697a3d-45bf-8dd7-4fec-84a9e28c69d7',params=params).json()['data']

agent_data = {
    'name': response['displayName'],
    'description': response['description'],
    'image-url': response['fullPortraitV2'],
    'voice-agent': response['voiceLine']['mediaList'][0]['wave'],
    'abilities': {
        'Ability1': {
            'name': response['abilities'][0]['displayName'],
            'description': response['abilities'][0]['description'],
            'icon': response['abilities'][0]['displayIcon']
        },
        'Ability2': {
            'name': response['abilities'][1]['displayName'],
            'description': response['abilities'][1]['description'],
            'icon': response['abilities'][1]['displayIcon']
        },
        'Ability3': {
            'name': response['abilities'][2]['displayName'],
            'description': response['abilities'][2]['description'],
            'icon': response['abilities'][2]['displayIcon']
        },
        'Ability4': {
            'name': response['abilities'][3]['displayName'],
            'description': response['abilities'][3]['description'],
            'icon': response['abilities'][3]['displayIcon']
        }
    }
}

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('765052468.wav')
pygame.mixer.music.play()
pygame.event.wait()

print(agent_data)



