class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) { // Input: ["neet","code","love","you"]
        let stringEncoded = '';
        for(let word of strs){
            stringEncoded += word.length + "#" + word;
        };

        return stringEncoded; //Input: "4#neet4#code4#love3#you"
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = [];
        let i = 0;
        while (i<str.length) {
            let hash_index = str.indexOf('#',i);
            let string_length = parseInt(str.substring(i,hash_index));
            let final_string = str.substring((hash_index+1),(hash_index + 1 + string_length));
            res.push(final_string);
            i = hash_index + 1 + string_length//i will be the next item;  

        }


        return res;
    }
};
