
function charCount(string){
    var freq = {}; // initializing object
    var new_str = string.toLowerCase()
    for (var char of new_str){
    if(/[a-z0-9]/.test(char)){ // Regular Expression to check if character is alphanumeric
        if(freq[char]){ // Checking if char is true (1) rather than (0)
            freq[char]++;
        }
        else{ // if char is not in object  set default value to 1
            freq[char] = 1;
        }
    }
    
}
        console.log(freq);
}   
   



charCount("hello")

// for if-else block I could refactor and use freq[char] = ++freq[char] || 1
// ^^ basically says if fre[char] is true do first option, if falsy commit 1 to object