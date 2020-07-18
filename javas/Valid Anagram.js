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

/* Colt's Solution
function validAnagram(first, second) {
  if (first.length !== second.length) {
    return false;
  }

  const lookup = {};

  for (let i = 0; i < first.length; i++) {
    let letter = first[i];
    // if letter exists, increment, otherwise set to 1
    lookup[letter] ? lookup[letter] += 1 : lookup[letter] = 1;
  }
  console.log(lookup)

  for (let i = 0; i < second.length; i++) {
    let letter = second[i];
    // can't find letter or letter is zero then it's not an anagram
    if (!lookup[letter]) {
      return false;
    } else {
      lookup[letter] -= 1;
    }
  }

  return true;
}

// {a: 0, n: 0, g: 0, r: 0, m: 0,s:1}
validAnagram('anagrams', 'nagaramm')

*/