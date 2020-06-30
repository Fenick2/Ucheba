function testFactorial(a) {
    var x=1;
    for (i = 1; i <= a; i++) {
        x *= i;
    }
    return x;
}

console.log(testFactorial(7))