#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

import logging

def shopping_log(username, item):
    for i in item:
        filename = "..\\log\\%s.log" % username
        logging.basicConfig(filename=filename,
                            level=logging.INFO,
                            format='%(asctime)s %(message)s',
                            datefmt ='%m-%d-%Y %H:%M:%S')

        message = "%s has been purchased successfully." % i
        logging.info(message)

def withdraw_log(username, amount):
    filename = "..\\log\\%s.log" % username
    logging.basicConfig(filename=filename,
                            level=logging.INFO,
                            format='%(asctime)s %(message)s',
                            datefmt ='%m-%d-%Y %H:%M:%S')

    message = "-%d has been withdrawed successfully. Surcharge is %d." % (amount, amount * 0.05)
    logging.info(message)

def transfer_log(username, target, amount):
    loggerUsername = logging.getLogger(username)
    loggerTarget = logging.getLogger(target)

    loggerTarget.setLevel(logging.INFO)
    loggerUsername.setLevel(logging.INFO)

    handlerUsername = logging.FileHandler("..\\log\\%s.log" % username)
    handlerTarget = logging.FileHandler("..\\log\\%s.log" % target)

    formatter = logging.Formatter('%(asctime)s %(message)s', '%m-%d-%Y %H:%M:%S')

    handlerTarget.setFormatter(formatter)
    handlerUsername.setFormatter(formatter)

    loggerUsername.addHandler(handlerUsername)
    loggerTarget.addHandler(handlerTarget)

    loggerTarget.info("Recieved +%d from %s." % (amount, username))
    loggerUsername.info("-%d has been transfered to %s successfully." % (amount, target))

def pay_back_log(username, amount):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("..\\log\\%s.log" % username)
    formatter = logging.Formatter('%(asctime)s %(message)s', '%m-%d-%Y %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("+%d has been payed bay to bank" % amount)

def add_account(admin, user):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("..\\log\\admin.log")
    formatter = logging.Formatter('%(asctime)s %(message)s', '%m-%d-%Y %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("Administrator %s creates an account named %s" % (admin, user))


def change_account_limit(admin, user, limit):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("..\\log\\admin.log")
    formatter = logging.Formatter('%(asctime)s %(message)s', '%m-%d-%Y %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("Administrator %s modified the limite of account named %s to %d" % (admin, user, limit))


def froze_account(admin, user):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("..\\log\\admin.log")
    formatter = logging.Formatter('%(asctime)s %(message)s', '%m-%d-%Y %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("Administrator %s forze the account named %s" % (admin, user))