# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# My XMPP-conference: bottiks@conference.jabber.ru
# My Site: bottiks.ucoz.ru
# leave package for Altaire XMPP bot

def command_rejoin(source, parameters):
	parameters = parameters.split()
	lenp = len(parameters)
	if lenp == 1:
		if access(source[2]) >= 7:
			if parameters[0] == source[3]: fmsg(source, translate['pRoom'])
			else:
				if search_conf(parameters[0]):
					JIDS[get_connect_jid(source[0])].conferences[parameters[0]].rejoin()
					fmsg(source, translate['performed'])
				else: fmsg(source, translate['notInRoom'])
		else: fmsg(source, translate['noAccess'])
	elif lenp == int() and source[1] == 'groupchat':
		JIDS[source[5]].conferences[source[3]].rejoin()
	else: fmsg(source, translate['outOfArguments'])
reg_command('rejoin', command_rejoin, 3)