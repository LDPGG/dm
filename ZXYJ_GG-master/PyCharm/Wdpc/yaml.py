from qqbot import QQBotSlot as qqbotslot, RunBot


@qqbotslot
def onQQMessage(bot, contact, member, content):
    if content == '你不配':
        bot.SendTo(contact, '我配')


if __name__ == '__main__':
    RunBot()