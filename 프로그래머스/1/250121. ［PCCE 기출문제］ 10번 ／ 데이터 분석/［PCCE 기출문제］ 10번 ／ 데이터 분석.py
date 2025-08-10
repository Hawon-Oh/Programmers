def solution(data, ext, val_ext, sort_by):
    arr = [d for d in data if d[["code", "date", "maximum", "remain"].index(ext)] < val_ext]
    arr.sort(key=lambda x: x[["code", "date", "maximum", "remain"].index(sort_by)])
    
    return arr