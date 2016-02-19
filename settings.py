#!/usr/bin/env python
import os 

PORT = 8080
TEMPLATES_PATH='./templates'
STATIC_PATH = './media'

APP = {
    'template_path': os.path.join(STATIC_PATH, TEMPLATES_PATH),
    'static_path': STATIC_PATH
}
