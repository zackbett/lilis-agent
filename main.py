# main.py

from core.agent import LilisAgent
from skills.skill_loader import SkillLoader


def main():
    print("Starting LILIS...")

    # initialize systems
    agent = LilisAgent()
    skill_loader = SkillLoader()

    # example skill registration
    skill_loader.register_skill("example", lambda: print("Example skill executed"))

    # start agent
    agent.run()


if __name__ == "__main__":
    main()
