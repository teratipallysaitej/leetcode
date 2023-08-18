class TrieNode{
  constructor() {
    this.node = {}
    this.isend = false
    this.prefix = 0
    this.word = 0
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
      if(word[i] in curr.node){
        curr = curr.node[word[i]]
      }else{
        curr.node[word[i]] = new TrieNode()
        curr = curr.node[word[i]]
      }
      curr.prefix += 1
    }
    curr.end = true
    curr.word += 1
};

/** 
 * @param {string} word
 * @return {number}
 */
Trie.prototype.countWordsEqualTo = function(word) {
    curr = this.head
    for(let i = 0;i<word.length;i++){
      if(word[i] in curr.node){
        curr = curr.node[word[i]]
      }
      else{
        return 0
      }
    }
    if(curr.end){
      return curr.word
    }
    return 0
};

/** 
 * @param {string} prefix
 * @return {number}
 */
Trie.prototype.countWordsStartingWith = function(word) {
    curr = this.head
    for(let i = 0;i<word.length;i++){
      if(word[i] in curr.node){
        curr = curr.node[word[i]]
      }
      else{
        return 0
      }
    }
    console.log(curr.prefix)
    return curr.prefix
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.erase = function(word) {
    curr = this.head
    for(let i = 0;i<word.length;i++){
        curr = curr.node[word[i]]
        curr.prefix -= 1
    }
    curr.word -= 1
    if(curr.word == 0){
      curr.isend = false
    }
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.countWordsEqualTo(word)
 * var param_3 = obj.countWordsStartingWith(prefix)
 * obj.erase(word)
 */