# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# My XMPP-conference: bottiks@conference.jabber.ru
# My Site: bottiks.ucoz.ru
# join package for Altaire XMPP bot

def command_join(source, parameters):
	parameters = parameters.split()
	lenp = len(parameters)
	if lenp in (1, 2): 
		if search_conf(parameters[0]): fmsg(source, translate['nowInRoom'])
		else:
			jid = min_confs()
			JIDS[jid].conferences[parameters[0]] = conference(get_connect(jid), parameters[0])
			if lenp == 1: JIDS[jid].conferences[parameters[0]].join()
			else: JIDS[jid].conferences[parameters[0]].join(parameters[1])
			fmsg(source, translate['performed'])
	else: fmsg(source, translate['outOfArguments'])
reg_command('join', command_join, 1)