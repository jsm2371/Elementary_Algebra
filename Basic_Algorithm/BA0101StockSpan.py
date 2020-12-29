

def SimpleStockSpan(quotes):
    size_quote = len(quotes)
    spans = [0 for i in range(size_quote)]
    for current_time in range(size_quote):
        span_count = 1
        span_end = False
        while current_time - span_count >= 0 and not span_end:
            if quotes[current_time] >= quotes[current_time - span_count]:
                span_count += 1
            else:
                span_end = True
        spans[current_time] = span_count
    return spans


