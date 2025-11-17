# question 1:
def solution(X, Y):
    def parse(arr):
        parsed = []
        for i in range(0, len(arr), 2):
            val = arr[i]
            prob = arr[i+1]
            parsed.append((val, prob))
        return parsed
    
    x_pairs = parse(X)
    y_pairs = parse(Y)

    weights = {}
    for x_val, x_prob in x_pairs:
        x_sq = x_val * x_val
        for y_val, y_prob in y_pairs:
            z = x_sq - y_val
            w = x_prob * y_prob
            weights[z] = weights.get(z, 0) + w
    print(weights.items())
    sorted_items = sorted(weights.items(), key = lambda kv: (kv[1], kv[0]))
    return [z for z,_ in sorted_items]

# question 2:
def solution(S):
    class Cleaner(HTMLParser):
        def __init__(self):
            super().__init__()
            self.out = []
        def handle_starttag( self, tag, attrs):
            attrs = dict(attrs)
            if tag == "a":
                href = attrs.get("href")
                if href:
                    self.out.append(f"(link:{href})")
            elif tag == "img":
                src = attrs.get("src")
                if src:
                    self.out.append(f"(image:{src})")
                    
        def handle_data(self, data):
            words = re.findall(r"[A-Za-z0-9]+", data)
            self.out.extend(w.lower() for w in words)
    parser = Cleaner()
    parser.feed(S)
    parser.close()
    return " ".join(parser.out)

# question 3:
def solution(X,Y,Z):
    x2 = [x*x for x in X]
    y2 = [y*y for y in Y]
    best_mae = float('inf')
    best_a, best_b = 0,0
    for a in range(-100,101):
        for b in range(-100,101):
            total_abs_err = 0
            for xi2, yi2, zi in zip(x2,y2,Z):
                pred = a*xi2 + b*yi2
                total_abs_err += abs((pred-zi))
            mae = total_abs_err/len(Z)
            if mae < best_mae:
                best_mae = mae
                best_a, best_b = a,b
    return [best_a, best_b]