#Texting module.

class Texter(object):

	def validateNumber(toValidate):
		return true #Temporary placeholder. Fix this later

	def sendRequest(request):

	def formSendRequest(self, text, number):

	def sendMSG(self, text, number):
		if validateNumber(number):
			request = formSendRequest(self = self, text = text, number = number)
			sendRequest(request)
		else:
			raise ValueError('The number passed is not a valid telephone number.')