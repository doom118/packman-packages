# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# My XMPP-conference: bottiks@conference.jabber.ru
# My Site: bottiks.ucoz.ru
# all_threads package for Altaire XMPP bot

getThreads = lambda: [x.getName() for x in smartThr.enumerate()]

command_all_threads = lambda source, parameters: \
fmsg(source, (enumerateLines(getThreads()) if parameters else translate['outOfArguments']))

reg_command('all_threads', command_all_threads)
