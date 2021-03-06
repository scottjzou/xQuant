# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 09:34:10 2015

@author: Administrator
"""
from numpy import *
from scipy.stats import norm, lognorm
from scipy.integrate import quad

def GeometricAverage(L,s0,r,q,K,Sigma,T,phi):
    SigmaA=Sigma/sqrt(3.0)
    ba=0.5*(r-q-Sigma*Sigma/6.0)
    d1=(log(s0/K)+(ba+0.5*SigmaA*SigmaA)*T)/SigmaA/sqrt(T)
    d2=d1-SigmaA*sqrt(T)
    OptVal=phi*L*(s0*exp((ba-r)*T)*norm.cdf(phi*d1,0.0,1.0)-K*exp(-r*T)*norm.cdf(phi*d2,0.0,1.0))
    return OptVal
    

def CurranApprox(L,s0,r,q,K,Sigma,T,phi,N):
    dt=T/N
    iy=array(range(1,N+1,1),ndmin=2)
    ix=transpose(iy)
    Mu_lnS=log(s0)+(r-q-0.5*Sigma**2.)*ix*dt
    Var_lnS=Sigma**2*ix*dt
    Corr_lnS=sqrt(gygMin(ix*ones((1,N)),iy*ones((N,1)))/gygMax(ix*ones((1,N)),iy*ones((N,1))))
    CoVar_lnS=sqrt(dot(Var_lnS,transpose(Var_lnS)))*Corr_lnS
    Mu_lnG=mean(Mu_lnS)
    Var_lnG=dot(sqrt(transpose(Var_lnS)),dot(Corr_lnS,sqrt(Var_lnS)))/N**2.
    Var_lnSG=sqrt(Var_lnS)*dot(Corr_lnS,sqrt(Var_lnS))/N
    
    Part21=exp(Mu_lnS+0.5*Var_lnS)*norm.cdf((Mu_lnG-log(K))/sqrt(Var_lnG)+Var_lnSG/sqrt(Var_lnG),0.,1.)
    Part21=mean(Part21)
    Part22=K*norm.cdf((Mu_lnG-log(K))/sqrt(Var_lnG))
    Part2=Part21-Part22
    
    CoVar_lnSonlnG=CoVar_lnS-dot(dot(CoVar_lnS,ones((N,1))),transpose(dot(CoVar_lnS,ones((N,1)))))/sum(sum(CoVar_lnS))
    Mu_lnSonlnG=Mu_lnS+Var_lnSG/Var_lnG*(log(K)-Mu_lnG)
    Mu_AonlnG=mean(exp(Mu_lnSonlnG+0.5*reshape(diag(CoVar_lnSonlnG),(-1,1))))
    Var_SonlnG=exp(Mu_lnSonlnG+0.5*reshape(diag(CoVar_lnSonlnG),(-1,1)))
    CoVar_SonlnG=(Var_SonlnG*ones((1,N)))*transpose(Var_SonlnG*ones((1,N)))*(exp(CoVar_lnSonlnG)-1.0)
    Var_AonlnG=sum(sum(CoVar_SonlnG))/N**2.
    
    Mu_Diff=Mu_AonlnG-K
    Var_Diff=copy(Var_AonlnG)
    Var_lnDiff=log(Var_Diff/Mu_Diff**2.+1)
    Diff0=copy(Mu_Diff)
    es=0.000000000001
    K=K-es
    
    func=lambda x:iBSOption(Diff0,Var_lnDiff,K,x,Mu_lnG,Var_lnG)
    Part1,IntError=quad(func,es,K)
    return float(L*(Part1+Part2)*exp(-r*T))



def gygMax(a,b):
    c=copy(a)
    if size(b)==1:
        c[a<b]=b
    else:
        c[a<b]=b[a<b]
    return c



def gygMin(a,b):
    c=copy(a)
    if size(b)==1:
        c[a>b]=b
    else:
        c[a>b]=b[a>b]
    return c



def iBSOption(Diff0,Var_lnDiff,K,G,Mu_lnG,Var_lnG):
    d1=(log(Diff0/(K-G)))/sqrt(Var_lnDiff)+0.5*sqrt(Var_lnDiff)
    d2=d1-sqrt(Var_lnDiff)
    OptVal=Diff0*norm.cdf(d1,0.,1.)-(K-G)*norm.cdf(d2,0.,1.)
    return OptVal*lognorm.pdf(G,sqrt(Var_lnG),0,exp(Mu_lnG))
    
    
    