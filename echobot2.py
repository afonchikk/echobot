#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.

This program is dedicated to the public domain under the CC0 license.

This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""


q1t = "To list your token on CHAOEX please send your query to business-cn@chaoex.com.hk and provide us with the information about your project. We will revise it as soon as possible and get back to you."
q2t = "CHAOEX KYC verification has 3 levels, KYC1 is for basic user, KYC2 is for real name authentication users, KYC3 is for video authentication users. For KYC2 certification click the personal information in the Chaoex account [real-name authentication], then fill in personal information and submit; Note: The photo size cannot exceed 2M. For KYC3 verification you need to add WeChat account. After KYC2 verification is passed, click on the real name authentication and follow the page prompts to scan the QR code to add the WeChat info to proceed KYC3 video authentication. Please provide the name and UID , and the customer service personnel will guide the user to do the video authentication after approval."
q3t = "There are two major differences: 1.Different trading fee; 2.Different withdraw limits. \n \nKYC1 verification allows to do trading and deposit, transactions are subjected to 0.1% one-way fee for each. KYC2 verification allows to do trading, deposit and withdraw daily limitation is 5 BTC, transactions are subjected to 0.075% one-way fee for each. KYC3 verification allows to do trading, deposit and withdraw daily limitation is 20 BTC, transactions are subjected to 0.05% one-way fee for each. Online deposit/ withdraw rate details：https://www.chaoex.io/rateexplain"
q4t = "In order to comply with the anti-money laundering and anti-terrorism financing laws and regulations of the authorities in various countries, the registered users are obliged to carry out real-name authentication. Therefore, in order to ensure the security of the platform user's assets, real-name authentication is the primary task for users to protect their own rights and interests."
q5t = "Click the \"Account Security\" under \"Personal Information\" in the home page menu of the website to change the login password or transaction password. Please note that when you change your password, you need to obtain the verification code through the registered email or mobile phone number. If you do not receive the verification code, please check the \"spam\" or disable the mobile phone intercept software."
q6t = "Log in to the Chaoex account. In the “Personal Information”, select “linking Modification of Mobile Number” and click “Edit” button and follow the instructions. Log in to the Chaoex account. In [Personal Information], select [E-mail linking Modify] and click the ‘Edit’ button and follow the instructions."
q7t = "Please check the following link for the guidelines: https://chaoex-en-us.udesk.cn/hc/articles/64953"
q8t = "That usually happens for two reasons: 1. The code being intercepted to the trash or junk mail. 2. You get email verification too often; Please check the junk mail, repeat the procedure, report the problem to one of our moderators and wait for help."
q9t = "The following conditions may exist when virtual assets are frozen: 1. Trading orders have not been executed or partially dealt; 2. Submitted a withdraw application. \nThe funds will be automatically thawed when the corresponding order is revoked. If not, please report the problem to one of our moderators."
q10t = "If your order has not been traded, first please check the price of your pending order, whether it has provided a competitive price, so that it can be established with the counterparty; You can cancel the order and re-open the price of the order as quickly trade; If you can't cancel your account pending order or have other errors, please send us an email or submit an application to us and attach an error point out or an error screenshot. We will deal with it as soon as possible."
q11t = "Please use the following link to see the trading guidelines: https://chaoex-en-us.udesk.cn/hc/articles/64973"
q12t = "In case of deposit/ withdraw failure, please go through the following procedures first: https://chaoex-en-us.udesk.cn/hc/articles/64967 \nIf it doesn’t help, please report the issue with the screenshot to our moderators or Customer Service support-en@chaoex.com.hk"

greet_text = "Thank you for joining CHAOEX community! \nHere you can find the list of frequently asked questions.\nLook through please and let us know if there anything else we can help you with! \n \nIf you don't want me to answer here in the groupe chat, send me a private message!\n\n"

question_list = "/question_1 - How to list my token on CHAOEX?\n" \
                "/question_2 - How to do the KYC verification? \n" \
                "/question_3 - What’s the difference between KYC levels?\n" \
                "/question_4 - Why do you need a real-name authentication?\n" \
                "/question_5 - How to reset the password?\n" \
                "/question_6 - How to link or change mobile and e-mail address? \n" \
                "/question_7 - How to use google 2-step Verification？\n" \
                "/question_8 - What if I can’t receive the mail verification code?\n" \
                "/question_9 - What if my virtual assets are frozen?\n" \
                "/question_10 - What I can do in case of Transaction error?\n" \
                "/question_11 - Trading Procedure.\n" \
                "/question_12 - Unsuccessful deposit/withdraw application."



from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def q1(bot, update):
    update.message.reply_text(q1t)
def q2(bot, update):
    update.message.reply_text(q2t)
def q3(bot, update):
    update.message.reply_text(q3t)
def q4(bot, update):
    update.message.reply_text(q4t)
def q5(bot, update):
    update.message.reply_text(q5t)
def q6(bot, update):
    update.message.reply_text(q6t)
def q7(bot, update):
    update.message.reply_text(q7t)
def q8(bot, update):
    update.message.reply_text(q8t)
def q9(bot, update):
    update.message.reply_text(q9t)
def q10(bot, update):
    update.message.reply_text(q10t)
def q11(bot, update):
    update.message.reply_text(q11t)
def q12(bot, update):
    update.message.reply_text(q12t)



def start(bot, update):
    """Echo the user message."""
    update.message.reply_text(greet_text + question_list)

def info(bot, update):
    """Echo the user message."""
    update.message.reply_text(greet_text + question_list)

def greet(bot, update):
    """Echo the user message."""
    if len(update.message.new_chat_members) > 0:
        new_member_name = ""
        if len(update.message.new_chat_members) == 1:
            new_member_name = update.message.new_chat_members[0]['first_name']
        else:
            new_member_name = "everyone"
        update.message.reply_text("Hello, {}!\n".format(new_member_name) + greet_text + question_list)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)



def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("643187200:AAH3z8uQZQ-5tuPiN8fbvsXUo7OWNuk2FWk")


    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("question_1", q1))
    dp.add_handler(CommandHandler("question_2", q2))
    dp.add_handler(CommandHandler("question_3", q3))
    dp.add_handler(CommandHandler("question_4", q4))
    dp.add_handler(CommandHandler("question_5", q5))
    dp.add_handler(CommandHandler("question_6", q6))
    dp.add_handler(CommandHandler("question_7", q7))
    dp.add_handler(CommandHandler("question_8", q8))
    dp.add_handler(CommandHandler("question_9", q9))
    dp.add_handler(CommandHandler("question_10", q10))
    dp.add_handler(CommandHandler("question_11", q11))
    dp.add_handler(CommandHandler("question_12", q12))



    # greet new member
    dp.add_handler(MessageHandler(None, greet))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
