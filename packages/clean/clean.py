# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# My XMPP-conference: bottiks@conference.jabber.ru
# My Site: bottiks.ucoz.ru
# clean package for Altaire XMPP bot


def command_clean(source, parameters):
	if search_conf(source[3]):
		if not hasattr(JIDS[jid].conferences[source[3]], 'dirt') or \
		not JIDS[jid].conferences[source[3]].dirt:
			JIDS[jid].conferences[source[3]].dirt = True
			JIDS[jid].conferences[source[3]].setStatus(
				translate['comms']['clean']['status'], 'dnd', True)
			message = xmpp.Message(to = source[3], typ = 'groupchat')
			for x in xrange(23):
				if not search_conf(source[3]): return
				source[0].send(message)
				sleep(1.5)
			source[0].send(message)
			JIDS[jid].conferences[source[3]].setStatus()
			JIDS[jid].conferences[source[3]].dirt = False
		else: fmsg(source, translate['comms']['clean']['nowCleaning'])
	else: fmsg(source, translate['onlyInConference'])

reg_command('clean', command_clean, 1)