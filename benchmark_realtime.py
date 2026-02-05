import time
import logging
from tvDatafeed import TvDatafeed, Interval

# Configure logging to suppress debug output during benchmark
logging.basicConfig(level=logging.INFO)

def benchmark():
    tv = TvDatafeed()
    
    # 20 diverse symbols (Indices, Stocks, Crypto, Forex)
    # Using specific exchanges to ensure they work
    symbols = [
        "NSE:RELIANCE", "NSE:TCS", "NSE:INFY", "NSE:HDFCBANK", "NSE:ICICIBANK",
        "NASDAQ:AAPL", "NASDAQ:MSFT", "NASDAQ:GOOGL", "NASDAQ:AMZN", "NASDAQ:TSLA",
        "NYSE:BABA", "NYSE:NIO", "NYSE:F", "NYSE:GE", "NYSE:T",
        "BINANCE:BTCUSDT", "BINANCE:ETHUSDT", "BINANCE:BNBUSDT", "BINANCE:ADAUSDT", "BINANCE:XRPUSDT"
    ]

    print(f"Benchmarking with {len(symbols)} symbols...")

    # Method A: Loop get_hist
    print("\nMethod A: Loop get_hist (1 bar)...")
    start_time_a = time.time()
    for symbol in symbols:
        try:
            # parsing exchange and symbol
            if ":" in symbol:
                exchange, sym = symbol.split(":")
            else:
                exchange = "NSE" # Default
                sym = symbol
            
            # get_hist takes symbol and exchange
            # We request 1 bar to be as fast as possible
            tv.get_hist(symbol=sym, exchange=exchange, n_bars=1, interval=Interval.in_daily)
            # print(f"Fetched {symbol}")
        except Exception as e:
            print(f"Failed {symbol}: {e}")
    end_time_a = time.time()
    duration_a = end_time_a - start_time_a
    print(f"Method A took {duration_a:.2f} seconds")

    # Method B: Batch get_quotes
    print("\nMethod B: Batch get_quotes...")
    start_time_b = time.time()
    try:
        quotes = tv.get_quotes(symbols, timeout=10.0) # slightly larger timeout for benchmark safety
        print(f"Fetched {len(quotes)} quotes")
        # Optional: print one to verify structure
        if quotes:
            first_key = list(quotes.keys())[0]
            print(f"Sample quote for {first_key}: {quotes[first_key]}")
    except AttributeError:
        print("get_quotes not implemented yet")
        duration_b = 9999
    except Exception as e:
        print(f"Method B failed: {e}")
        duration_b = 9999
    else:
        end_time_b = time.time()
        duration_b = end_time_b - start_time_b
        print(f"Method B took {duration_b:.2f} seconds")

    # Comparison
    if duration_b < duration_a:
        speedup = duration_a / duration_b
        print(f"\nSpeedup: {speedup:.2f}x")
    else:
        print("\nNo speedup or failure.")

if __name__ == "__main__":
    benchmark()
