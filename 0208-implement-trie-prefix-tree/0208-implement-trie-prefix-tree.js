class TrieNode {
    constructor(){
        this.node = {}
        this.end = false
    }
}

var Trie = function() {
    this.head = new TrieNode()
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    curr = this.head
    for(let i = 0;i<word.length;i++){
        if(!(word[i] in curr.node)){
            curr.node[word[i]] = new TrieNode()
            curr = curr.node[word[i]]
        }
        else{
            curr = curr.node[word[i]]
        }

    }
    curr.end = true
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    curr = this.head
    for(let i =0;i<word.length;i++){
        if(!(word[i] in curr.node)){
            return false
        }
        else{
            curr = curr.node[word[i]]
        }
    }    
    return curr.end
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    curr = this.head
    for(let i = 0;i<prefix.length;i++){

        if(!(prefix[i] in curr.node)){
            return false
        }
        else{
            curr = curr.node[prefix[i]]
        }
    }    
    return true
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */