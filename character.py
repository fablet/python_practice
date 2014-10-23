import random

from combat import Combat

class Character(Combat):
	attack_limit = 10
	experience = 0
	hit_points = 10

	def get_weapon(self):
		weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow): ").lower()

		if weapon_choice in 'sab':
			if weapon_choice == 's':
				return 'sword'
			elif weapon_choice = 'a':
				return 'axe'
			else:
				return 'bow'
		else:
			return self.get_weapon()

	def attack(self):
		roll = random.randint(1, self.attack_limit)
		if self.weapon == 'sword':
			roll += 1
		elif self.weapon == 'axe':
			roll += 2
		return roll > 4

	def __init__(self, **kwargs):
		self.name = input("Name: ")
		self.weapon = self.get_weapon()

		for key, value in kwargs.items():
			setattr(self, key, value)

