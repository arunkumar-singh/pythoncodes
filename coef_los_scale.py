# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 17:31:55 2016

@author: aks
"""

from numpy import *

def coef_los_scale(xt_1, yt_1, theta_1, vel_1, xt_2, yt_2, theta_2, vel_2):
    
     xdot_1 = vel_1*cos(theta_1)     
     ydot_1 = vel_1*sin(theta_1)
     xdot_2 = vel_2*cos(theta_2)
     ydot_2 = vel_2*sin(theta_2)  
    
     A12 = ydot_1*(xt_1-xt_2)-xdot_1*(yt_1-yt_2)
     B12 = xdot_2*(yt_1-yt_2)-ydot_2*(xt_1-xt_2)
     
     return A12, B12