# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# sh package for Altaire XMPP bot

def command_sh(source, parameters):
	if parameters.strip():
<<<<<<< HEAD
		result = popen(parameters.encode("utf-8"))
		fmsg(source, (result if result else translate['performed']))
	else: fmsg(source, translate['outOfArguments'])
reg_command('sh', command_sh, 9)
=======
		result = unicode(os.popen('sh -c "' + parameters.encode("utf-8") + '" 2>&1').read())
		fmsg(source, (result if result else translate['performed']))
	else: fmsg(source, translate['outOfArguments'])
reg_command('sh', command_sh, 9)
>>>>>>> d8c89b7edf59fcc175cf5e65e983d4d771e14191
