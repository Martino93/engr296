from vars import vars
from openai import OpenAI

config = vars('./config/.env')

key = config['api_key']


# function that takes in string argument as parameter 
def comp(PROMPT, MaxToken=50, outputs=3): 
	# using OpenAI's Completion module that helps execute 
	# any tasks involving text 
	response = OpenAI.completions.create(
		# model name used here is text-davinci-003 
		# there are many other models available under the 
		# umbrella of GPT-3 
		model="text-davinci-003", 
		# passing the user input 
		prompt=PROMPT, 
		# generated output can have "max_tokens" number of tokens 
		max_tokens=MaxToken, 
		# number of outputs generated in one call 
		n=outputs 
	) 
	# creating a list to store all the outputs 
	output = list() 
	for k in response['choices']: 
		output.append(k['text'].strip()) 
	return output



