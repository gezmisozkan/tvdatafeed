import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tvDatafeed import TvDatafeed

tv = TvDatafeed()

print("Testing find_exchange:")
symbols = ['AAPL', 'MSFT', 'BTCUSDT', 'UNKNOWNKEYWORD123', "THYAO"]

for s in symbols:
    ex = tv.find_exchange(s)
    print(f"Symbol: {s}, Exchange: {ex}")
