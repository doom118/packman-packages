# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# restart package for Altaire XMPP bot

def command_restart(source, parameters):
	if parameters.strip():
		bot_off(translate['comms']['restart'] + ' (' + parameters + ')', None, True)
	else: bot_off(translate['comms']['restart'], None, True)
reg_command('restart', command_restart, 8)
