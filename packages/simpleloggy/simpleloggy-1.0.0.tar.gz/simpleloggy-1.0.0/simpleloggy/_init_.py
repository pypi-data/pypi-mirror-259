from datetime import datetime
from time import sleep
from os import system 

logfile = open('latest.log', 'w+')
logfile.truncate(0)

loggerConfig = {
    "logBranding": " [SLoggy] ",
    "printLogs": False,
    "isInited": False
}

def log(text):
    """Write anything in logs"""
    if loggerConfig['isInited']:
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        logtext = f'[{time}]{loggerConfig["logBranding"]}{text}'
        logfile.write(logtext + '\n')
        if loggerConfig["printLogs"]:
            print(logtext)
    else:
        raise Exception('not inited')

def warn(text):
    """Write warn in logs"""
    log(f'[WARN] {text}')

def error(text):
    """Write error in logs"""
    log(f'[ERROR] {text}')

def info(text):
    """Write info in logs"""
    log(f'[INFO] {text}')

def user(text):
    """Make a input with your text what will be logged."""
    userInput = input(text)
    log(f'[USER] {userInput}')
    return userInput

def custom(logtype, text):
    """Write custom log in logs"""
    log(f'[{logtype}] {text}')

def init_logger(branding = None, printInLogs = True, alertAboutInit = True):
    if branding != None:
        loggerConfig['logBranding'] = f' [{branding}] '
    else:
        loggerConfig['logBranding'] = ' '
    loggerConfig['printLogs'] = printInLogs
    loggerConfig['isInited'] = True
    if alertAboutInit:
        log(f'SLogger started with parameters: {loggerConfig}')


