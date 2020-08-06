function testCycle(n) {
    var x=0;
    
    while (n>0) {
        x += n--;
    }
    return x;
}

console.log(testCycle(3))
