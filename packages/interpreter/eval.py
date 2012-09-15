# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# eval package for Altaire XMPP bot

def command_eval(source, parameters):
	if parameters.strip():
		try: result = unicode(eval(unicode(parameters)))
		except: result = format_exc()
		fmsg(source, result)
	else: fmsg(source, translate['outOfArguments'])
reg_command('eval', command_eval, 9)
