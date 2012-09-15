# /* encoding: utf-8 */
# Copyright Altaire bot © Assassin, 2011 - 2012
# This program published under Apache 2.0 license
# See LICENSE for more details
# My EMail: assassin@sonikelf.ru
# whats_color package for Altaire XMPP bot
# the first entertaining plugin for altaire

if not 'packages/whats_color/grab.zip' in sys.path:
	sys.path.insert(0, 'depends/grab/grab.zip')

from re import compile as RCompile
from HTMLParser import HTMLParser
from grab import Grab

finder = RCompile("<td width='16%'/><td>(.+?)</td></tr>", 16)

def command_whats_color(source, parameters):
	if parameters:
		grab = Grab()
		grab.go('xml.yandex.net/cgi/color-search.pl')
		grab.set_input('query', parameters)
		fmsg(source, replaceHTML(finder.search(grab.submit().body).group(1)))
	else: fmsg(source, translate['outOfArguments'])

reg_command('whats_color', command_whats_color)
