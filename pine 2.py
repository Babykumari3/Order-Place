strategy("intradaygeeks ema", overlay=true)
num1=input(25,title='ema1')
num2=input(50,title="ema1")
ema1=ema(close,num1)
ema2=ema(close,num2)
plot(ema1,title="ema1",color=color.white)
plot(ema2,title="emal", color=color.yellow)

exitlong=crossunder(ema1,ema2)
exitshort=crossover(ema1,ema2)

longCondition = crossover(sma1,ema2)
if (longCondition)
    strategy.entry("BUY", strategy.long)

shortCondition = crossunder(ema1,ema2)

if (shortCondition)
      strategy.entry("SELL", strategy.short)

if(exitlong)
    stategy.close(id="BUY",comment="exitlong")

