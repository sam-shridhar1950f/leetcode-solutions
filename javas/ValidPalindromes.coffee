validPalindromes = (string1) ->
  inplace_str = string1.toLowerCase()
  reverse_str = string1.split('').reverse().join('').toLowerCase()
  lis = []
  lis2 = []
  i = 0
  while i < reverse_str.length
    if /[a-z0-9]/.test(reverse_str[i]) == true
      lis.push reverse_str[i]
      new_reverse_str = lis.join('')
      rev_str = new_reverse_str.replace(/\s/g, '')
    i++
  j = 0
  while j < inplace_str.length
    if /[a-z0-9]/.test(inplace_str[j]) == true
      lis2.push inplace_str[j]
      new_str = lis2.join('')
      str = new_str.replace(/\s/g, '')
    j++
  console.log reverse_str
  if str == rev_str
    console.log true
  else
    console.log false

validPalindromes 'A man, a plan, a canal: Panama'

