"""Set up the AI and its goals"""
from colorama import Fore, Style

from autogpt import utils
from autogpt.config.ai_config import AIConfig
from autogpt.logs import logger


def prompt_user() -> AIConfig:
    """Prompt the user for input

    Returns:
        AIConfig: The AIConfig object containing the user's input
    """
    ai_name = ""
    # Construct the prompt
    logger.typewriter_log(
        "Willkommen zur Luis-Version von Auto-GPT!",
        Fore.GREEN,
        "run with '--help' für mehr informationen.",
        speak_text=True,
    )

    logger.typewriter_log(
        "Create an AI-Assistant:",
        Fore.GREEN,
        " Geben Sie unten den Namen Ihrer KI und ihre Rolle ein."
        " Wenn Sie nichts eingeben, werden die Standardeinstellungen geladen.",
        speak_text=True,
    )

    # Get AI Name from User
    logger.typewriter_log(
        "Name your AI: ", Fore.GREEN, "For example, 'Luis-GPT'"
    )
    ai_name = utils.clean_input("AI Name: ")
    if ai_name == "":
        ai_name = "Luis-GPT"

    logger.typewriter_log(
        f"{ai_name} here!", Fore.LIGHTBLUE_EX, "I am at your service.", speak_text=True
    )

    # Get AI Role from User
    logger.typewriter_log(
        "Beschreibe die Rolle deiner A.I: ",
        Fore.GREEN,
        "Zum Beispiel, 'eine KI, die entwickelt wurde, um autonom Unternehmen zu entwickeln und zu leiten"
        " das alleinige Ziel, Ihr Nettovermögen zu steigern.'",
    )
    ai_role = utils.clean_input(f"{ai_name} is: ")
    if ai_role == "":
        ai_role = "an AI designed to autonomously develop and run businesses with the"
        " sole goal of increasing your net worth."

    # Gibs bis zu 5 Ziele für Luis AI
    logger.typewriter_log(
        "Gibs bis zu 5 Ziele für Luis AI: ",
        Fore.GREEN,
        "For example: \n , Entwicklung und Verwaltung"
        " mehrere Unternehmen eigenständig'",
    )
    print("Enter nothing to load defaults, enter nothing when finished.", flush=True)
    ai_goals = []
    for i in range(5):
        ai_goal = utils.clean_input(f"{Fore.LIGHTBLUE_EX}Goal{Style.RESET_ALL} {i+1}: ")
        if ai_goal == "":
            break
        ai_goals.append(ai_goal)
    if not ai_goals:
        ai_goals = [
            "Increase net worth",
            "Grow Twitter Account",
            "Develop and manage multiple businesses autonomously",
        ]

    return AIConfig(ai_name, ai_role, ai_goals)
