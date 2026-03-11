# skills/skill_loader.py

class SkillLoader:

    def __init__(self):
        self.skills = {}

    def register_skill(self, name, skill):
        self.skills[name] = skill
        print(f"Skill registered: {name}")

    def get_skill(self, name):
        return self.skills.get(name)
