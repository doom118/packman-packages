# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# My XMPP-conference: bottiks@conference.jabber.ru
# My Site: bottiks.ucoz.ru
# send package for Altaire XMPP bot


def updateSendFile(update = False):
	File('other/send.txt')
def command_send(source, parameters):
	parameters = parameters.split(None, 1)
	if len(parameters) != 2:
		fmsg(source, translate['outOfArguments'])
	else:
		

reg_command('send', command_send)
register_handler(updateSendFile, 'after_load_jids')
