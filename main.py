import sys

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor

from lpmcbot import commands
from lpmcbot.commander import CommanderFactory


if __name__ == '__main__':
    if len(sys.argv) > 1:
        chan = sys.argv[1]
    else:
        chan = 'lpmcbot'

    if len(sys.argv) > 2:
        nickname = sys.argv[2]
    else:
        nickname = 'lpmcbot'

    reactor.connectTCP('irc.freenode.net', 6667,
        CommanderFactory('#' + chan, nickname))
    reactor.run()
