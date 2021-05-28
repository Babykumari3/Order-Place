strategy("Doge SMA",Overlay=true)

fast_ma=sma(close,5)
slow_ma=sma(close,15)

plot(fast_ma,color=color.green,linewidth=1)
plot(slow_ma,color=color.yellow,linewidth=3)

bye_condition=crossover(fast_ma,slow_ma)
sell_condition=crossunder(fast_ma, slow_ma)

strategy.entry("doge door", strategy.long, 10000, when=bye_condition)
strategy.close("doge door" , when=sell_condition)