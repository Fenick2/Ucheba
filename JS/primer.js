function testWhile(a) {
    var x=0; y=1;
    while (y <= a) {
        if (y % 2 == 0) {
            x = x+y;
        }
        y++;
    }
    return x;
}

console.log(testWhile(3))