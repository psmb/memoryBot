from regionsMarkup import regionsMarkup


def chooseRegionForNeedHelp(context, message):
    mesg = context.bot.send_message(
        message.chat.id, 'В каком регионе находится место памяти?', reply_markup=regionsMarkup)

    def handler(message):
        if message.text == 'Назад':
            context.user.needHelp = False
            message.text = None
            # start(context, message)
        else:
            if message.text != None:
                context.user.region = message.text
            # roadToRegion(context, message)
    context.bot.register_next_step_handler(mesg, handler)
