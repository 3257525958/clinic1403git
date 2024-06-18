// using from global funtion
console.log(Num2persian(1398)); // یک هزار و سیصد و نود و هشت

// number prototype
console.log((1398).num2persian()); // یک هزار و سیصد و نود و هشت
console.log((1.398).num2persian()); // یک ممیز سیصد و نود و هشت هزارم
console.log((-13980).num2persian()); // منفی سیزده هزار و نهصد و هشتاد 

// string prototype
console.log("1,399".num2persian()); // یک هزار و سیصد و نود و هشت
console.log("1400".num2persian()); // یک هزار و چهارصد