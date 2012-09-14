# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# My XMPP-conference: bottiks@conference.jabber.ru
# My Site: bottiks.ucoz.ru
# sh package for Altaire XMPP bot

def command_sh(source, parameters):
	if parameters.strip():
		result = popen(parameters.encode("utf-8"))
		fmsg(source, (result if result else translate['performed']))
	else: fmsg(source, translate['outOfArguments'])
reg_command('sh', command_sh, 9)
