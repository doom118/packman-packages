# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# My XMPP-conference: bottiks@conference.jabber.ru
# My Site: bottiks.ucoz.ru
# help package for Altaire XMPP bot

def command_help(source, parameters):
	parameters = parameters.split()
	lenp = len(parameters)
	if lenp == 1:
		if parameters[0] == translate['comms']['help']['all']:
			answer = translate['comms']['help']['allCommands']
			for comstat in commands.keys():
				answer += commands[comstat]['commands'][0]
				if len(commands[comstat]['commands']) > 1:
					answer += ' (%s: %s)' % \
						(translate['comms']['help']['analogues'], 
						', '.join(commands[comstat]['commands'][1:]))
				answer += chr(10)
			fmsg(source, answer)
		else:
			temp = search_command(parameters[0])
			if temp:
				fmsg(source, File(commands[temp]['help']))
			else:
				fmsg(source, translate['comms']['help']['noCommand'])
	elif lenp == 0:
		fmsg(source, translate['comms']['help']['defaultAnswer'])
	else: fmsg(source, translate['outOfArguments'])

reg_command('help', command_help)