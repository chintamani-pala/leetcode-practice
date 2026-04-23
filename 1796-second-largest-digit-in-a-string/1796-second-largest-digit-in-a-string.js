/**
 * @param {string} s
 * @return {number}
 */

var secondHighest = function(s) {
    let firstLargest = -Infinity;
    let secondLargest = -Infinity;
    for(let num of s){
        let currentNumber = Number(num)
        if(!Number.isNaN(currentNumber)){
            if(currentNumber == firstLargest) continue
            if(currentNumber > firstLargest){
                secondLargest = firstLargest;
                firstLargest = currentNumber;
            }
            else if(secondLargest < currentNumber){
                secondLargest = currentNumber;
            }
        }
    }
    return secondLargest === -Infinity ? -1 : secondLargest;
};