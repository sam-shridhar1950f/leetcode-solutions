var sorted_array = [-3,-2,-1,0,1,2,3]

function zeroSum(array){

    hmap = {};
    hmap2 ={};

    for(i=0; i < sorted_array.length; i++){

        hmap[array[i]] = Math.abs(array[i] - 0);

    }

    for(i=0; i < sorted_array.length; i++){

        hmap2[array[i]] = Math.abs(array[i] - 0);


}
console.log(hmap)
}

zeroSum(sorted_array)