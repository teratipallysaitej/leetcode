var LRUCache = function(capacity) {
    this.capacity = capacity;
    this.mp = new Map(); // Use a Map object
};

LRUCache.prototype.get = function(key) {
    if (!this.mp.has(key)) {
        return -1;
    }
    var val = this.mp.get(key); // Declare val with var
    this.mp.delete(key);
    this.mp.set(key, val);
    return val;
};

LRUCache.prototype.put = function(key, value) {
    if (this.mp.has(key)) {
        this.mp.delete(key);
    }
    this.mp.set(key, value);
    if (this.mp.size > this.capacity) { // Use size property of Map
        this.mp.delete(this.mp.keys().next().value); // Delete the first key
    }
};

// Usage example:
// var obj = new LRUCache(capacity);
// var param_1 = obj.get(key);
// obj.put(key, value);