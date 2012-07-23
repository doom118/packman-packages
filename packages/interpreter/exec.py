# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# My XMPP-conference: bottiks@conference.jabber.ru
# My Site: bottiks.ucoz.ru
# exec package for Altaire XMPP bot

def command_exec(source, parameters):
	if parameters.strip():
		try: exec(unicode(parameters + chr(10)), globals())
		except: result = format_exc()
		else: result = translate['performed']
		fmsg(source, result)
	else: fmsg(source, translate['outOfArguments'])
reg_command('exec', command_exec, 9)