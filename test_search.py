import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tvDatafeed import TvDatafeed
tv = TvDatafeed()

# Check valid ticker
matches = tv.search_symbol(symbol='AAPL')
if matches:
    print("Found:", matches[0]['symbol'])
else:
    print("Ticker not found")