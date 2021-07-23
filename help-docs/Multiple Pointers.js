



var sorted_array = [-2,-1,0]

function zeroSum(array){
    pointer1 = 0
    hmap2 ={};


    for(i=0; i < sorted_array.length; i++){

        hmap2[array[i]] = Math.abs(array[i] - 0);


}
    for(let key in hmap2){
      if(Math.abs(array[pointer1]) in hmap2){
        if(Math.abs(array[pointer1]) !== array[pointer1])

        var new_array = [array[pointer1], Math.abs(array[pointer1])]
        return console.log(new_array)

      }
      else{
            
        pointer1 += 1;

    }

    }



}
zeroSum(sorted_array)
