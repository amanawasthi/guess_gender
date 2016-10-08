import requests
import json		

class endpoint:
	def findGender(self):
		name = input("Enter Your name: ")
		URL = "https://api.genderize.io/?name="+name

		response = requests.get(URL)
		parsed_json = json.loads(response.text)
		gender = parsed_json['gender']
		if gender == None:
			print("Request could not be processed. Come back later!")
			return 0		
		self.show(gender)
	
	def show(self,gender):
		if gender == 'male':
			print("The gender is male")
		elif gender == 'female':
			print("The gender is female")
		
client = endpoint()
client.findGender()