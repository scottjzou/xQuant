# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 08:16:59 2015

@author: Administrator
"""
import numpy as np
import AsianOption as AmOp
import time
import os
print os.getcwd()
L=1.0
s0=200.0
r=0.04
q=0.02
K=200.0
Sigma=0.4
T=1.0
phi=1.0
#Call= AsianOption.GeometricAverage(L,s0,r,q,K,Sigma,T,phi)
#call=AsianOption.ArithmeticAverage(L,s0,s0,r,q,K,Sigma,T,T,phi)
#print Call
N=250

time0=time.time()
Call=AmOp.CurranApprox(L,s0,r,q,K,Sigma,T,phi,N)
print Call, time.time()-time0