# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# My XMPP-conference: bottiks@conference.jabber.ru
# My Site: bottiks.ucoz.ru
# off package for Altaire XMPP bot

def command_off(source, parameters):
	if parameters.strip():
		bot_off(translate['comms']['off'] + ' (' + parameters + ')')
	else: bot_off(translate['comms']['off'])

reg_command('off', command_off, 8)