var TimeLimitedCache = function() {
    this.mp = {}; // Store the cache map as an instance property
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    // If the key already exists, clear the previous timer
    if (key in this.mp) {
        clearTimeout(this.mp[key].timer);
    }

    const alreadyExists = key in this.mp;
    // Create a timer to delete the key after the specified duration
    const timer = setTimeout(() => {
        delete this.mp[key];
    }, duration);

    this.mp[key] = { value, timer }; // Store the value along with the timer

    return alreadyExists;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (key in this.mp) {
        return this.mp[key].value; // Return the value from the stored object
    }
    return -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.mp).length; // Use Object.keys to get the count of keys
};

/**
 * Usage:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */
