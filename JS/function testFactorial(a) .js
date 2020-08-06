function testFactorial(a) {
    let x=1;
    for (let i = 1; i <= a; i++) {
        x *= i;
    }
    return x;
}

console.log(testFactorial(7))