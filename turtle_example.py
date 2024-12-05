#!/usr/bin/env python3

from turtle import *
bgcolor('black')
speed(30)
color('aqua')
for i in range(160):
    rt(i)
    circle(150,i)
    fd(i)
    rt(90)
hideturtle()
done()
