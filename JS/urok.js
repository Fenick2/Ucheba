const myDate = new Date();
console.log(myDate);
myDate.setFullYear(2017, 4, 22);
myDate.setDate(myDate.getDate() + 10);
console.log(myDate);