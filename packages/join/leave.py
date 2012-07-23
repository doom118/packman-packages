# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# My XMPP-conference: bottiks@conference.jabber.ru
# My Site: bottiks.ucoz.ru
# leave package for Altaire XMPP bot

def command_leave(source, parameters):
	parameters = parameters.split()
	lenp = len(parameters)
	if lenp == 1:
		if access(source[2]) >= 7:
			if parameters[0] == source[3]: fmsg(source, translate['pRoom'])
			else:
				if search_conf(parameters[0]):
					JIDS[get_connect_jid(connect)].conferences[parameters[0]].leave()
					del JIDS[get_connect_jid(connect)].conferences[parameters[0]]
					fmsg(source, translate['performed'])
				else: fmsg(source, translate['notInRoom'])
		else: fmsg(source, translate['noAccess'])
	elif lenp == int() and source[1] == 'groupchat':
		JIDS[source[5]].conferences[source[3]].leave()
		del JIDS[source[5]].conferences[source[3]]
	else: fmsg(source, translate['outOfArguments'])
reg_command('leave', command_leave, 4)