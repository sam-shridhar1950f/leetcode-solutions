function validPalindromes(string1){

    var inplace_str = string1.toLowerCase()
    var reverse_str = string1.split("").reverse().join("").toLowerCase();
    lis = []
    lis2 = []
    for(i = 0; i < reverse_str.length; i++){

        if (/[a-z0-9]/.test(reverse_str[i]) === true){

            
               lis.push(reverse_str[i])
               var new_reverse_str = lis.join("")
               var rev_str = new_reverse_str.replace(/\s/g,''); 

        }

    }

    for(j=0; j < inplace_str.length; j++){

        if (/[a-z0-9]/.test(inplace_str[j]) === true){

            
            lis2.push(inplace_str[j])
            var new_str = lis2.join("")
            var str = new_str.replace(/\s/g,''); 



    }

    }


    console.log(reverse_str)
    if(str == rev_str){

        return console.log(true)
    }
    else{
        return console.log(false)
    }





}

validPalindromes("A man, a plan, a canal: Panama")