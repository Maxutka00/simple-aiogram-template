import sqlite3



class ActionWithDB():
	"""Управление базой данных"""
	def __init__(self):
		self.conn= sqlite3.connect('data.db')
		self.cursor = self.conn.cursor()
		