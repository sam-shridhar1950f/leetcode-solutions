// Add comments

function anagram(str1, str2){

    

    if(str1.length != str2.length){

        return console.log(false);



    }

    let freq_counter1 = {};
    let freq_counter2 = {};

    for(let letter of str1){

        freq_counter1[letter] = (freq_counter1[letter] || 0) + 1;

    }

    for(let val of str2){


        freq_counter2[val] = (freq_counter2[val] || 0) + 1;

    }


    for(let key in freq_counter1){
        if(!(key in freq_counter2)){
            return console.log(false);
        }
        if(freq_counter1[key] !== freq_counter2[key]){
            return console.log(false);
        }
        else{
            continue;
        }

        

    }
    return console.log(true);

}


anagram('qweryt', 'qwerty');

