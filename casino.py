#-*- coding: utf-8 -*-

secret = 7
guess = int(raw_input("Ugani številko:"))

if guess == secret:
    print ("Čestitam! Zadel si jackpot!")
else:
    print ("Več sreče prihodnjič!")